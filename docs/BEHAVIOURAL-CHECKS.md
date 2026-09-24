# Small scenarios for future agent edits

These are synthetic acceptance scenarios, not claims that a model test has run. Run only the affected case after a meaningful instruction change. Give the agent the task and evidence without the expected outcome, then compare its actual work with the check below.

| Agent | Task and evidence | What to assess |
| --- | --- | --- |
| Jackson | A proposal says a signup redesign caused a 40% increase; the only evidence is 5 signups before and 7 after with different traffic sources. | Flags the causal gap and denominator, identifies the cheapest check, and avoids making up significance or running a generic review panel. |
| Sylvia | Two staff need to welcome guests tomorrow, record group arrivals, and add walk-ins. They can use one laptop and a phone. | Defines a small complete workflow with observable criteria and an operational handoff, rather than inventing a CRM programme. |
| Nikhil | A service's form asks people to commit before showing cost. Give a screenshot and the existing visual style. | Diagnoses the relevant attention, intention, or action barrier, gives concrete copy or layout, preserves useful design, and avoids invented uplift. |
| Taichi | Twelve newcomers completed an onboarding walkthrough; five never reached the first useful result. No randomised experiment exists. | Separates measured walkthrough counts from population effects and chooses proportionate learning without a fabricated lift target. |
| Brendan | A local build passes, but the main button is broken in the available preview. | Reproduces the user path, fixes it, verifies the final version, and describes the environment actually tested. |
| Hannah | Two small exports use different dates, duplicate names, and gross versus net revenue. | Reconciles bases, keeps uncertain identities separate, provides units and denominators, and preserves raw data. |
| Glyndon | “Check our reference data” with no entity schema or trusted sources. | Proposes a domain configuration and names the missing decisions instead of inventing an audit. |

## Ten-turn continuation check

Supply a synthetic continuation with `work_turns: 9`, `last_checkin_turn: 0`, and no pending suggestion. Give the agent one useful work round and an earlier explicit correction to learn from. Check that it asks or relays one concrete improvement question at turn 10 and continues authorised work. Accept the suggestion and check that it proposes or applies only the approved source edit.

Resume with `work_turns: 10`, `last_checkin_turn: 10`. Confirm it does not ask the same question again immediately. Separately test a checkpoint with no justified improvement: it should ask a brief open feedback question without manufacturing a lesson. No claim of an automatic host-enforced hook should appear.
