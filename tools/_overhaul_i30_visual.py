#!/usr/bin/env python3
"""I-30 visual overhaul: rebuild presentation shell/tree/types; splice inspector panels.

Does not touch scripted_gui bindings, selection ints, JE open/pin, or gameplay files.
"""
from __future__ import annotations

from pathlib import Path

MOD = Path(__file__).resolve().parents[1]
GUI = MOD / "gui" / "sp_campaign_tree.gui"
ART = "gfx/interface/illustrations/sp_campaign_tree"
ICON = "gfx/interface/icons/sp_campaign_tree"

SGUI = "GuiScope.SetRoot(GetPlayer.MakeScope).End"


def vis(name: str) -> str:
    return f"[GetScriptedGui('{name}').IsShown({SGUI})]"


def exe(name: str) -> str:
    return f"[GetScriptedGui('{name}').Execute({SGUI})]"


def node(
    typename: str,
    select: str,
    vis_key: str,
    title: str,
    tooltip: str,
    icon: str | None = None,
    has_active: bool = True,
) -> str:
    active = vis(f"sp_ct_vis_{vis_key}_active") if has_active else "no"
    lines = [
        f"\t\t\t\t\t\t\t{typename} = {{",
        f"\t\t\t\t\t\t\t\tblockoverride \"node_onclick\" {{",
        f"\t\t\t\t\t\t\t\t\tonclick = \"{exe(select)}\"",
        f"\t\t\t\t\t\t\t\t}}",
        f"\t\t\t\t\t\t\t\tblockoverride \"node_title\" {{ text = \"{title}\" }}",
        f"\t\t\t\t\t\t\t\tblockoverride \"node_tooltip\" {{ tooltip = \"{tooltip}\" }}",
        f"\t\t\t\t\t\t\t\tblockoverride \"node_selected\" {{",
        f"\t\t\t\t\t\t\t\t\tvisible = \"{vis(f'sp_ct_vis_sel_{vis_key}')}\"",
        f"\t\t\t\t\t\t\t\t}}",
        f"\t\t\t\t\t\t\t\tblockoverride \"state_completed\" {{",
        f"\t\t\t\t\t\t\t\t\tvisible = \"{vis(f'sp_ct_vis_{vis_key}_completed')}\"",
        f"\t\t\t\t\t\t\t\t}}",
        f"\t\t\t\t\t\t\t\tblockoverride \"state_active\" {{",
        f"\t\t\t\t\t\t\t\t\tvisible = \"{active}\"",
        f"\t\t\t\t\t\t\t\t}}",
        f"\t\t\t\t\t\t\t\tblockoverride \"state_active_glow\" {{",
        f"\t\t\t\t\t\t\t\t\tvisible = \"{active}\"",
        f"\t\t\t\t\t\t\t\t}}",
        f"\t\t\t\t\t\t\t\tblockoverride \"state_available\" {{",
        f"\t\t\t\t\t\t\t\t\tvisible = \"{vis(f'sp_ct_vis_{vis_key}_available')}\"",
        f"\t\t\t\t\t\t\t\t}}",
        f"\t\t\t\t\t\t\t\tblockoverride \"state_locked\" {{",
        f"\t\t\t\t\t\t\t\t\tvisible = \"{vis(f'sp_ct_vis_{vis_key}_locked')}\"",
        f"\t\t\t\t\t\t\t\t}}",
        f"\t\t\t\t\t\t\t\tblockoverride \"state_locked_dim\" {{",
        f"\t\t\t\t\t\t\t\t\tvisible = \"{vis(f'sp_ct_vis_{vis_key}_locked')}\"",
        f"\t\t\t\t\t\t\t\t}}",
    ]
    if icon:
        lines.append(f"\t\t\t\t\t\t\t\tblockoverride \"node_icon\" {{")
        lines.append(f"\t\t\t\t\t\t\t\t\ttexture = \"{ART}/sp_ct_insp_{icon}.dds\"")
        lines.append(f"\t\t\t\t\t\t\t\t}}")
    lines.append(f"\t\t\t\t\t\t\t}}")
    return "\n".join(lines)


def chrome(art_w: int, art_h: int, title_font: str, title_max: int, layout: str) -> str:
    """Shared button chrome. layout: 'banner' | 'row' | 'text'."""
    align = "hcenter|nobaseline" if layout in ("text", "banner") else "left|nobaseline"
    if layout == "text":
        return f"""
			vbox = {{
				parentanchor = center
				spacing = 1
				margin_left = 6
				margin_right = 6
{textboxes}
			}}
"""
    if layout == "banner":
        body = f"""
			vbox = {{
				size = {{ 100% 100% }}
				icon = {{
					size = {{ {art_w} {art_h} }}
					parentanchor = hcenter
					block "node_icon" {{
						texture = "gfx/interface/icons/event_icons/event_default.dds"
					}}
				}}
				vbox = {{
					parentanchor = hcenter
					layoutpolicy_horizontal = expanding
					spacing = 1
					margin_left = 8
					margin_right = 8
					margin_top = 2
"""
    else:
        body = f"""
			flowcontainer = {{
				direction = horizontal
				size = {{ 100% 100% }}
				spacing = 8
				margin_left = 10
				margin_right = 8
				icon = {{
					size = {{ {art_w} {art_h} }}
					parentanchor = vcenter
					block "node_icon" {{
						texture = "gfx/interface/icons/event_icons/event_default.dds"
					}}
				}}
				flowcontainer = {{
					direction = vertical
					parentanchor = vcenter
					layoutpolicy_horizontal = expanding
					spacing = 1
"""
    body += f"""
					textbox = {{
						block "node_title" {{ text = "sp_ct_node_placeholder" }}
						autoresize = yes
						align = {align}
						default_format = "#header"
						using = {title_font}
						max_width = {title_max}
						elide = right
					}}
					textbox = {{
						block "state_completed" {{ visible = no }}
						text = "sp_ct_state_completed"
						autoresize = yes
						align = {align}
						using = fontsize_small
						default_format = "#G"
					}}
					textbox = {{
						block "state_active" {{ visible = no }}
						text = "sp_ct_state_active"
						autoresize = yes
						align = {align}
						using = fontsize_small
						default_format = "#Y"
					}}
					textbox = {{
						block "state_available" {{ visible = no }}
						text = "sp_ct_state_available"
						autoresize = yes
						align = {align}
						using = fontsize_small
					}}
					textbox = {{
						block "state_locked" {{ visible = no }}
						text = "sp_ct_state_locked"
						autoresize = yes
						align = {align}
						using = fontsize_small
						default_format = "#I"
					}}
				}}
			}}
"""
    return body


def node_type(name: str, w: int, h: int, art_w: int, art_h: int, title_font: str, title_max: int, layout: str) -> str:
    body = chrome(art_w, art_h, title_font, title_max, layout)
    return f"""
	type {name} = widget {{
		size = {{ {w} {h} }}
		parentanchor = hcenter

		button = {{
			size = {{ 100% 100% }}
			using = default_button_action
			using = confirm_button_sound
			block "node_onclick" {{
				onclick = "[GetPlayer.IsValid]"
			}}
			block "node_tooltip" {{
				tooltip = "sp_ct_node_placeholder_tt"
			}}
			background = {{
				using = default_header_bg
			}}
			widget = {{
				size = {{ 100% 100% }}
				block "state_locked_dim" {{ visible = no }}
				background = {{
					using = dark_area
					alpha = 0.58
				}}
			}}
			widget = {{
				size = {{ 100% 100% }}
				block "state_active_glow" {{ visible = no }}
				background = {{
					texture = "gfx/interface/buttons/default_button_mouseover.dds"
					spriteType = Corneredstretched
					spriteborder = {{ 0 0 }}
					blend_mode = colordodge
					alpha = 0.82
				}}
			}}
			widget = {{
				size = {{ 100% 100% }}
				block "node_selected" {{ visible = no }}
				background = {{
					texture = "gfx/interface/buttons/default_button_mouseover.dds"
					spriteType = Corneredstretched
					spriteborder = {{ 0 0 }}
					blend_mode = colordodge
					alpha = 0.58
				}}
			}}
{body}
		}}
	}}
"""


def types_block() -> str:
    # Stage type: compact vertical, small 2:1 thumb
    stage = node_type(
        "sp_ct_node_stage", 150, 72, 64, 32, "fontsize_small", 138, "text"
    )
    # Objective under identity (I-31 expansion)
    objective = node_type(
        "sp_ct_node_objective", 260, 52, 40, 20, "fontsize_small", 200, "row"
    )
    major = node_type(
        "sp_ct_node_major", 420, 84, 80, 40, "fontsize_large", 300, "row"
    )
    identity = node_type(
        "sp_ct_node_identity", 260, 178, 260, 130, "fontsize_medium", 244, "banner"
    )
    grand = node_type(
        "sp_ct_node_grand", 636, 88, 96, 48, "fontsize_large", 500, "row"
    )
    final = node_type(
        "sp_ct_node_final", 636, 92, 96, 48, "fontsize_large", 500, "row"
    )
    return (
        major
        + identity
        + grand
        + final
        + stage
        + objective
        + """
	type sp_ct_connector_v = widget {
		size = { 4 18 }
		parentanchor = hcenter
		background = {
			texture = "gfx/interface/dividers/divider_clean_vertical.dds"
			spriteType = Corneredstretched
			spriteborder = { 0 0 }
			alpha = 0.85
		}
	}

	type sp_ct_connector_h = widget {
		size = { 12 4 }
		parentanchor = vcenter
		background = {
			texture = "gfx/interface/backgrounds/divider_gold.dds"
			spriteType = Corneredstretched
			spriteborder = { 0 0 }
			alpha = 0.9
		}
	}

	type sp_ct_branch_fork = widget {
		size = { 828 20 }
		parentanchor = hcenter
		icon = {
			size = { 100% 4 }
			parentanchor = center
			texture = "gfx/interface/backgrounds/divider_gold.dds"
			spriteType = Corneredstretched
			spriteborder = { 0 0 }
			alpha = 0.95
		}
	}

	type sp_ct_insp_empty = flowcontainer {
		direction = vertical
		parentanchor = center
		spacing = 10
		widget = {
			size = { 520 260 }
			parentanchor = hcenter
			background = {
				using = dark_area
				alpha = 0.5
			}
			icon = {
				parentanchor = center
				size = { 520 260 }
				texture = "gfx/interface/illustrations/sp_campaign_tree/sp_ct_insp_empty.dds"
			}
		}
		textbox = {
			text = "sp_ct_insp_empty_title"
			autoresize = yes
			align = hcenter|nobaseline
			default_format = "#header"
			using = fontsize_xl
		}
		textbox = {
			text = "sp_ct_insp_empty_desc"
			autoresize = yes
			align = hcenter|nobaseline
			using = fontsize_medium
			max_width = 500
			multiline = yes
		}
	}
"""
    )


def tree_block() -> str:
    tanzimat = node(
        "sp_ct_node_major", "sp_ct_select_tanzimat", "tanzimat",
        "sp_ct_node_tanzimat", "sp_ct_tt_tanzimat", "tanzimat",
    )
    post = node(
        "sp_ct_node_major", "sp_ct_select_post_tanzimat", "post_tanzimat",
        "sp_ct_node_post_tanzimat", "sp_ct_tt_post_tanzimat", "post_tanzimat",
    )
    identity = node(
        "sp_ct_node_major", "sp_ct_select_identity", "identity",
        "sp_ct_node_identity", "sp_ct_tt_identity", "identity",
        has_active=False,
    )
    ott = node(
        "sp_ct_node_identity", "sp_ct_select_ottomanism", "ottomanism",
        "sp_ct_node_ottomanism", "sp_ct_tt_ottomanism", "ottomanism",
    )
    isl = node(
        "sp_ct_node_identity", "sp_ct_select_islamism", "islamism",
        "sp_ct_node_islamism", "sp_ct_tt_islamism", "islamism",
    )
    turk = node(
        "sp_ct_node_identity", "sp_ct_select_turkism", "turkism",
        "sp_ct_node_turkism", "sp_ct_tt_turkism", "turkism",
    )
    turan = node(
        "sp_ct_node_grand", "sp_ct_select_turan", "turan",
        "sp_ct_node_turan", "sp_ct_tt_turan", "turan",
    )
    go = node(
        "sp_ct_node_final", "sp_ct_select_great_ottoman", "great_ottoman",
        "sp_ct_node_great_ottoman_short", "sp_ct_tt_great_ottoman", "great_ottoman",
    )

    def stage(key: str, title: str, icon: str) -> str:
        return node(
            "sp_ct_node_stage", f"sp_ct_select_{key}", key,
            title, f"sp_ct_tt_{key}", icon,
        )

    def obj(key: str, title: str, icon: str) -> str:
        return node(
            "sp_ct_node_objective", f"sp_ct_select_{key}", key,
            title, f"sp_ct_tt_{key}", icon,
        )

    ott_stages = "\n\t\t\t\t\t\t\t\tsp_ct_connector_v = {}\n".join(
        obj(f"ottomanism_s{i}", f"sp_ct_node_ottomanism_s{i}", "ottomanism")
        for i in range(1, 5)
    )
    isl_stages = "\n\t\t\t\t\t\t\t\tsp_ct_connector_v = {}\n".join(
        obj(f"islamism_s{i}", f"sp_ct_node_islamism_s{i}", "islamism")
        for i in range(1, 5)
    )
    turan_stages = "\n\t\t\t\t\t\t\t\t\tsp_ct_connector_h = {}\n".join(
        stage(f"turan_s{i}", f"sp_ct_node_turan_s{i}_short", f"turan_s{i}")
        for i in range(1, 5)
    )

    return f"""
						flowcontainer = {{
							direction = vertical
							parentanchor = top|hcenter
							spacing = 4
							margin_top = 8
							margin_bottom = 28
							minimumsize = {{ 1204 -1 }}

{tanzimat}
							sp_ct_connector_v = {{}}
{post}
							sp_ct_connector_v = {{}}
{identity}
							sp_ct_connector_v = {{}}
							sp_ct_branch_fork = {{}}

							# flowcontainer cannot nest hbox/vbox (engine crash / stack overflow)
							flowcontainer = {{
								direction = horizontal
								parentanchor = top|hcenter
								spacing = 24

								flowcontainer = {{
									direction = vertical
									spacing = 4
									minimumsize = {{ 260 -1 }}
									sp_ct_connector_v = {{}}
{ott}
									sp_ct_connector_v = {{}}
									{ott_stages}
								}}

								flowcontainer = {{
									direction = vertical
									spacing = 4
									minimumsize = {{ 260 -1 }}
									sp_ct_connector_v = {{}}
{isl}
									sp_ct_connector_v = {{}}
									{isl_stages}
								}}

								flowcontainer = {{
									direction = vertical
									spacing = 4
									minimumsize = {{ 636 -1 }}
									sp_ct_connector_v = {{}}
{turk}
									sp_ct_connector_v = {{}}
{turan}
									sp_ct_connector_v = {{}}
									flowcontainer = {{
										direction = horizontal
										parentanchor = hcenter
										spacing = 0
{turan_stages}
									}}
									sp_ct_connector_v = {{}}
{go}
								}}
							}}
						}}
"""


def prefix() -> str:
    return f"""# I-30 Campaign Tree UI — visual overhaul (presentation only).
# Additive scripted widget. No vanilla GUI overwrite.
# Custom near-fullscreen chrome (not InformationPanelBar) so com_open_window /
# com_fullscreen clear reliably on close/back.
# Node classes: major / identity / grand / final / stage / objective.
# Connectors are GUI widgets (vanilla techtree_spline is CPP-backed and unavailable).

@sp_ct_insp_art_w = 520
@sp_ct_insp_art_h = 260

widget = {{
	name = "sp_campaign_tree_root"
	layer = layer_ingame_menu
	size = {{ 100% 100% }}
	visible = "[GetMetaPlayer.GetPlayedOrObservedCountry.IsValid]"

	sp_campaign_tree_window = {{}}
}}

types sp_campaign_tree_types {{

	type sp_campaign_tree_window = widget {{
		name = "sp_campaign_tree_window"
		datacontext = "[AccessPlayer]"
		size = {{ 100% 100% }}
		using = clickthrough_blocker

		visible = "[GetVariableSystem.HasValue('com_open_window', 'gui_sidebar_sp_campaign_tree')]"

		state = {{
			name = _show
			alpha = 1
			duration = 0
			on_start = "[InformationPanelBar.ClosePanel]"
			on_start = "[MapListPanelManager.CloseCurrentPanel]"
			on_finish = "[GetVariableSystem.Set('com_fullscreen', 'com_fullscreen')]"
			start_sound = {{
				soundeffect = "event:/SFX/UI/SideBar/journal"
			}}
		}}
		state = {{
			name = _hide
			alpha = 0
			duration = 0.2
			using = Animation_Curve_Default
			on_finish = "[GetVariableSystem.Clear('com_fullscreen')]"
			start_sound = {{
				soundeffect = "event:/SFX/UI/SideBar/journal_stop"
			}}
		}}

		background = {{
			using = default_bg
			margin = {{ 28 28 }}
		}}

		fullscreen_top_header = {{}}

		widget = {{
			size = {{ 50 100% }}
			parentanchor = left
			background = {{
				using = dark_area
				alpha = 0.5
				mirror = horizontal
				modify_texture = {{
					texture = "gfx/interface/masks/fade_horizontal_left_full.dds"
					spriteType = Corneredstretched
					spriteborder = {{ 0 0 }}
					blend_mode = alphamultiply
				}}
			}}
		}}
		widget = {{
			size = {{ 50 100% }}
			parentanchor = right
			background = {{
				using = dark_area
				alpha = 0.5
				modify_texture = {{
					texture = "gfx/interface/masks/fade_horizontal_left_full.dds"
					spriteType = Corneredstretched
					spriteborder = {{ 0 0 }}
					blend_mode = alphamultiply
				}}
			}}
		}}

		vbox = {{
			using = clickthrough_blocker
			margin_top = 88
			margin_left = 28
			margin_right = 28
			margin_bottom = 20
			layoutpolicy_vertical = expanding
			layoutpolicy_horizontal = expanding
			spacing = 8

			widget = {{
				size = {{ 100% 108 }}
				layoutpolicy_horizontal = expanding
				background = {{
					texture = "{ICON}/sp_ct_header_logo.dds"
					spriteType = Corneredstretched
					spriteborder = {{ 120 0 }}
				}}
				background = {{
					using = dark_area
					alpha = 0.28
				}}
				icon = {{
					size = {{ 100% 4 }}
					parentanchor = bottom
					texture = "gfx/interface/backgrounds/divider_gold.dds"
					spriteType = Corneredstretched
					spriteborder = {{ 0 0 }}
				}}

				back_button_large = {{
					position = {{ 8 24 }}
					parentanchor = top|left
					onclick = "[GetVariableSystem.Clear('com_open_window')]"
					onclick = "[GetVariableSystem.Clear('com_fullscreen')]"
					input_action = "back"
				}}

				close_button_large = {{
					parentanchor = top|right
					position = {{ -8 24 }}
					onclick = "[GetVariableSystem.Clear('com_open_window')]"
					onclick = "[GetVariableSystem.Clear('com_fullscreen')]"
					shortcut = "close_window"
				}}

				hbox = {{
					parentanchor = center
					spacing = 14
					icon = {{
						size = {{ 56 56 }}
						parentanchor = vcenter
						texture = "{ICON}/sp_ct_sidebar_icon.dds"
					}}
					textbox = {{
						text = "sp_ct_window_title"
						autoresize = yes
						align = left|vcenter|nobaseline
						default_format = "#header"
						using = header_font_fancy
						using = header_font_fancy_size
					}}
				}}
			}}

			hbox = {{
				layoutpolicy_vertical = expanding
				layoutpolicy_horizontal = expanding
				spacing = 12

				scrollarea = {{
					size = {{ 67% 100% }}
					layoutpolicy_vertical = expanding
					scrollbarpolicy_horizontal = as_needed
					scrollbar_horizontal = {{ using = horizontal_scrollbar }}
					scrollbar_vertical = {{ using = vertical_scrollbar }}

					scrollwidget = {{
{tree_block()}
					}}
				}}

				widget = {{
					size = {{ 33% 100% }}
					layoutpolicy_vertical = expanding
					background = {{
						using = dark_area
						alpha = 0.42
						margin = {{ 2 2 }}
					}}

					vbox = {{
						size = {{ 100% 100% }}
						margin = {{ 10 10 }}
						spacing = 6

						scrollarea = {{
							layoutpolicy_vertical = expanding
							layoutpolicy_horizontal = expanding
							scrollbar_vertical = {{ using = vertical_scrollbar }}

							scrollwidget = {{
								flowcontainer = {{
									direction = vertical
									spacing = 4
									minimumsize = {{ 500 -1 }}

									sp_ct_insp_empty = {{
										visible = "[Not({vis('sp_ct_vis_has_selection')})]"
									}}

									### SP_CT_INSPECTOR_PANELS_START
"""


def suffix() -> str:
    return f"""
					### SP_CT_INSPECTOR_PANELS_END
								}}
							}}
						}}
					}}
				}}
			}}
		}}
	}}
{types_block()}
}}
"""


def patch_inspector(raw: str) -> str:
    text = raw
    text = text.replace("size = { 380 190 }", "size = { 520 260 }")
    text = text.replace("minimumsize = { 400 -1 }", "minimumsize = { 500 -1 }")
    text = text.replace("minimumsize = { 400 18 }", "minimumsize = { 500 18 }")
    text = text.replace("minimumsize = { 356 -1 }", "minimumsize = { 500 -1 }")
    text = text.replace("max_width = 380", "max_width = 500")
    text = text.replace("max_width = 360", "max_width = 480")
    return text


def main() -> None:
    src = GUI.read_text(encoding="utf-8-sig")
    start = src.index("### SP_CT_INSPECTOR_PANELS_START") + len("### SP_CT_INSPECTOR_PANELS_START")
    end = src.index("### SP_CT_INSPECTOR_PANELS_END")
    panels = src[start:end]
    # Drop the marker line leftovers; keep widget bodies
    panels = patch_inspector(panels)
    out = prefix() + panels + suffix()
    # Remove accidental space-prefixed typos from authoring
    GUI.write_text(out, encoding="utf-8-sig")
    print(f"Wrote {GUI} ({len(out)} chars)")


if __name__ == "__main__":
    main()
