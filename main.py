import shutil
import sys
from pathlib import Path

SOURCE_PATH = Path(__file__).resolve().parent / "happy.png"
DESTINATION_PATH = Path("/output/entry.png")


def main() -> int:
    DESTINATION_PATH.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE_PATH, DESTINATION_PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
