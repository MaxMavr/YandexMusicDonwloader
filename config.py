from os import getenv
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

VERSION = "1.4.2"

load_dotenv(find_dotenv())
DOWNLOAD_PATH = Path(getenv('DOWNLOAD_PATH'))
TEMP_PATH = DOWNLOAD_PATH / "temp"
STATE_FILE = TEMP_PATH / "state.json"
