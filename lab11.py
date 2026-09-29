"""Day 11 learner CLI wrapper."""
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from svm11.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
