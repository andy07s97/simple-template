# tests/conftest.py
import sys
from pathlib import Path

# 專案根目錄：.../simple-template
ROOT_DIR = Path(__file__).resolve().parents[1]

# 確保 root 在 sys.path 最前面，讓 `import app` 找得到
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

