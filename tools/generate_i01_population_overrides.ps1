param(
    [string]$VanillaGameRoot = 'C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game'
)

$ErrorActionPreference = 'Stop'
$modRoot = Split-Path -Parent $PSScriptRoot
$populationCsv = Join-Path $modRoot 'docs/research/data/R02_ottoman_population_proposal.csv'
$vanillaFiles = @(
    'common/history/pops/01_south_europe.txt',
    'common/history/pops/08_middle_east.txt'
)

# Each entry is culture|religion|percentage. These integer, gameplay-grade
# marginals are the approved R-02 proposal resolved to valid Victoria 3 keys.
$plans = @{
    STATE_DOBRUDJA = @('bulgarian|orthodox|40','romanian|orthodox|35','turkish|sunni|25')
    STATE_BASRA = @('mashriqi|shiite|55','mashriqi|sunni|10','bedouin|sunni|30','armenian|oriental_orthodox|5')
    STATE_EASTERN_THRACE = @('turkish|sunni|55','greek|orthodox|25','armenian|oriental_orthodox|10','sephardic|jewish|5','bulgarian|orthodox|5')
    STATE_ALBANIA = @('albanian|sunni|75','albanian|orthodox|10','albanian|catholic|10','greek|orthodox|5')
    STATE_BOSNIA = @('serb|orthodox|45','bosniak|sunni|35','croat|catholic|20')
    STATE_SKOPIA = @('bulgarian|orthodox|45','turkish|sunni|20','albanian|sunni|20','greek|orthodox|10','serb|orthodox|5')
    STATE_MACEDONIA = @('greek|orthodox|45','bulgarian|orthodox|20','turkish|sunni|20','sephardic|jewish|10','albanian|sunni|5')
    STATE_THESSALIA = @('greek|orthodox|80','albanian|orthodox|10','turkish|sunni|10')
    STATE_WESTERN_THRACE = @('greek|orthodox|45','turkish|sunni|35','bulgarian|orthodox|20')
    STATE_NORTHERN_THRACE = @('bulgarian|orthodox|65','turkish|sunni|30','greek|orthodox|5')
    STATE_BULGARIA = @('bulgarian|orthodox|75','turkish|sunni|25')
    STATE_BAGHDAD = @('mashriqi|shiite|50','mashriqi|sunni|15','bedouin|sunni|25','turkish|sunni|5','armenian|oriental_orthodox|5')
    STATE_MOSUL = @('kurdish|sunni|35','mashriqi|sunni|25','mashriqi|shiite|5','turkish|sunni|15','assyrian|oriental_orthodox|10','armenian|oriental_orthodox|10')
    STATE_MONTENEGRO = @('serb|orthodox|70','albanian|sunni|15','bosniak|sunni|15')
    STATE_WESTERN_SERBIA = @('bosniak|sunni|50','serb|orthodox|30','albanian|sunni|15','turkish|sunni|5')
    STATE_EASTERN_SERBIA = @('serb|orthodox|70','albanian|sunni|15','turkish|sunni|15')
    STATE_KOSOVO = @('albanian|sunni|55','albanian|catholic|5','serb|orthodox|30','turkish|sunni|10')
    STATE_HUDAVENDIGAR = @('turkish|sunni|75','greek|orthodox|15','armenian|oriental_orthodox|10')
    STATE_AYDIN = @('turkish|sunni|70','greek|orthodox|25','armenian|oriental_orthodox|5')
    STATE_KONYA = @('turkish|sunni|90','greek|orthodox|5','kurdish|sunni|5')
    STATE_KASTAMONU = @('turkish|sunni|95','greek|orthodox|5')
    STATE_CYPRUS = @('greek|orthodox|70','turkish|sunni|30')
    STATE_TRABZON = @('turkish|sunni|75','greek|orthodox|15','armenian|oriental_orthodox|5','georgian|orthodox|5')
    STATE_ERZURUM = @('kurdish|sunni|35','kurdish|shiite|5','turkish|sunni|30','armenian|sunni|5','armenian|oriental_orthodox|25')
    STATE_KARS = @('turkish|sunni|40','georgian|orthodox|20','armenian|oriental_orthodox|20','kurdish|sunni|10','greek|orthodox|10')
    STATE_EAST_AEGEAN_ISLANDS = @('greek|orthodox|90','turkish|sunni|10')
    STATE_ANKARA = @('turkish|sunni|70','turkish|shiite|5','armenian|oriental_orthodox|10','kurdish|shiite|10','greek|orthodox|5')
    STATE_DIYARBAKIR = @('kurdish|sunni|45','kurdish|shiite|5','armenian|oriental_orthodox|25','turkish|sunni|15','assyrian|oriental_orthodox|5','mashriqi|sunni|5')
    STATE_ADANA = @('turkish|sunni|90','armenian|oriental_orthodox|5','greek|orthodox|5')
    STATE_DEIR_EZ_ZOR = @('mashriqi|sunni|45','mashriqi|shiite|5','bedouin|sunni|20','kurdish|sunni|15','assyrian|oriental_orthodox|15')
}

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

function Allocate-IntegerShares {
    param([int64]$Total, [object[]]$Items, [scriptblock]$Weight)
    $result = @()
    $floorSum = [int64]0
    for ($i = 0; $i -lt $Items.Count; $i++) {
        $raw = [decimal]$Total * [decimal](& $Weight $Items[$i])
        $floor = [int64][math]::Floor($raw)
        $floorSum += $floor
        $result += [pscustomobject]@{ Index = $i; Value = $floor; Fraction = $raw - $floor }
    }
    $remainder = [int]($Total - $floorSum)
    foreach ($entry in ($result | Sort-Object @{ Expression = 'Fraction'; Descending = $true }, Index | Select-Object -First $remainder)) {
        $entry.Value++
    }
    return @($result | Sort-Object Index)
}

function Get-VanillaPopStats {
    param([string]$TurBlock)
    $total = [int64]0
    $slaves = [int64]0
    foreach ($match in [regex]::Matches($TurBlock, '(?ms)create_pop\s*=\s*\{[^{}]*\}')) {
        $sizeMatch = [regex]::Match($match.Value, 'size\s*=\s*(\d+)')
        if (-not $sizeMatch.Success) { throw 'create_pop block without size' }
        $size = [int64]$sizeMatch.Groups[1].Value
        $total += $size
        if ($match.Value -match 'pop_type\s*=\s*slaves') { $slaves += $size }
    }
    return [pscustomobject]@{ Total = $total; Slaves = $slaves }
}

function New-TurBlock {
    param([string]$State, [int64]$Target, [int64]$VanillaTotal, [int64]$VanillaSlaves)
    $identities = @()
    foreach ($spec in $plans[$State]) {
        $parts = $spec.Split('|')
        $identities += [pscustomobject]@{
            Culture = $parts[0]
            Religion = $parts[1]
            Percentage = [int]$parts[2]
        }
    }
    if (($identities.Percentage | Measure-Object -Sum).Sum -ne 100) { throw "$State identity plan does not sum to 100" }

    $sizes = Allocate-IntegerShares -Total $Target -Items $identities -Weight { param($x) [decimal]$x.Percentage / 100 }
    for ($i = 0; $i -lt $identities.Count; $i++) { $identities[$i] | Add-Member Size $sizes[$i].Value }

    $targetSlaves = [int64][math]::Round(([decimal]$Target * $VanillaSlaves / $VanillaTotal), 0, [MidpointRounding]::AwayFromZero)
    $slaveAlloc = Allocate-IntegerShares -Total $targetSlaves -Items $identities -Weight { param($x) [decimal]$x.Size / $Target }

    $lines = [Collections.Generic.List[string]]::new()
    $lines.Add("`t`tregion_state:TUR = {")
    $lines.Add("`t`t`t# I-01: approved R-02 demographic reconstruction; profession status scaled from vanilla.")
    for ($i = 0; $i -lt $identities.Count; $i++) {
        $identity = $identities[$i]
        $slaveSize = [int64]$slaveAlloc[$i].Value
        $freeSize = [int64]$identity.Size - $slaveSize
        foreach ($row in @(
            [pscustomobject]@{ Size = $freeSize; Slave = $false },
            [pscustomobject]@{ Size = $slaveSize; Slave = $true }
        )) {
            if ($row.Size -le 0) { continue }
            $lines.Add("`t`t`tcreate_pop = {")
            if ($row.Slave) { $lines.Add("`t`t`t`tpop_type = slaves") }
            $lines.Add("`t`t`t`tculture = $($identity.Culture)")
            $lines.Add("`t`t`t`treligion = $($identity.Religion)")
            $lines.Add("`t`t`t`tsize = $($row.Size)")
            $lines.Add("`t`t`t}")
        }
    }
    $lines.Add("`t`t}")
    return $lines -join "`r`n"
}

$proposalRows = @(Import-Csv $populationCsv)
if ($proposalRows.Count -ne 30 -or $plans.Count -ne 30) { throw 'I-01 requires exactly 30 proposal rows and 30 identity plans' }
if ((($proposalRows.proposed_mod_population | ForEach-Object { [int64]$_ }) | Measure-Object -Sum).Sum -ne 19196112) {
    throw 'Approved proposed population does not total 19,196,112'
}

$files = @{}
foreach ($relative in $vanillaFiles) {
    $source = Join-Path $VanillaGameRoot $relative
    if (-not (Test-Path $source)) { throw "Missing vanilla source: $source" }
    $files[$relative] = [IO.File]::ReadAllText($source)
}

$stateResults = @()
foreach ($row in $proposalRows) {
    $state = $row.vic3_state
    if (-not $plans.ContainsKey($state)) { throw "Missing identity plan for $state" }
    $foundIn = @()
    foreach ($relative in $vanillaFiles) {
        $stateBlock = Find-BracedBlock -Text $files[$relative] -SearchStart 0 -Pattern "^\s*s:$state\s*=\s*\{"
        if ($null -ne $stateBlock) { $foundIn += [pscustomobject]@{ Relative = $relative; State = $stateBlock } }
    }
    if ($foundIn.Count -ne 1) { throw "$state found in $($foundIn.Count) vanilla population files" }

    $location = $foundIn[0]
    $stateText = $files[$location.Relative].Substring($location.State.Start, $location.State.End - $location.State.Start + 1)
    $turRelative = Find-BracedBlock -Text $stateText -SearchStart 0 -Pattern '^\s*region_state:TUR\s*=\s*\{'
    if ($null -eq $turRelative) { throw "No TUR region_state block in $state" }
    $turText = $stateText.Substring($turRelative.Start, $turRelative.End - $turRelative.Start + 1)
    $stats = Get-VanillaPopStats $turText
    if ($stats.Total -ne [int64]$row.vanilla_population) {
        throw "$state vanilla total mismatch: file=$($stats.Total), CSV=$($row.vanilla_population)"
    }

    $replacement = New-TurBlock -State $state -Target ([int64]$row.proposed_mod_population) -VanillaTotal $stats.Total -VanillaSlaves $stats.Slaves
    $absoluteStart = $location.State.Start + $turRelative.Start
    $absoluteLength = $turRelative.End - $turRelative.Start + 1
    $files[$location.Relative] = $files[$location.Relative].Remove($absoluteStart, $absoluteLength).Insert($absoluteStart, $replacement)
    $stateResults += [pscustomobject]@{ State = $state; Target = [int64]$row.proposed_mod_population; File = $location.Relative }
}

$utf8NoBom = [Text.UTF8Encoding]::new($false)
foreach ($relative in $vanillaFiles) {
    $destination = Join-Path $modRoot $relative
    [IO.Directory]::CreateDirectory((Split-Path -Parent $destination)) | Out-Null
    [IO.File]::WriteAllText($destination, $files[$relative], $utf8NoBom)
}

$stateResults | Sort-Object State | Format-Table -AutoSize
Write-Output "I-01 generated: $($stateResults.Count)/30 TUR states; total=$((($stateResults.Target) | Measure-Object -Sum).Sum)"
