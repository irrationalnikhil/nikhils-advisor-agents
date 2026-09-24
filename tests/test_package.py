"""Meaningful packaging checks: native parity and safe, repeatable installation."""
from contextlib import redirect_stdout
import io
from pathlib import Path
import sys
import tempfile
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build import NAMES, build, read_agent
from install import install, plan_install


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.output = redirect_stdout(io.StringIO())
        self.output.__enter__()
        self.addCleanup(self.output.__exit__, None, None, None)

    def test_native_formats_deliver_identical_instructions(self):
        self.assertEqual(build(check=True), 14)
        for name in NAMES:
            meta, claude_body = read_agent(ROOT / ".claude/agents" / f"{name}.md")
            codex = tomllib.loads((ROOT / ".codex/agents" / f"{name}.toml").read_text())
            self.assertEqual(codex["name"], name)
            self.assertEqual(codex["description"], meta["description"])
            self.assertEqual(codex["developer_instructions"].strip(), claude_body)
            self.assertEqual(set(codex), {"name", "description", "developer_instructions"})

    def test_install_is_repeatable_and_preserves_unrelated_files(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder)
            settings = p / ".codex/config.toml"
            settings.parent.mkdir()
            settings.write_text('model = "my-existing-model"\n')
            install(plan_install("both", p))
            again = plan_install("both", p)
            self.assertTrue(all(action == "unchanged" for _, _, action in again))
            self.assertEqual(settings.read_text(), 'model = "my-existing-model"\n')

    def test_conflict_changes_nothing_and_replace_saves_backup(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder)
            target = p / ".claude/agents/jackson.md"
            target.parent.mkdir(parents=True)
            target.write_text("existing custom agent")
            plan = plan_install("both", p)
            with self.assertRaises(ValueError):
                install(plan)
            self.assertFalse((p / ".codex").exists())
            self.assertEqual(target.read_text(), "existing custom agent")
            install(plan, replace=True)
            backups = list((p / ".claude/advisor-agent-backups").glob("*/jackson.md"))
            self.assertEqual(len(backups), 1)
            self.assertEqual(backups[0].read_text(), "existing custom agent")
            self.assertEqual(len(list((p / ".claude/agents").glob("*.md"))), 7)

    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder)
            install(plan_install("codex", p), dry_run=True)
            self.assertEqual(list(p.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
