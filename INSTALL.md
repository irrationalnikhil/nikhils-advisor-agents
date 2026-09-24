# Install Nikhil's Advisor Agents

## Ask your AI to do it

Drop the ZIP into a tool that can inspect it, or open the extracted folder. Say:

> Install the seven named agents in this package for my current project. Use the native format for this tool. Preserve existing configuration and custom agents; show me any conflicting agent before replacing it. Start a new session if needed, verify discovery, then delegate a small task to one agent. If you cannot install custom agents here, explain where I should open the folder instead.

Project scope is the default. Ask for “all my projects” if you prefer a personal installation. Each person uses their own AI account and tools.

## For the assistant doing the installation

Use the generated definitions without rewriting or expanding them:

| Host | Project destination | Personal destination |
| --- | --- | --- |
| Claude Code | `.claude/agents/*.md` | `~/.claude/agents/*.md` |
| Codex | `.codex/agents/*.toml` | `$CODEX_HOME/agents/*.toml`, normally `~/.codex/agents/*.toml` |

The packaged files are self-contained. `name`, `description`, and `developer_instructions` identify the Codex agents. Claude Code uses YAML frontmatter and a Markdown body. Leave the user's chosen models, approval settings, connectors, and global instructions intact. A project's native definitions can take precedence over personal ones; inspect a conflict rather than treating a successful file copy as proof of which version is running.

With Python 3.11+ available, run the helper from this extracted folder. Substitute the actual destination project path:

```sh
python3 scripts/install.py --platform codex --project "/path/to/project" --dry-run
python3 scripts/install.py --platform codex --project "/path/to/project"
```

Use `--platform claude` or `--platform both` as appropriate. For personal installation:

```sh
python3 scripts/install.py --platform codex --global
```

If same-name agents differ, the helper stops before changing any files. Review the conflict. After the user authorises replacement, add `--replace`; the helper saves previous definitions outside the agents directory under the host's `advisor-agent-backups/`. It never merges or overwrites host configuration. It does not remove an old `bens-nikhil` agent: this package's behavioural advisor is `nikhil`, and both may appear until the user chooses to retire the older one.

If Python is unavailable, copy just the seven native files into the appropriate destination, with the same conflict checks and backups. Do not copy the top-level `agents/` sources directly: those need the shared agreement appended, which the generated native files already contain.

## Confirm it worked

Start a new session in the target project. Ask it to list the seven advisor agents and **delegate** a small task to one by name. Confirm that the tool shows a separate agent activity or worker, rather than just an inline answer written in that persona. A parser check alone does not establish live delegation.

If the agents are missing, check the actual project folder, personal configuration directory, file contents, conflicting names, and the host version. For Codex, also check whether an existing `agents.enabled = false` or managed policy disables delegation; do not silently change it. Follow the host's normal project-trust flow. If the version does not support the native format, report that limitation instead of inventing a configuration key.

The parent should pass an agent's continuation state when resuming it and relay any ten-turn improvement prompt once. The full protocol is included in every installed agent. A platform that supplies no continuation state cannot guarantee a count across separate tasks.

## Format references

Verified against the official documentation on 24 September 2026:

- [OpenAI: custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)
- [OpenAI: configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Anthropic: custom subagents](https://code.claude.com/docs/en/sub-agents)

This package configures agents; it does not provision a continuously running cloud service. Host capabilities, available tools, and permissions determine what an agent can execute.
