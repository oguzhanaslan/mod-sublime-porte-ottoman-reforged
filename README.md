# Sublime Porte: Ottoman Reforged

A Victoria 3 overhaul and flavor project focused on making the Ottoman Empire more historical, deeper, balanced, and engaging from 1836 through the late game.

## Project goals

The project aims to create a distinct Ottoman campaign across economics, demographics, politics, reform, diplomacy, warfare, migration, centralization, and historical development. The goal is not to make the Ottoman Empire overpowered: success should require reform, investment, political struggle, diplomacy, time, and opportunity cost.

## Compatibility

- Supported Victoria 3 version: `1.13.11`
- Required dependency: Community Mod Framework `1.*`
- CMF reference baseline: `1.59.2` (released 31 July 2026)
- Development status: I-01 through I-14 gameplay is implemented on Victoria 3 `1.13.11`; runtime validation remains pending. I-15 is not started.
- Project namespace: `sp_`
- Supported localization: English and Turkish

Community Mod Framework is declared as a dependency, but individual systems should use it only when a verified CMF extension point provides a concrete benefit. Features that can be implemented cleanly with standard Victoria 3 script should remain vanilla-script implementations.

Authoritative CMF source: [Victoria-3-Modding-Co-op/Community-Mod-Framework](https://github.com/Victoria-3-Modding-Co-op/Community-Mod-Framework).

## Development principles

- Vanilla game files are read-only references and are never modified.
- Study a working vanilla or CMF pattern before implementing a feature; never invent script syntax.
- Prefer additive files and narrow changes over broad vanilla overrides.
- Keep player-facing text in localization files; never hardcode it in script.
- Treat English as the source language and provide a synchronized Turkish translation for every released player-facing string.
- Use `sp_` for custom IDs and localization keys wherever possible.
- Treat compatibility, maintainability, historical sourcing, and balanced trade-offs as first-class requirements.
- Mark uncertain historical material as `ASSUMPTION` until verified.
- Develop each logical gameplay feature as a separate Git commit and require Tiger validation before completion.

Contributor rules and the approval workflow are defined in [AGENTS.md](AGENTS.md). Technical boundaries are documented in [ARCHITECTURE.md](ARCHITECTURE.md).
