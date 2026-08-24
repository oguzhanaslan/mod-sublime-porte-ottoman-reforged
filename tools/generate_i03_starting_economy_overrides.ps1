param(
    [string]$VanillaGameRoot = 'C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game'
)

$ErrorActionPreference = 'Stop'
$modRoot = Split-Path -Parent $PSScriptRoot
$relativeFiles = @(
    'common/history/buildings/01_south_europe.txt',
    'common/history/buildings/08_middle_east.txt'
)

function Find-BracedBlock {
    param([string]$Text, [int]$SearchStart, [string]$Pattern)
    $match = [regex]::Match($Text.Substring($SearchStart), $Pattern, [Text.RegularExpressions.RegexOptions]::Multiline)
    if (-not $match.Success) { return $null }
    $start = $SearchStart + $match.Index
    $open = $Text.IndexOf('{', $start)
    $depth = 0
    for ($i = $open; $i -lt $Text.Length; $i++) {
        if ($Text[$i] -eq '{') { $depth++ }
        elseif ($Text[$i] -eq '}') {
            $depth--
            if ($depth -eq 0) {
                return [pscustomobject]@{ Start = $start; Open = $open; End = $i }
            }
        }
    }
    throw "Unclosed block matching $Pattern"
}

function Get-StateLocation {
    param([hashtable]$Files, [string]$State)
    $found = @()
    foreach ($relative in $relativeFiles) {
        $block = Find-BracedBlock -Text $Files[$relative] -SearchStart 0 -Pattern "^\s*s:$State\s*=\s*\{"
        if ($null -ne $block) { $found += [pscustomobject]@{ Relative = $relative; Block = $block } }
    }
    if ($found.Count -ne 1) { throw "$State found in $($found.Count) vanilla building files" }
    return $found[0]
}

function Edit-TurBlock {
    param([hashtable]$Files, [string]$State, [scriptblock]$Edit)
    $location = Get-StateLocation -Files $Files -State $State
    $stateText = $Files[$location.Relative].Substring($location.Block.Start, $location.Block.End - $location.Block.Start + 1)
    $tur = Find-BracedBlock -Text $stateText -SearchStart 0 -Pattern '^\s*region_state:TUR\s*=\s*\{'
    if ($null -eq $tur) { throw "No TUR region_state block in $State" }
    $turText = $stateText.Substring($tur.Start, $tur.End - $tur.Start + 1)
    $edited = & $Edit $turText
    $absoluteStart = $location.Block.Start + $tur.Start
    $Files[$location.Relative] = $Files[$location.Relative].Remove($absoluteStart, $turText.Length).Insert($absoluteStart, $edited)
}

function Find-BuildingBlock {
    param([string]$TurText, [string]$Building)
    $search = 0
    $found = @()
    while ($true) {
        $block = Find-BracedBlock -Text $TurText -SearchStart $search -Pattern '^[\t ]*create_building\s*=\s*\{'
        if ($null -eq $block) { break }
        $value = $TurText.Substring($block.Start, $block.End - $block.Start + 1)
        if ($value -match "(?m)^\s*building\s*=\s*`"$([regex]::Escape($Building))`"\s*$") {
            $found += $block
        }
        $search = $block.End + 1
    }
    if ($found.Count -ne 1) { throw "$Building found $($found.Count) times in TUR block" }
    return $found[0]
}

function Remove-Building {
    param([string]$TurText, [string]$Building)
    $block = Find-BuildingBlock -TurText $TurText -Building $Building
    $length = $block.End - $block.Start + 1
    if ($block.End + 2 -lt $TurText.Length -and $TurText.Substring($block.End + 1, 2) -eq "`r`n") { $length += 2 }
    return $TurText.Remove($block.Start, $length)
}

function Set-BuildingLevels {
    param([string]$TurText, [string]$Building, [int]$From, [int]$To)
    $block = Find-BuildingBlock -TurText $TurText -Building $Building
    $value = $TurText.Substring($block.Start, $block.End - $block.Start + 1)
    $matches = [regex]::Matches($value, "(?m)^(\s*levels\s*=\s*)$From\s*$")
    if ($matches.Count -ne 1) { throw "$Building expected one levels=$From entry, found $($matches.Count)" }
    $edited = [regex]::Replace($value, "(?m)^(\s*levels\s*=\s*)$From\s*$", "`${1}$To", 1)
    return $TurText.Remove($block.Start, $value.Length).Insert($block.Start, $edited)
}

function Add-CountryBuilding {
    param([string]$TurText, [string]$Building, [int]$Levels, [string[]]$Methods)
    $methodText = $Methods -join '" "'
    $entry = @"
			# I-03: approved R-06 starting-economy correction.
			create_building={
				building="$Building"
				add_ownership={
					country={
						country="c:TUR"
						levels=$Levels
					}
				}
				reserves=1
				activate_production_methods={ "$methodText" }
			}
"@
    $insertAt = $TurText.LastIndexOf('}') - 2
    $entry += "`r`n`t`t"
    return $TurText.Remove($insertAt, 2).Insert($insertAt, $entry)
}

function Add-ManorBuilding {
    param([string]$TurText, [string]$State, [string]$Building, [int]$Levels, [string[]]$Methods)
    $methodText = $Methods -join '" "'
    $entry = @"
			# I-03: approved R-06 starting-economy correction.
			create_building={
				building="$Building"
				add_ownership={
					building={
						type="building_manor_house"
						country="c:TUR"
						levels=$Levels
						region="$State"
					}
				}
				reserves=1
				activate_production_methods={ "$methodText" }
			}
"@
    $insertAt = $TurText.LastIndexOf('}') - 2
    $entry += "`r`n`t`t"
    return $TurText.Remove($insertAt, 2).Insert($insertAt, $entry)
}

function Add-FinancialBuilding {
    param([string]$TurText, [string]$State, [string]$Building, [int]$Levels, [string[]]$Methods)
    $methodText = $Methods -join '" "'
    $entry = @"
			# I-03: approved R-06 starting-economy correction.
			create_building={
				building="$Building"
				add_ownership={
					building={
						type="building_financial_district"
						country="c:TUR"
						levels=$Levels
						region="$State"
					}
				}
				reserves=1
				activate_production_methods={ "$methodText" }
			}
"@
    $insertAt = $TurText.LastIndexOf('}') - 2
    $entry += "`r`n`t`t"
    return $TurText.Remove($insertAt, 2).Insert($insertAt, $entry)
}

$files = @{}
foreach ($relative in $relativeFiles) {
    $source = Join-Path $VanillaGameRoot $relative
    if (-not (Test-Path $source)) { throw "Missing vanilla source: $source" }
    $files[$relative] = [IO.File]::ReadAllText($source)
}

Edit-TurBlock $files 'STATE_EASTERN_THRACE' {
    param($text)
    $text = Add-CountryBuilding $text 'building_arms_industry' 1 @('pm_muskets','pm_automation_disabled')
    $text = Add-CountryBuilding $text 'building_artillery_foundry' 1 @('pm_cannons','pm_automation_disabled')
    Add-CountryBuilding $text 'building_university' 1 @('pm_scholastic_education')
}
Edit-TurBlock $files 'STATE_BOSNIA' {
    param($text)
    $text = Set-BuildingLevels $text 'building_arms_industry' 2 1
    Remove-Building $text 'building_artillery_foundry'
}
Edit-TurBlock $files 'STATE_MACEDONIA' {
    param($text)
    Add-CountryBuilding $text 'building_port' 1 @('pm_basic_port')
}
Edit-TurBlock $files 'STATE_HUDAVENDIGAR' {
    param($text)
    $text = Remove-Building $text 'building_tea_plantation'
    Add-ManorBuilding $text 'STATE_HUDAVENDIGAR' 'building_silk_plantation' 5 @('default_building_silk_plantation','pm_road_carts')
}
Edit-TurBlock $files 'STATE_AYDIN' {
    param($text)
    $text = Remove-Building $text 'building_tea_plantation'
    Set-BuildingLevels $text 'building_cotton_plantation' 2 3
}
Edit-TurBlock $files 'STATE_KONYA' {
    param($text)
    $text = Remove-Building $text 'building_tea_plantation'
    Add-ManorBuilding $text 'STATE_KONYA' 'building_wheat_farm' 3 @('pm_simple_farming','pm_no_secondary','pm_tools_disabled')
}
Edit-TurBlock $files 'STATE_KASTAMONU' {
    param($text)
    $text = Remove-Building $text 'building_tea_plantation'
    $text = Add-ManorBuilding $text 'STATE_KASTAMONU' 'building_wheat_farm' 3 @('pm_simple_farming','pm_no_secondary','pm_tools_disabled')
    $text = Add-ManorBuilding $text 'STATE_KASTAMONU' 'building_livestock_ranch' 2 @('pm_open_air_stockyards','pm_simple_ranch','pm_standard_fences','pm_unrefrigerated')
    Add-FinancialBuilding $text 'STATE_KASTAMONU' 'building_logging_camp' 2 @('pm_saw_mills','pm_no_hardwood','pm_no_equipment','pm_road_carts')
}
Edit-TurBlock $files 'STATE_TRABZON' {
    param($text)
    $text = Remove-Building $text 'building_tea_plantation'
    $text = Set-BuildingLevels $text 'building_livestock_ranch' 1 2
    Add-ManorBuilding $text 'STATE_TRABZON' 'building_tobacco_plantation' 2 @('default_building_tobacco_plantation','pm_road_carts')
}
Edit-TurBlock $files 'STATE_ERZURUM' {
    param($text)
    $text = Remove-Building $text 'building_tea_plantation'
    Set-BuildingLevels $text 'building_livestock_ranch' 1 2
}
Edit-TurBlock $files 'STATE_KARS' {
    param($text)
    $text = Remove-Building $text 'building_tea_plantation'
    Set-BuildingLevels $text 'building_livestock_ranch' 1 2
}
Edit-TurBlock $files 'STATE_ANKARA' {
    param($text)
    $text = Remove-Building $text 'building_tea_plantation'
    $text = Set-BuildingLevels $text 'building_wheat_farm' 3 4
    Set-BuildingLevels $text 'building_livestock_ranch' 1 3
}
Edit-TurBlock $files 'STATE_DIYARBAKIR' {
    param($text)
    $text = Remove-Building $text 'building_tea_plantation'
    $text = Set-BuildingLevels $text 'building_livestock_ranch' 1 2
    Add-ManorBuilding $text 'STATE_DIYARBAKIR' 'building_wheat_farm' 2 @('pm_simple_farming','pm_no_secondary','pm_tools_disabled')
}

$utf8Bom = [Text.UTF8Encoding]::new($true)
foreach ($relative in $relativeFiles) {
    $destination = Join-Path $modRoot $relative
    [IO.Directory]::CreateDirectory((Split-Path -Parent $destination)) | Out-Null
    [IO.File]::WriteAllText($destination, $files[$relative], $utf8Bom)
}

Write-Output 'I-03 generated: 12 state packages / 29 approved atomic edits.'
