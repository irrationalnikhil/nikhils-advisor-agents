# Changelog

## 1.0.0 — 24 September 2026

First private team release as native named agents for Claude Code and Codex. The six concise Codex advisor profiles and the September behavioural-design update are the baseline. Hannah's numerical-analysis role is condensed from the existing agent library and added alongside them.

The review used the supplied Phase II AI training transcript and selected recent work logs covering advisor refinement, behavioural design, UI verification, simulation explanation, operational handoffs, and data handling. Only reusable lessons are included here; the source transcript and logs are not distributed.

Small refinements:

- **All agents:** independent action-and-evaluation work, concise evidence returns, reuse of applicable measured facts, clear stopping conditions, and an improvement question every ten work turns with continuation state and parent relay. The cadence was absent from the inspected Codex package; this release adds it explicitly.
- **Jackson and Brendan:** findings tied to reproduction and impact; recheck the formerly broken control after the final change; distinguish successful builds from successful user behaviour.
- **Sylvia:** acceptance criteria include a usable handoff and material delivery effort.
- **Nikhil:** preserve attention + intention + action and COM-B, keep needed information near the action, check promise-to-delivery consistency, and preserve useful visual character.
- **Taichi:** keep observed leaks separate from suspected barriers; choose a test suited to the traffic and decision without invented lift or arbitrary sample thresholds.
- **Hannah:** retain primary-source computation, units and denominators, reproducibility, uncertain identity matches, and data-purpose boundaries.
- **Glyndon:** retain configuration-first domain stewardship and separate simulation assumptions from observed outcomes.

Sharing improvements: a short entry guide, platform-native definitions generated from the same source, a settings-preserving installer with backups, and a ZIP of the repository's tracked contents.

No model is pinned. The package inherits the host's model and permissions; it grants no additional service or account access.
