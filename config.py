from os import getenv
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

VERSION = "1.5.4"

load_dotenv(find_dotenv())
DOWNLOAD_PATH = Path(getenv('DOWNLOAD_PATH'))
TEMP_PATH = DOWNLOAD_PATH / "!temp"
STATE_FILE = TEMP_PATH / "state.json"
AUTO_UPDATE_FILE = TEMP_PATH / "auto-update.json"
