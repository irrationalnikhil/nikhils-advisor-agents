#!/usr/bin/env python3
"""Install the native agents without changing host settings or unrelated files."""
import argparse
from datetime import datetime, timezone
import os
from pathlib import Path
import shutil
import sys
import tempfile

from build import ROOT, build


def plan_install(platform, project=None, user_home=None):
    base = Path(project).expanduser().resolve() if project else Path(user_home or Path.home()).expanduser().resolve()
    if not base.is_dir():
        raise ValueError(f"Destination directory does not exist: {base}")
    platforms = ("codex", "claude") if platform == "both" else (platform,)
    plan = []
    for host in platforms:
        source = ROOT / f".{host}/agents"
        if host == "codex" and project is None and user_home is None:
            destination = Path(os.environ.get("CODEX_HOME", str(base / ".codex"))).expanduser().resolve() / "agents"
        else:
            destination = base / f".{host}/agents"
        for item in sorted(source.iterdir()):
            if item.is_file():
                target = destination / item.name
                identical = target.is_file() and item.read_bytes() == target.read_bytes()
                plan.append((item, target, "unchanged" if identical else "replace" if target.exists() else "create"))
    return plan


def install(plan, replace=False, dry_run=False):
    # Complete preflight before any destination mutation.
    conflicts = [str(target) for _, target, action in plan if action == "replace"]
    if conflicts and not replace:
        raise ValueError("Existing agents differ; no files changed. Review them, then use --replace to save backups and update:\n" + "\n".join(conflicts))
    for _, target, _ in plan:
        if target.is_symlink() or (target.exists() and not target.is_file()):
            raise ValueError(f"Refusing non-regular destination: {target}")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    for source, target, action in plan:
        print(f"{action}: {target}")
        if dry_run or action == "unchanged":
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        if action == "replace":
            # Backups live outside the recursively discovered agents directory.
            backup = target.parent.parent / "advisor-agent-backups" / stamp / target.name
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, backup)
        with tempfile.NamedTemporaryFile(dir=target.parent, prefix=".install-", suffix=".tmp", delete=False) as out:
            temp_path = Path(out.name)
            out.write(source.read_bytes())
        try:
            os.replace(temp_path, target)
        finally:
            temp_path.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--platform", choices=("codex", "claude", "both"), required=True)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument("--project", type=Path, help="Install into this existing project's native agent directories")
    scope.add_argument("--global", dest="global_scope", action="store_true", help="Install for the current OS user")
    parser.add_argument("--replace", action="store_true", help="Back up and replace differing agents with these names")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()
    try:
        build(check=True)
        plan = plan_install(args.platform, args.project)
        install(plan, args.replace, args.dry_run)
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print("Preview complete." if args.dry_run else "Agent files ready. Start a new session and ask it to delegate to a named agent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
