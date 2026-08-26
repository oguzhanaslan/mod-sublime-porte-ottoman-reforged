#!/usr/bin/env python3
"""I-30 layout normalization — presentation-only pass on sp_campaign_tree.gui."""
from __future__ import annotations

import re
from pathlib import Path

MOD = Path(__file__).resolve().parents[1]
GUI = MOD / "gui" / "sp_campaign_tree.gui"

# Shared card content chrome: icon + label block, vertically centered in button.
def card_row(art_w: int, art_h: int, title_font: str, title_max: int, margins: str) -> str:
    return f"""
			widget = {{
				size = {{ 100% 100% }}
				flowcontainer = {{
					direction = horizontal
					parentanchor = vcenter
					spacing = 8
{margins}
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
						spacing = 2

						textbox = {{
							block "node_title" {{ text = "sp_ct_node_placeholder" }}
							autoresize = yes
							align = left|nobaseline
							default_format = "#header"
							using = {title_font}
							max_width = {title_max}
							elide = right
						}}
						textbox = {{
							block "state_completed" {{ visible = no }}
							text = "sp_ct_state_completed"
							autoresize = yes
							align = left|nobaseline
							using = fontsize_small
							default_format = "#G"
						}}
						textbox = {{
							block "state_active" {{ visible = no }}
							text = "sp_ct_state_active"
							autoresize = yes
							align = left|nobaseline
							using = fontsize_small
							default_format = "#Y"
						}}
						textbox = {{
							block "state_available" {{ visible = no }}
							text = "sp_ct_state_available"
							autoresize = yes
							align = left|nobaseline
							using = fontsize_small
						}}
						textbox = {{
							block "state_locked" {{ visible = no }}
							text = "sp_ct_state_locked"
							autoresize = yes
							align = left|nobaseline
							using = fontsize_small
							default_format = "#I"
						}}
					}}
				}}
			}}
"""


def node_shell(name: str, w: int, h: int, body: str, extras: str = "") -> str:
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
					alpha = 0.45
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
					alpha = 0.88
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
					alpha = 0.72
				}}
			}}
{extras}{body}
		}}
	}}
"""


def types_block() -> str:
    major = node_shell(
        "sp_ct_node_major",
        400,
        72,
        card_row(80, 40, "fontsize_large", 280, "\t\t\t\t\tmargin_left = 12\n\t\t\t\t\tmargin_right = 12"),
    )
    identity = node_shell(
        "sp_ct_node_identity",
        248,
        88,
        card_row(80, 40, "fontsize_medium", 140, "\t\t\t\t\tmargin_left = 10\n\t\t\t\t\tmargin_right = 10"),
        extras="""
			widget = {
				size = { 100% 3 }
				parentanchor = bottom
				background = {
					texture = "gfx/interface/backgrounds/divider_gold.dds"
					spriteType = Corneredstretched
					spriteborder = { 0 0 }
					alpha = 0.9
				}
			}
""",
    )
    grand = node_shell(
        "sp_ct_node_grand",
        680,
        88,
        card_row(96, 48, "fontsize_large", 520, "\t\t\t\t\tmargin_left = 12\n\t\t\t\t\tmargin_right = 12"),
        extras="""
			widget = {
				size = { 100% 3 }
				parentanchor = bottom
				background = {
					texture = "gfx/interface/backgrounds/divider_gold.dds"
					spriteType = Corneredstretched
					spriteborder = { 0 0 }
					alpha = 0.85
				}
			}
""",
    )
    final = node_shell(
        "sp_ct_node_final",
        680,
        96,
        card_row(96, 48, "fontsize_large", 520, "\t\t\t\t\tmargin_left = 12\n\t\t\t\t\tmargin_right = 12"),
        extras="""
			widget = {
				size = { 100% 4 }
				parentanchor = top
				background = {
					texture = "gfx/interface/backgrounds/divider_gold.dds"
					spriteType = Corneredstretched
					spriteborder = { 0 0 }
					alpha = 0.95
				}
			}
			widget = {
				size = { 100% 4 }
				parentanchor = bottom
				background = {
					texture = "gfx/interface/backgrounds/divider_gold.dds"
					spriteType = Corneredstretched
					spriteborder = { 0 0 }
					alpha = 0.95
				}
			}
""",
    )
    stage = node_shell(
        "sp_ct_node_stage",
        160,
        72,
        """
			widget = {
				size = { 100% 100% }
				vbox = {
					parentanchor = vcenter
					spacing = 2
					margin_left = 8
					margin_right = 8

					textbox = {
						block "node_title" { text = "sp_ct_node_placeholder" }
						autoresize = yes
						align = hcenter|nobaseline
						default_format = "#header"
						using = fontsize_small
						max_width = 144
						elide = right
					}
					textbox = {
						block "state_completed" { visible = no }
						text = "sp_ct_state_completed"
						autoresize = yes
						align = hcenter|nobaseline
						using = fontsize_small
						default_format = "#G"
					}
					textbox = {
						block "state_active" { visible = no }
						text = "sp_ct_state_active"
						autoresize = yes
						align = hcenter|nobaseline
						using = fontsize_small
						default_format = "#Y"
					}
					textbox = {
						block "state_available" { visible = no }
						text = "sp_ct_state_available"
						autoresize = yes
						align = hcenter|nobaseline
						using = fontsize_small
					}
					textbox = {
						block "state_locked" { visible = no }
						text = "sp_ct_state_locked"
						autoresize = yes
						align = hcenter|nobaseline
						using = fontsize_small
						default_format = "#I"
					}
				}
			}
""",
    )
    objective = node_shell(
        "sp_ct_node_objective",
        248,
        44,
        card_row(40, 20, "fontsize_small", 168, "\t\t\t\t\tmargin_left = 8\n\t\t\t\t\tmargin_right = 8"),
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
		size = { 4 16 }
		parentanchor = hcenter
		background = {
			texture = "gfx/interface/backgrounds/divider_gold.dds"
			spriteType = Corneredstretched
			spriteborder = { 0 0 }
			alpha = 0.75
		}
	}

	type sp_ct_connector_h = widget {
		size = { 12 4 }
		parentanchor = vcenter
		background = {
			texture = "gfx/interface/backgrounds/divider_gold.dds"
			spriteType = Corneredstretched
			spriteborder = { 0 0 }
			alpha = 0.85
		}
	}

	type sp_ct_branch_fork = widget {
		size = { 808 16 }
		parentanchor = hcenter
		widget = {
			size = { 808 4 }
			parentanchor = center
			background = {
				texture = "gfx/interface/backgrounds/divider_gold.dds"
				spriteType = Corneredstretched
				spriteborder = { 0 0 }
				alpha = 0.95
			}
		}
	}

	type sp_ct_insp_empty = flowcontainer {
		direction = vertical
		parentanchor = center
		spacing = 12
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


ROOT = """widget = {
	name = "sp_campaign_tree_root"
	layer = layer_ingame_menu
	size = { 100% 100% }
	visible = "[GetMetaPlayer.GetPlayedOrObservedCountry.IsValid]"

	# fullscreen_top_header inside sp_campaign_tree_window clears vanilla top HUD;
	# no outer margin_top offset (that strip was redundant dead space).
	sp_campaign_tree_window = {}
}
"""


def patch_inspector(text: str) -> str:
    start = text.index("### SP_CT_INSPECTOR_PANELS_START")
    end = text.index("### SP_CT_INSPECTOR_PANELS_END")
    head = text[:start]
    body = text[start:end]
    tail = text[end:]
    body = body.replace("spacing = 6", "spacing = 12", 1) if "spacing = 6" in body else body
    body = re.sub(r"spacing = 6\n", "spacing = 12\n", body)
    body = re.sub(r"spacing = 3\n", "spacing = 8\n", body)
    body = body.replace("margin_top = 6", "margin_top = 12")
    body = body.replace("margin_top = 8", "margin_top = 16")
    return head + body + tail


def main() -> None:
    text = GUI.read_text(encoding="utf-8")

    # Root shell — remove redundant outer margin_top host
    root_start = text.index('widget = {\n\tname = "sp_campaign_tree_root"')
    root_end = text.index("\n\ntypes sp_campaign_tree_types {", root_start)
    text = text[:root_start] + ROOT.rstrip() + text[root_end:]

    # Window chrome spacing
    text = text.replace("margin = { 20 20 }", "margin = { 16 16 }", 1)
    text = text.replace("margin_top = 76", "margin_top = 72", 1)
    text = text.replace("margin_left = 20", "margin_left = 16", 1)
    text = text.replace("margin_right = 20", "margin_right = 16", 1)
    text = text.replace("margin_bottom = 14", "margin_bottom = 16", 1)
    text = text.replace("\t\t\tspacing = 6\n\n\t\t\twidget = {\n\t\t\t\tsize = { 100% 84 }", "\t\t\tspacing = 8\n\n\t\t\twidget = {\n\t\t\t\tsize = { 100% 68 }", 1)

    # Header controls + branding
    text = text.replace(
        """\t\t\t\tback_button_large = {
\t\t\t\t\tposition = { 8 16 }
\t\t\t\t\tparentanchor = top|left""",
        """\t\t\t\tback_button_large = {
\t\t\t\t\tposition = { 12 0 }
\t\t\t\t\tparentanchor = left|vcenter""",
        1,
    )
    text = text.replace(
        """\t\t\t\tclose_button_large = {
\t\t\t\t\tparentanchor = top|right
\t\t\t\t\tposition = { -8 16 }""",
        """\t\t\t\tclose_button_large = {
\t\t\t\t\tparentanchor = right|vcenter
\t\t\t\t\tposition = { -12 0 }""",
        1,
    )
    text = text.replace(
        """\t\t\t\thbox = {
\t\t\t\t\tparentanchor = center
\t\t\t\t\tspacing = 12
\t\t\t\t\ticon = {
\t\t\t\t\t\tsize = { 48 48 }
\t\t\t\t\t\tparentanchor = vcenter
\t\t\t\t\t\ttexture = "gfx/interface/icons/sp_campaign_tree/sp_ct_sidebar_icon.dds"
\t\t\t\t\t}
\t\t\t\t\ttextbox = {
\t\t\t\t\t\ttext = "sp_ct_window_title"
\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\tparentanchor = vcenter
\t\t\t\t\t\talign = left|nobaseline""",
        """\t\t\t\thbox = {
\t\t\t\t\tparentanchor = hcenter|vcenter
\t\t\t\t\tspacing = 12
\t\t\t\t\ticon = {
\t\t\t\t\t\tsize = { 44 44 }
\t\t\t\t\t\tparentanchor = vcenter
\t\t\t\t\t\ttexture = "gfx/interface/icons/sp_campaign_tree/sp_ct_sidebar_icon.dds"
\t\t\t\t\t}
\t\t\t\t\ttextbox = {
\t\t\t\t\t\ttext = "sp_ct_window_title"
\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\tparentanchor = vcenter
\t\t\t\t\t\talign = left|vcenter|nobaseline""",
        1,
    )

    # Body split
    text = text.replace("\t\t\t\tspacing = 10\n\n\t\t\t\tscrollarea = {", "\t\t\t\tspacing = 12\n\n\t\t\t\tscrollarea = {", 1)
    text = text.replace(
        "\t\t\t\t\tvbox = {\n\t\t\t\t\t\tsize = { 100% 100% }\n\t\t\t\t\t\tmargin = { 6 6 }\n\t\t\t\t\t\tspacing = 4",
        "\t\t\t\t\tvbox = {\n\t\t\t\t\t\tsize = { 100% 100% }\n\t\t\t\t\t\tmargin = { 12 12 }\n\t\t\t\t\t\tspacing = 8",
        1,
    )

    # Tree grid
    text = text.replace("minimumsize = { 1310 -1 }", "minimumsize = { 808 -1 }", 1)
    text = text.replace("spacing = 6\n\t\t\t\t\t\t\tmargin_top = 4", "spacing = 8\n\t\t\t\t\t\t\tmargin_top = 8", 1)
    text = text.replace("margin_bottom = 20", "margin_bottom = 16", 1)
    text = text.replace("spacing = 36", "spacing = 32", 1)
    text = text.replace("minimumsize = { 230 -1 }", "minimumsize = { 248 -1 }", 2)
    text = text.replace("minimumsize = { 740 -1 }", "minimumsize = { 680 -1 }", 1)
    text = text.replace("spacing = 4\n\t\t\t\t\t\t\tsp_ct_node_stage", "spacing = 8\n\t\t\t\t\t\t\tsp_ct_node_stage", 1)

    # Replace node + connector type definitions (major … insp_empty)
    start_marker = "\ttype sp_ct_node_major = widget {"
    idx_start = text.index(start_marker)
    idx_types_close = text.rfind("\n}")
    text = text[:idx_start] + types_block().rstrip() + text[idx_types_close:]

    text = patch_inspector(text)

    if text.count("{") != text.count("}"):
        raise SystemExit(f"Brace mismatch: {{={text.count('{')} }}={text.count('}')}")

    GUI.write_text(text, encoding="utf-8")
    print(f"Patched {GUI} ({len(text.splitlines())} lines)")


if __name__ == "__main__":
    main()
