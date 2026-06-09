from os import getenv
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

VERSION = "1.4.2"

load_dotenv(find_dotenv())
DOWNLOAD_PATH = Path(getenv('DOWNLOAD_PATH'))
TEMP_PATH = DOWNLOAD_PATH / "!temp"
CONFIG_PATH = DOWNLOAD_PATH / "!config"
STATE_FILE = TEMP_PATH / "state.json"
AUTO_UPDATE_FILE = CONFIG_PATH / "auto-update.json"
