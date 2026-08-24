# Technical Architecture

## Reference model

The installed Victoria 3 `game/` directory is a read-only source of working patterns, scopes, effects, triggers, folder conventions, and localization usage. No project workflow may write to vanilla files. CMF source is likewise read-only and must be inspected before using an extension point.

## Additive-first strategy

New content should live in feature-scoped mod files and merge additively with vanilla. Direct overrides are reserved for cases where the engine exposes no additive route. `replace_path` is a last resort because it increases patch and mod compatibility risk. Every unavoidable override must be narrow and documented.

## Namespace and file organization

Custom identifiers use `sp_` wherever the engine permits. Files should be grouped by feature rather than accumulated into global monoliths. Event IDs, journal entries, decisions, modifiers, scripted triggers, scripted effects, scripted values, and localization keys must follow predictable `sp_<feature>_<purpose>` naming.

## Localization

English is the source and primary development language under `localization/english/`. Turkish is a required supported language under `localization/turkish/`. Both languages use identical key sets and must be updated together for every player-facing feature. Script contains localization keys rather than player-facing prose. Other languages may be added later after the English and Turkish texts stabilize.

## Script domains

- **Events:** feature-scoped files, systematic `sp_` IDs, localized titles/descriptions/options, and explicit triggering paths.
- **Journal entries:** additive definitions where possible, with presentation and reusable logic separated from progression rules.
- **Decisions:** narrowly scoped eligibility and effects, avoiding duplicated JE or event logic.
- **Scripted triggers/effects/values:** shared only when logic is genuinely reused; names describe scope and intent.
- **Modifiers:** custom `sp_` keys with documented duration, stacking, and balance rationale.
- **Characters and companies:** additive definitions backed by verified historical research and vanilla creation patterns.
- **State/history changes:** highest-risk changes because of direct-file conflicts; use only after auditing vanilla ownership and compatibility options.

## CMF integration

CMF is a declared dependency, but not a default implementation layer. The authoritative source is the `Victoria-3-Modding-Co-op/Community-Mod-Framework` repository. Use a CMF hook only after verifying its current API there and demonstrating that it supplies an extension point or compatibility benefit that vanilla script cannot cleanly provide. Keep CMF-coupled code isolated by feature and document the dependency reason.

## Compatibility

Compatibility is protected through additive files, narrow scopes, unique keys, minimal overrides, and documented load-order assumptions. Before changing a vanilla-owned file, audit likely conflicts with CMF and major reference mods.

## Validation

Validation is layered:

1. Parse and metadata checks for JSON, descriptors, encoding, and balanced braces.
2. Repository checks for duplicate `sp_` definitions, missing English localization, and namespace violations.
3. Tiger (`vic3-tiger`) as a required gameplay validation gate for syntax, scopes, references, definitions, and localization.
4. Victoria 3 debug-mode logs and an isolated test playset for runtime validation.
5. Diff review to confirm vanilla and CMF sources remain untouched.

Repository checks should stay small until real content justifies automation; avoid building a bespoke validator prematurely.

Git history is part of the safety model. Each feature is implemented and validated as a separate focused commit so risky population, history, state, and balance changes remain reviewable and reversible.
