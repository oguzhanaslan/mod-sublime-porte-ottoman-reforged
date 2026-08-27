#!/usr/bin/env python3
"""Add I-31 capstone tree nodes + inspector panels to sp_campaign_tree.gui."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUI = ROOT / "gui" / "sp_campaign_tree.gui"

OTTOMAN_TREE_ANCHOR = """\t\t\t\t\t\t\tblockoverride "node_icon" {
\t\t\t\t\t\t\t\t\ttexture = "gfx/interface/illustrations/sp_campaign_tree/sp_ct_insp_ottomanism.dds"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t}

\t\t\t\t\t\t\t\tflowcontainer = {
\t\t\t\t\t\t\t\t\tdirection = vertical
\t\t\t\t\t\t\t\t\tspacing = 6
\t\t\t\t\t\t\t\t\tminimumsize = { 230 -1 }
\t\t\t\t\t\t\t\t\tsp_ct_connector_v = {}
\t\t\t\t\t\t\tsp_ct_node_identity = {
\t\t\t\t\t\t\t\tblockoverride "node_onclick" {
\t\t\t\t\t\t\t\t\tonclick = "[GetScriptedGui('sp_ct_select_islamism').Execute(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
"""

OTTOMAN_TREE_INSERT = """\t\t\t\t\t\t\tblockoverride "node_icon" {
\t\t\t\t\t\t\t\t\ttexture = "gfx/interface/illustrations/sp_campaign_tree/sp_ct_insp_ottomanism.dds"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tsp_ct_connector_v = {}
\t\t\t\t\t\t\tsp_ct_node_final = {
\t\t\t\t\t\t\t\tblockoverride "node_onclick" {
\t\t\t\t\t\t\t\t\tonclick = "[GetScriptedGui('sp_ct_select_constitutional_ottoman').Execute(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tblockoverride "node_title" { text = "sp_ct_node_constitutional_ottoman_short" }
\t\t\t\t\t\t\t\tblockoverride "node_tooltip" { tooltip = "sp_ct_tt_constitutional_ottoman" }
\t\t\t\t\t\t\t\tblockoverride "node_selected" {
\t\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_sel_constitutional_ottoman').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tblockoverride "state_completed" {
\t\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_constitutional_ottoman_completed').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tblockoverride "state_active" {
\t\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_constitutional_ottoman_active').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tblockoverride "state_active_glow" {
\t\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_constitutional_ottoman_active').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tblockoverride "state_available" {
\t\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_constitutional_ottoman_available').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tblockoverride "state_locked" {
\t\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_constitutional_ottoman_locked').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tblockoverride "state_locked_dim" {
\t\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_constitutional_ottoman_locked').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tblockoverride "node_icon" {
\t\t\t\t\t\t\t\t\ttexture = "gfx/interface/illustrations/sp_campaign_tree/sp_ct_insp_ottomanism.dds"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t}

\t\t\t\t\t\t\t\tflowcontainer = {
\t\t\t\t\t\t\t\t\tdirection = vertical
\t\t\t\t\t\t\t\t\tspacing = 6
\t\t\t\t\t\t\t\t\tminimumsize = { 230 -1 }
\t\t\t\t\t\t\t\t\tsp_ct_connector_v = {}
\t\t\t\t\t\t\tsp_ct_node_identity = {
\t\t\t\t\t\t\t\tblockoverride "node_onclick" {
\t\t\t\t\t\t\t\t\tonclick = "[GetScriptedGui('sp_ct_select_islamism').Execute(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
"""

ISLAM_TREE_ANCHOR = """\t\t\t\t\t\t\tblockoverride "node_icon" {
\t\t\t\t\t\t\t\t\ttexture = "gfx/interface/illustrations/sp_campaign_tree/sp_ct_insp_islamism.dds"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t}

\t\t\t\t\t\t\t\tflowcontainer = {
\t\t\t\t\t\t\t\t\tdirection = vertical
\t\t\t\t\t\t\t\t\tspacing = 6
\t\t\t\t\t\t\t\t\tminimumsize = { 740 -1 }
\t\t\t\t\t\t\t\t\tsp_ct_connector_v = {}
\t\t\t\t\t\t\tsp_ct_node_identity = {
\t\t\t\t\t\t\t\tblockoverride "node_onclick" {
\t\t\t\t\t\t\t\t\tonclick = "[GetScriptedGui('sp_ct_select_turkism').Execute(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
"""

ISLAM_TREE_INSERT = """\t\t\t\t\t\t\tblockoverride "node_icon" {
\t\t\t\t\t\t\t\t\ttexture = "gfx/interface/illustrations/sp_campaign_tree/sp_ct_insp_islamism.dds"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tsp_ct_connector_v = {}
\t\t\t\t\t\t\tsp_ct_node_final = {
\t\t\t\t\t\t\t\tblockoverride "node_onclick" {
\t\t\t\t\t\t\t\t\tonclick = "[GetScriptedGui('sp_ct_select_great_caliphate').Execute(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tblockoverride "node_title" { text = "sp_ct_node_great_caliphate_short" }
\t\t\t\t\t\t\t\tblockoverride "node_tooltip" { tooltip = "sp_ct_tt_great_caliphate" }
\t\t\t\t\t\t\t\tblockoverride "node_selected" {
\t\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_sel_great_caliphate').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tblockoverride "state_completed" {
\t\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_great_caliphate_completed').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tblockoverride "state_active" {
\t\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_great_caliphate_active').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tblockoverride "state_active_glow" {
\t\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_great_caliphate_active').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tblockoverride "state_available" {
\t\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_great_caliphate_available').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tblockoverride "state_locked" {
\t\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_great_caliphate_locked').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tblockoverride "state_locked_dim" {
\t\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_great_caliphate_locked').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tblockoverride "node_icon" {
\t\t\t\t\t\t\t\t\ttexture = "gfx/interface/illustrations/sp_campaign_tree/sp_ct_insp_islamism.dds"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t}

\t\t\t\t\t\t\t\tflowcontainer = {
\t\t\t\t\t\t\t\t\tdirection = vertical
\t\t\t\t\t\t\t\t\tspacing = 6
\t\t\t\t\t\t\t\t\tminimumsize = { 740 -1 }
\t\t\t\t\t\t\t\t\tsp_ct_connector_v = {}
\t\t\t\t\t\t\tsp_ct_node_identity = {
\t\t\t\t\t\t\t\tblockoverride "node_onclick" {
\t\t\t\t\t\t\t\t\tonclick = "[GetScriptedGui('sp_ct_select_turkism').Execute(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
"""

INSPECTOR_ANCHOR = """\t\t\t\t\t\t\ttext = "sp_ct_insp_islamism_s4_rewards"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tusing = fontsize_small
\t\t\t\t\t\t\t\tmax_width = 500
\t\t\t\t\t\t\t\tmultiline = yes
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\twidget = {
"""

INSPECTOR_INSERT = """\t\t\t\t\t\t\ttext = "sp_ct_insp_islamism_s4_rewards"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tusing = fontsize_small
\t\t\t\t\t\t\t\tmax_width = 500
\t\t\t\t\t\t\t\tmultiline = yes
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\ttextbox = {
\t\t\t\t\t\t\t\ttext = "sp_ct_sec_navigation"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tdefault_format = "#header"
\t\t\t\t\t\t\t\tusing = fontsize_medium
\t\t\t\t\t\t\t\tmargin_top = 6
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\ttextbox = {
\t\t\t\t\t\t\t\ttext = "sp_ct_nav_prev_islamism_s3"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tusing = fontsize_small
\t\t\t\t\t\t\t\tmax_width = 500
\t\t\t\t\t\t\t\tmultiline = yes
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\ttextbox = {
\t\t\t\t\t\t\t\ttext = "sp_ct_nav_next_great_caliphate"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tusing = fontsize_small
\t\t\t\t\t\t\t\tmax_width = 500
\t\t\t\t\t\t\t\tmultiline = yes
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t}

\t\t\t\t\twidget = {
\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_sel_constitutional_ottoman').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\tsize = { 100% -1 }
\t\t\t\t\t\tflowcontainer = {
\t\t\t\t\t\t\tdirection = vertical
\t\t\t\t\t\t\tspacing = 6
\t\t\t\t\t\t\tminimumsize = { 500 -1 }
\t\t\t\t\t\t\twidget = {
\t\t\t\t\t\t\t\tsize = { 520 260 }
\t\t\t\t\t\t\t\tparentanchor = hcenter
\t\t\t\t\t\t\t\tbackground = { using = dark_area alpha = 0.55 }
\t\t\t\t\t\t\t\ticon = {
\t\t\t\t\t\t\t\t\tparentanchor = center
\t\t\t\t\t\t\t\t\tsize = { 520 260 }
\t\t\t\t\t\t\t\t\ttexture = "gfx/interface/illustrations/sp_campaign_tree/sp_ct_insp_ottomanism.dds"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\ttextbox = {
\t\t\t\t\t\t\t\ttext = "sp_ct_node_constitutional_ottoman"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tdefault_format = "#header"
\t\t\t\t\t\t\t\tusing = fontsize_large
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\ttextbox = {
\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_constitutional_ottoman_completed').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\ttext = "sp_ct_state_completed"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tusing = fontsize_medium
\t\t\t\t\t\t\t\tdefault_format = "#G"
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\ttextbox = {
\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_constitutional_ottoman_active').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\ttext = "sp_ct_state_active"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tusing = fontsize_medium
\t\t\t\t\t\t\t\tdefault_format = "#Y"
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\ttextbox = {
\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_constitutional_ottoman_locked').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\ttext = "sp_ct_state_locked"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tusing = fontsize_medium
\t\t\t\t\t\t\t\tdefault_format = "#I"
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_sec_description" autoresize = yes align = left|nobaseline default_format = "#header" using = fontsize_medium margin_top = 6 }
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_insp_constitutional_ottoman_desc" autoresize = yes align = left|nobaseline using = fontsize_small max_width = 500 multiline = yes }
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_sec_flavor" autoresize = yes align = left|nobaseline default_format = "#header" using = fontsize_medium margin_top = 6 }
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_insp_constitutional_ottoman_flavor" autoresize = yes align = left|nobaseline using = fontsize_small max_width = 500 multiline = yes }
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_sec_unlock" autoresize = yes align = left|nobaseline default_format = "#header" using = fontsize_medium margin_top = 6 }
\t\t\t\t\t\t\tflowcontainer = {
\t\t\t\t\t\t\t\tdirection = horizontal
\t\t\t\t\t\t\t\tspacing = 6
\t\t\t\t\t\t\t\tminimumsize = { 500 18 }
\t\t\t\t\t\t\t\ticon = { visible = "[GetScriptedGui('sp_ct_vis_req_ottomanism_s4_done').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]" size = { 16 16 } texture = "gfx/interface/icons/generic_icons/green_checkmark.dds" }
\t\t\t\t\t\t\t\ticon = { visible = "[Not(GetScriptedGui('sp_ct_vis_req_ottomanism_s4_done').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End))]" size = { 16 16 } texture = "gfx/interface/icons/generic_icons/red_cross.dds" }
\t\t\t\t\t\t\t\ttextbox = { text = "sp_ct_req_ottomanism_s4_done" tooltip = "sp_ct_req_ottomanism_s4_done_tt" autoresize = yes align = left|nobaseline using = fontsize_small max_width = 480 multiline = yes }
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_sec_completion" autoresize = yes align = left|nobaseline default_format = "#header" using = fontsize_medium margin_top = 6 }
\t\t\t\t\t\t\tflowcontainer = {
\t\t\t\t\t\t\t\tdirection = horizontal
\t\t\t\t\t\t\t\tspacing = 6
\t\t\t\t\t\t\t\tminimumsize = { 500 18 }
\t\t\t\t\t\t\t\ticon = { visible = "[GetScriptedGui('sp_ct_vis_req_ottomanism_ideal_complete').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]" size = { 16 16 } texture = "gfx/interface/icons/generic_icons/green_checkmark.dds" }
\t\t\t\t\t\t\t\ticon = { visible = "[Not(GetScriptedGui('sp_ct_vis_req_ottomanism_ideal_complete').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End))]" size = { 16 16 } texture = "gfx/interface/icons/generic_icons/red_cross.dds" }
\t\t\t\t\t\t\t\ttextbox = { text = "sp_ct_req_ottomanism_ideal_complete" tooltip = "sp_ct_req_ottomanism_ideal_complete_tt" autoresize = yes align = left|nobaseline using = fontsize_small max_width = 480 multiline = yes }
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_sec_rewards" autoresize = yes align = left|nobaseline default_format = "#header" using = fontsize_medium margin_top = 6 }
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_insp_constitutional_ottoman_rewards" tooltip = "sp_ct_insp_constitutional_ottoman_rewards_tt" autoresize = yes align = left|nobaseline using = fontsize_small max_width = 500 multiline = yes }
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_sec_navigation" autoresize = yes align = left|nobaseline default_format = "#header" using = fontsize_medium margin_top = 6 }
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_nav_prev_ottomanism_s4" autoresize = yes align = left|nobaseline using = fontsize_small max_width = 500 multiline = yes }
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_nav_next_none" autoresize = yes align = left|nobaseline using = fontsize_small max_width = 500 multiline = yes }
\t\t\t\t\t\t}
\t\t\t\t\t}

\t\t\t\t\twidget = {
\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_sel_great_caliphate').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\tsize = { 100% -1 }
\t\t\t\t\t\tflowcontainer = {
\t\t\t\t\t\t\tdirection = vertical
\t\t\t\t\t\t\tspacing = 6
\t\t\t\t\t\t\tminimumsize = { 500 -1 }
\t\t\t\t\t\t\twidget = {
\t\t\t\t\t\t\t\tsize = { 520 260 }
\t\t\t\t\t\t\t\tparentanchor = hcenter
\t\t\t\t\t\t\t\tbackground = { using = dark_area alpha = 0.55 }
\t\t\t\t\t\t\t\ticon = {
\t\t\t\t\t\t\t\t\tparentanchor = center
\t\t\t\t\t\t\t\t\tsize = { 520 260 }
\t\t\t\t\t\t\t\t\ttexture = "gfx/interface/illustrations/sp_campaign_tree/sp_ct_insp_islamism.dds"
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\ttextbox = {
\t\t\t\t\t\t\t\ttext = "sp_ct_node_great_caliphate"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tdefault_format = "#header"
\t\t\t\t\t\t\t\tusing = fontsize_large
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\ttextbox = {
\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_great_caliphate_completed').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\ttext = "sp_ct_state_completed"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tusing = fontsize_medium
\t\t\t\t\t\t\t\tdefault_format = "#G"
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\ttextbox = {
\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_great_caliphate_active').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\ttext = "sp_ct_state_active"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tusing = fontsize_medium
\t\t\t\t\t\t\t\tdefault_format = "#Y"
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\ttextbox = {
\t\t\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_great_caliphate_locked').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
\t\t\t\t\t\t\t\ttext = "sp_ct_state_locked"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tusing = fontsize_medium
\t\t\t\t\t\t\t\tdefault_format = "#I"
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_sec_description" autoresize = yes align = left|nobaseline default_format = "#header" using = fontsize_medium margin_top = 6 }
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_insp_great_caliphate_desc" autoresize = yes align = left|nobaseline using = fontsize_small max_width = 500 multiline = yes }
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_sec_flavor" autoresize = yes align = left|nobaseline default_format = "#header" using = fontsize_medium margin_top = 6 }
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_insp_great_caliphate_flavor" autoresize = yes align = left|nobaseline using = fontsize_small max_width = 500 multiline = yes }
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_sec_unlock" autoresize = yes align = left|nobaseline default_format = "#header" using = fontsize_medium margin_top = 6 }
\t\t\t\t\t\t\tflowcontainer = {
\t\t\t\t\t\t\t\tdirection = horizontal
\t\t\t\t\t\t\t\tspacing = 6
\t\t\t\t\t\t\t\tminimumsize = { 500 18 }
\t\t\t\t\t\t\t\ticon = { visible = "[GetScriptedGui('sp_ct_vis_req_islamism_s4_done').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]" size = { 16 16 } texture = "gfx/interface/icons/generic_icons/green_checkmark.dds" }
\t\t\t\t\t\t\t\ticon = { visible = "[Not(GetScriptedGui('sp_ct_vis_req_islamism_s4_done').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End))]" size = { 16 16 } texture = "gfx/interface/icons/generic_icons/red_cross.dds" }
\t\t\t\t\t\t\t\ttextbox = { text = "sp_ct_req_islamism_s4_done" tooltip = "sp_ct_req_islamism_s4_done_tt" autoresize = yes align = left|nobaseline using = fontsize_small max_width = 480 multiline = yes }
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_sec_completion" autoresize = yes align = left|nobaseline default_format = "#header" using = fontsize_medium margin_top = 6 }
\t\t\t\t\t\t\tflowcontainer = {
\t\t\t\t\t\t\t\tdirection = horizontal
\t\t\t\t\t\t\t\tspacing = 6
\t\t\t\t\t\t\t\tminimumsize = { 500 18 }
\t\t\t\t\t\t\t\ticon = { visible = "[GetScriptedGui('sp_ct_vis_req_great_caliphate_complete').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]" size = { 16 16 } texture = "gfx/interface/icons/generic_icons/green_checkmark.dds" }
\t\t\t\t\t\t\t\ticon = { visible = "[Not(GetScriptedGui('sp_ct_vis_req_great_caliphate_complete').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End))]" size = { 16 16 } texture = "gfx/interface/icons/generic_icons/red_cross.dds" }
\t\t\t\t\t\t\t\ttextbox = { text = "sp_ct_req_great_caliphate_complete" tooltip = "sp_ct_req_great_caliphate_complete_tt" autoresize = yes align = left|nobaseline using = fontsize_small max_width = 480 multiline = yes }
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_sec_rewards" autoresize = yes align = left|nobaseline default_format = "#header" using = fontsize_medium margin_top = 6 }
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_insp_great_caliphate_rewards" tooltip = "sp_ct_insp_great_caliphate_rewards_tt" autoresize = yes align = left|nobaseline using = fontsize_small max_width = 500 multiline = yes }
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_sec_navigation" autoresize = yes align = left|nobaseline default_format = "#header" using = fontsize_medium margin_top = 6 }
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_nav_prev_islamism_s4" autoresize = yes align = left|nobaseline using = fontsize_small max_width = 500 multiline = yes }
\t\t\t\t\t\t\ttextbox = { text = "sp_ct_nav_next_none" autoresize = yes align = left|nobaseline using = fontsize_small max_width = 500 multiline = yes }
\t\t\t\t\t\t}
\t\t\t\t\t}

\t\t\t\t\twidget = {
"""

OTTOMAN_S4_NAV_ANCHOR = """\t\t\t\t\t\t\ttext = "sp_ct_insp_ottomanism_s4_rewards"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tusing = fontsize_small
\t\t\t\t\t\t\t\tmax_width = 500
\t\t\t\t\t\t\t\tmultiline = yes
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t}

\t\t\t\t\twidget = {
\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_sel_islamism_s1').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
"""

OTTOMAN_S4_NAV_INSERT = """\t\t\t\t\t\t\ttext = "sp_ct_insp_ottomanism_s4_rewards"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tusing = fontsize_small
\t\t\t\t\t\t\t\tmax_width = 500
\t\t\t\t\t\t\t\tmultiline = yes
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\ttextbox = {
\t\t\t\t\t\t\t\ttext = "sp_ct_sec_navigation"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tdefault_format = "#header"
\t\t\t\t\t\t\t\tusing = fontsize_medium
\t\t\t\t\t\t\t\tmargin_top = 6
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\ttextbox = {
\t\t\t\t\t\t\t\ttext = "sp_ct_nav_prev_ottomanism_s3"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tusing = fontsize_small
\t\t\t\t\t\t\t\tmax_width = 500
\t\t\t\t\t\t\t\tmultiline = yes
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\ttextbox = {
\t\t\t\t\t\t\t\ttext = "sp_ct_nav_next_constitutional_ottoman"
\t\t\t\t\t\t\t\tautoresize = yes
\t\t\t\t\t\t\t\talign = left|nobaseline
\t\t\t\t\t\t\t\tusing = fontsize_small
\t\t\t\t\t\t\t\tmax_width = 500
\t\t\t\t\t\t\t\tmultiline = yes
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t}

\t\t\t\t\twidget = {
\t\t\t\t\t\tvisible = "[GetScriptedGui('sp_ct_vis_sel_islamism_s1').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End)]"
"""


def replace_once(text: str, anchor: str, insert: str, label: str) -> str:
    if insert.split("\n", 1)[0] in text and label.endswith("tree") and "sp_ct_select_constitutional_ottoman" in text:
        print(f"skip {label}: already patched")
        return text
    if anchor not in text:
        raise SystemExit(f"anchor not found for {label}")
    return text.replace(anchor, insert, 1)


def main() -> None:
    text = GUI.read_text(encoding="utf-8-sig")
    text = replace_once(text, OTTOMAN_TREE_ANCHOR, OTTOMAN_TREE_INSERT, "ottoman tree")
    text = replace_once(text, ISLAM_TREE_ANCHOR, ISLAM_TREE_INSERT, "islam tree")
    text = replace_once(text, OTTOMAN_S4_NAV_ANCHOR, OTTOMAN_S4_NAV_INSERT, "ottoman s4 nav")
    if "sp_ct_vis_sel_constitutional_ottoman" not in text:
        text = replace_once(text, INSPECTOR_ANCHOR, INSPECTOR_INSERT, "inspectors")
    else:
        print("skip inspectors: already patched")
    GUI.write_text(text, encoding="utf-8-sig")
    print("patched", GUI)


if __name__ == "__main__":
    main()
