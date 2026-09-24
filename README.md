# Nikhil's Advisor Agents

Nikhil's personal collection of seven named agents that can take on work independently, use the tools available in your project, and return evidence and a recommendation. Adapted from his working advisor team, with the concise Codex versions as the starting point.

**New here? Open [START HERE.md](START%20HERE.md).** The ZIP contains the same files as this repository, including the native agent definitions for **Claude Code** and **Codex**.

| Agent | Give them this kind of work |
| --- | --- |
| **Jackson** | Pressure-test a plan, strategy, or technical decision. |
| **Sylvia** | Find the smallest useful product slice and define success. |
| **Nikhil** | Improve behaviour across a website, funnel, message, or service. |
| **Taichi** | Get new users to first value and an early return. |
| **Brendan** | Build or fix something and verify the important behaviour. |
| **Hannah** | Work out what the numbers actually say. |
| **Glyndon** | Check domain facts, reference records, coordinates, or calibration. |

Try: **“Delegate a review of this onboarding flow to the Nikhil agent. Give him the current flow and our goal, then bring me his recommendation.”**

The agents inherit your selected model and available permissions. Each has its own instructions and runs as a delegated worker when your AI tool supports custom agents. You do not need Nikhil's accounts or connectors. Agent names are memorable roles, not claims that the actual people are participating.

## Install

Opening this folder as a project in Claude Code or Codex makes the included project agent definitions available to compatible versions. Start a new session and ask it to delegate to a named agent. To add the agents to another project or all your projects, follow [INSTALL.md](INSTALL.md).

For a colleague who prefers plain language, attach the ZIP in a tool that can read archives and local files, then paste:

> Read START HERE.md and INSTALL.md in this archive. Install these as named agents for this project in the AI tool I am using. Preserve my existing settings and any custom agents. Verify that the seven agents are available, then help me try one on my work. If this chat cannot install or run custom agents, tell me the supported place to use the files; do not claim installation succeeded.

Uploading a ZIP to an ordinary chat supplies files; it does not by itself register native agents. The receiving tool needs custom-agent and filesystem support. The same role instructions can be read in a chat, but that alone does not create independent workers.

## Improving the team

Every agent is instructed to ask for one small improvement **every 10 work turns**. It reviews its own recent work, suggests a specific change when justified, and continues the task while waiting for optional feedback. The parent relays the question if a worker cannot address you directly. The counter travels with a task's handoff; it is separate for each agent.

This is an instruction-based cadence, not a background service or a guaranteed host-level trigger. Full counting, resume, and change-approval rules are in [shared/working-rules.md](shared/working-rules.md). Nothing rewrites the agents silently.

## Maintain

Edit the role in `agents/` or the shared agreement in `shared/working-rules.md`, then rebuild the native files:

```sh
python3 scripts/build.py
python3 scripts/build.py --check
python3 -m unittest discover -s tests -v
```

Python 3.11 or newer is needed only for these helper scripts. No extra Python packages are required. The agent definitions themselves do not require Python.

- `agents/`: maintained role instructions and metadata.
- `shared/`: shared evidence, scope, context, and improvement rules.
- `.claude/agents/`: complete, generated Claude Code agents.
- `.codex/agents/`: complete, generated Codex agents.
- `scripts/install.py`: installs native files, preserves host settings, and backs up explicitly replaced agents.
- [CHANGELOG.md](CHANGELOG.md): release changes and their rationale.
- [docs/BEHAVIOURAL-CHECKS.md](docs/BEHAVIOURAL-CHECKS.md): small, synthetic scenarios for testing future edits.

Each installed definition includes its own role and the shared agreement, so it remains usable when copied to another project. Rebuild instead of editing the generated copies. Keep project data, meeting transcripts, chat logs, credentials, and private feedback out of commits and shared ZIPs.

Publicly available for viewing and forking on GitHub. No open-source licence is granted by this repository.
