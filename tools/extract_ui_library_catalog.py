#!/usr/bin/env python3
"""Extract Victoria 3 UI Library catalog from vanilla window_component_library.gui."""
from __future__ import annotations

import re
from pathlib import Path

VANILLA = Path(
    r"C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game\gui\window_component_library.gui"
)
OUT = Path(__file__).resolve().parents[1] / "docs" / "development" / "VIC3_UI_LIBRARY.md"


def field(text: str, name: str) -> str:
    m = re.search(
        rf'blockoverride "{name}" \{{\s*raw_text = "((?:[^"\\]|\\.)*)"',
        text,
        re.DOTALL,
    )
    return m.group(1).replace("\\n", " ").strip() if m else ""


def main() -> None:
    text = VANILLA.read_text(encoding="utf-8")

    # Split on ui_guide_component_area blocks (greedy to closing brace at same indent)
    parts = text.split("ui_guide_component_area = {")
    components: list[dict[str, str]] = []
    for part in parts[1:]:
        chunk = part.split("\n\t\t\t\t\t\t\tui_guide_component_area")[0]
        chunk = chunk.split("\n\t\t\t\t\t\tui_guide_component_area")[0]
        name = field(chunk, "component_name")
        if not name:
            continue
        components.append(
            {
                "name": name,
                "kind": field(chunk, "component_name_type"),
                "desc": field(chunk, "component_desc"),
                "impl": field(chunk, "component_implementation_note"),
                "warn": field(chunk, "component_warning_note"),
            }
        )

    # Inline button/template listings (name + (template) pattern)
    inline: list[tuple[str, str, str]] = []
    for m in re.finditer(
        r'raw_text = "([^"]+)"\s*\n\s*\}\s*\n\s*textbox = \{\s*\n\s*autoresize = yes\s*\n\s*raw_text = "\((template|type|dds|bink video file)\)"',
        text,
    ):
        inline.append((m.group(1), m.group(2), ""))

    for m in re.finditer(
        r'raw_text = "([^"]+)"\s*\n\s*\}\s*\n\s*textbox = \{\s*\n\s*autoresize = yes\s*\n\s*align = left\|nobaseline\s*\n\s*raw_text = "([^"]{8,})"',
        text,
    ):
        if m.group(1) not in {c["name"] for c in components}:
            inline.append((m.group(1), "note", m.group(2)[:120]))

    lines = [
        "# Victoria 3 UI Library — Component Catalog",
        "",
        "**Audience:** Sublime Porte mod developers and AI agents.",
        "**Source:** Installed Victoria 3 `1.13.11` vanilla `game/gui/window_component_library.gui`.",
        "**Status:** Extracted from in-game UI Library (Paradox internal style guide). Not player documentation.",
        "",
        "The UI Library is an **in-game catalog**, not a moddable API. Mods reference the same vanilla",
        "`template` / `type` names via `using = …` in `.gui` files.",
        "",
        "> **Web docs:** Paradox does not publish UI Library as a standalone wiki page. This file is the",
        "> project-local mirror of the in-game catalog. Re-run `tools/extract_ui_library_catalog.py` after",
        "> Vic3 patches if components change.",
        "",
        "---",
        "",
        "## How to open (debug mode)",
        "",
        "1. Steam launch options: `-debug_mode`",
        "2. In-game console (`~` / `` ` `` depending on keyboard layout)",
        "3. Either:",
        "   - Debug menu → **Master Menu → Tools → UI Library**",
        "   - Console button: **UI Library**",
        "   - Console command:",
        "     `GUI.CreateWidget gui/window_component_library.gui component_library_window`",
        "",
        "### Related debug tools",
        "",
        "| Tool | How to open | Purpose |",
        "|---|---|---|",
        "| **UI Library** | Tools menu / command above | Live component catalog + descriptions |",
        "| **GUI Editor** | `gui_editor` or Ctrl+F8 | In-game layout edit (**save can corrupt files**) |",
        "| **GUI Debug** | `gui.debug` | Hover tooltip shows `.gui` file + line |",
        "| **Data Types** | `data_types_explorer` | GUI script functions per datatype |",
        "| **Script Explorer** | `explorer` | Game script inspection |",
        "| **Reload GUI** | `reload gui` | Hot-reload `.gui` in debug mode |",
        "| **Reload textures** | `reload texture` | Hot-reload DDS |",
        "",
        "Wiki cross-refs (general GUI, not UI Library-specific):",
        "",
        "- [Interface modding](https://vic3.paradoxwikis.com/Interface_modding)",
        "- [GUI script](https://vic3.paradoxwikis.com/GUI_script)",
        "- [Scripted GUI](https://vic3.paradoxwikis.com/Scripted_gui)",
        "- [Console commands](https://vic3.paradoxwikis.com/Console)",
        "",
        "---",
        "",
        "## UI Library structure",
        "",
        "### Top tabs",
        "",
        "| Tab | Status | Notes |",
        "|---|---|---|",
        "| **UI Components** | Complete | Primary modder reference |",
        "| **UI Art Guide** | Stub | Paradox-internal placeholders (Swedish notes) |",
        "| **UX Guide** | Stub | Paradox-internal placeholders |",
        "",
        "### UI Components sub-tabs",
        "",
        "| Sub-tab | Typical `using =` / types |",
        "|---|---|",
        "| Buttons | `default_button`, `default_button_action`, icon buttons, `button_tab`, `check_button` |",
        "| Backgrounds | `default_bg`, `default_background`, `dark_area`, `entry_bg_simple`, `entry_bg_fancy` |",
        "| Headers | `default_header_bg`, `default_header_bg_faded`, `top_header_bg`, `sidepanel_top_header` |",
        "| Frames | `popup_bg_frame`, `frame_small`, `simple_frame`, `side_frame.dds` |",
        "| Dividers | `divider_gold`, standard dividers |",
        "| Progressbars | Journal / timed bar widgets |",
        "| Icons | Domain icons under `gfx/interface/icons/` |",
        "| Text | `fontsize_small`, `fontsize_medium`, `header_font_fancy`, format codes |",
        "| Characters | Requires active game session |",
        "| Flags | Requires active game session |",
        "| Animations | `Animation_FadeIn_*`, `Animation_ShowHide_*`, state blocks |",
        "",
        "---",
        "",
        "## How to use in mods",
        "",
        "```gui",
        "background = { using = default_header_bg }",
        "background = { using = dark_area alpha = 0.45 }",
        "button = { using = default_button_action }",
        "widget = {",
        "    background = { using = entry_bg_simple }",
        "}",
        "```",
        "",
        "**Workflow:**",
        "",
        "1. Open UI Library in debug mode → find component + read description.",
        "2. Grep installed `Victoria 3/game/gui/` for `using = component_name`.",
        "3. Copy the **structural pattern** from a working vanilla panel.",
        "4. Apply in mod `.gui` with `sp_` loc keys and scripted GUI bindings.",
        "",
        "**Do not:**",
        "",
        "- Ship or `CreateWidget` `window_component_library.gui` in mod UI.",
        "- Save mod files from GUI Editor without review (corruption reports on forum).",
        "- Guess widget syntax not shown in vanilla or UI Library.",
        "",
        "---",
        "",
        "## I-30 Campaign Tree — recommended components",
        "",
        "| UI need | Component | Kind | Vanilla grep target |",
        "|---|---|---|---|",
        "| Node card shell | `default_header_bg` | template | `game/gui/shared/*.gui`, journal panels |",
        "| Faded panel | `default_header_bg_faded` | template | inspector-style panels |",
        "| Inner depth overlay | `dark_area` | template | widespread |",
        "| Gold line | `gfx/interface/backgrounds/divider_gold.dds` | texture | connectors, section breaks |",
        "| Inspector row card | `entry_bg_simple` | template | list rows, journal req lines |",
        "| Fancy row | `entry_bg_fancy` | template | highlighted entries |",
        "| Section header | `section_header_button` | type | expandable journal sections |",
        "| Small card frame | `simple_frame` + `simple_frame_mask` | template pair | compact framed content |",
        "| Node click | `default_button_action` | template | all interactive cards |",
        "| Window title font | `header_font_fancy` | template | fullscreen headers |",
        "| Progress display | progressbar types (see catalog) | type | journal entries |",
        "",
        "---",
        "",
        f"## Component catalog — `ui_guide_component_area` ({len(components)} entries)",
        "",
    ]

    for comp in components:
        lines.append(f"### `{comp['name']}`")
        if comp["kind"]:
            lines.append(f"- **Kind:** {comp['kind']}")
        if comp["desc"]:
            lines.append(f"- **Description:** {comp['desc']}")
        if comp["impl"]:
            lines.append(f"- **Implementation:** {comp['impl']}")
        if comp["warn"]:
            lines.append(f"- **Warning:** {comp['warn']}")
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            "## Buttons — inline catalog entries",
            "",
            "These appear as labeled examples in the Buttons tab (may overlap with catalog above).",
            "",
            "### Navigational buttons (no game state change)",
            "",
            "| Name | Kind | UI Library note |",
            "|---|---|---|",
            "| `default_button` | template | Most common button; lists and general use |",
            "| `default_button_primary` | template | Primary navigation option |",
            "| `default_button_primary_big` | template | Primary nav when height ≥ 50px |",
            "",
            "### Action buttons (change game state)",
            "",
            "| Name | Kind | UI Library note |",
            "|---|---|---|",
            "| `default_button_action` | template | Default action button |",
            "| `default_button_primary_action` | template | Primary action |",
            "| `default_button_primary_big_action` | template | Primary action, height ≥ 50px |",
            "| `default_button_map_interaction` | template | Map 2-click delayed action |",
            "",
            "### Icon button base types",
            "",
            "| Name | Kind |",
            "|---|---|",
            "| `button_icon_round` | type |",
            "| `button_icon_round_action` | type |",
            "| `button_icon_round_map_interaction` | type |",
            "| `button_icon_round_big` | type |",
            "| `button_icon_round_big_action` | type |",
            "| `button_icon_square` | type |",
            "| `button_icon_square_action` | type |",
            "",
            "> Use `blockoverride` for icon texture and `icon_size`. Round is default shape.",
            "",
            "### View controls",
            "",
            "| Name | Kind | Use |",
            "|---|---|---|",
            "| `button_tab` | type | Window tabs |",
            "| `sort_button` | type | Sortable columns |",
            "| `section_header_button` | type | Expandable section headers |",
            "| `expand_button_bg` | template | Expand control without arrow+title |",
            "| `scrollbox` | type | Vertical scroll lists |",
            "| `checkbutton` / `check_button` | type/template | Multi-select lists |",
            "",
            "---",
            "",
            "## Backgrounds — key templates",
            "",
            "| Name | Kind | Use |",
            "|---|---|---|",
            "| `default_bg` | template | Sidepanels and fullscreen UI base |",
            "| `default_background` | template | Popups, HUD, context menus |",
            "| `dark_area` | template | Dim overlay / inner panel depth |",
            "| `entry_bg_simple` | template | Simple list row background |",
            "| `entry_bg_fancy` | template | Decorative row background |",
            "| `entry_bg_simple_colored` | template | Tinted row background |",
            "",
            "> When placing frames on top, use the matching **mask template** so background shape follows frame.",
            "",
            "---",
            "",
            "## Headers — key templates",
            "",
            "| Name | Kind | Use |",
            "|---|---|---|",
            "| `header_color` | template | Base color for all headers |",
            "| `header_graphical_properties` | template | Header texture/modify_texture tweaks |",
            "| `top_header_bg` | template | Main window top headers (side/fullscreen/popup) |",
            "| `sidepanel_top_header` | template | Sidepanel frame + mask combo |",
            "| `default_header_bg` | template | Standard in-panel header strip |",
            "| `default_header_bg_faded` | template | Subtle header / secondary panel |",
            "",
            "---",
            "",
            "## Frames — key types/templates",
            "",
            "| Name | Kind | Use |",
            "|---|---|---|",
            "| `popup_bg_frame` | type | Floating popup windows |",
            "| `popup_bg_frame_frontend` | type | Frontend flow popups |",
            "| `frame_small` + `frame_small_mask` | template pair | Small decorative frame |",
            "| `simple_frame` + `simple_frame_mask` | template pair | Clean compact frame |",
            "| `side_frame.dds` | texture | Sidepanel vertical borders |",
            "",
            "---",
            "",
            "## UX rules from UI Library (Buttons tab notes)",
            "",
            "- **Navigational** vs **Action** button families are distinct — pick the correct template.",
            "- **Icon buttons:** default shape is **round**; square is rare.",
            "- **Horizontal scroll:** UI Library says aim to **never** use it.",
            "- **Big** icon/button variants: use when control height ≥ 50–60px.",
            "- **Checkboxes:** use `check_button` template inside `checkbutton` type.",
            "",
            "---",
            "",
            "## Related project docs",
            "",
            "- [PARADOX_GUI_GUIDE.md](./PARADOX_GUI_GUIDE.md) — layout rules, CMF hooks, I-30 regression baseline",
            "- [AGENTS.md](../../AGENTS.md) — GUI hard rules for agents",
            "",
            "---",
            "",
            f"*Catalog entries: {len(components)} from `ui_guide_component_area`. Generated by `tools/extract_ui_library_catalog.py`.*",
            "",
        ]
    )

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(components)} components to {OUT}")


if __name__ == "__main__":
    main()
