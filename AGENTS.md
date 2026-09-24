# Maintaining this agent package

The maintained sources are `agents/*.md` and `shared/working-rules.md`. Generate both native formats with `python3 scripts/build.py`. Preserve their parity and keep individual roles focused.

For changes, inspect the relevant source, make the smallest justified edit, and run the build check plus packaging tests. Test a meaningful behavioural scenario when an edit changes decisions, rather than matching the wording of instructions. Report simulated checks separately from native host execution. Do not claim ten-turn prompting is enforced by a runtime hook.

Keep raw logs, transcripts, client material, credentials, local feedback, and user-specific settings out of the repository and ZIP. Record only general lessons in the changelog. Do not add model pins or extra access requirements without a reason.

When acting as the parent for an explicitly requested advisor, delegate to the named native agent. Give it the task, relevant evidence, constraints, and a defined output. Return its evidence faithfully, relay any due improvement question once, and carry its `advisor_state` into a continuation. Avoid overlapping writes and panels assembled just to agree.
