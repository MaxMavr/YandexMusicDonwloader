from typing import Literal

from config import DOWNLOAD_PATH, VERSION

GREEN = "\033[92m"
GRAY = "\033[90m"
RED = "\033[91m"
RESET = "\033[0m"

COLORS = {
    "success": GREEN,
    "exists": GRAY,
    "error": RED,
}


def _log(title: str, description: str, status: Literal["success", "exists", "error"]):
    color = COLORS.get(status, RESET)
    print(f'\t{color}{title}{RESET} {description}')


def log_artist(description: str, status: Literal["success", "exists", "error"]):
    _log('[ Артист ]', description, status)


def log_album(description: str, status: Literal["success", "exists", "error"]):
    _log('[ Альбом }', description, status)


def log_track(description: str, status: Literal["success", "exists", "error"]):
    _log('[  Трек  >', description, status)


def log_header():
    print("\n\n\n\t           Я Н Д Е К С   С К А Ч И В А Т Е Л Ь"
          f"\n\n\t{GRAY}[ Версия ] {VERSION}"
          f"\n\t[ Папка  ] {DOWNLOAD_PATH}{RESET}\n")


def log_invalid_link():
    _log('[ Ошибка ]', 'Что-то херню ты ввёл! Попробуй ещё разок', 'error')

    # print(
    #     "\t _          _   _ "
    #     "\n\t| |    ___ | | | |"
    #     "\n\t| |   / _ \\| | | |"
    #     "\n\t| |__| (_) | | |_|"
    #     "\n\t|_____\\___/|_| (_)"
    #     "\n\n\tЧто-то херню ты ввёл! Попробуй ещё разок\n"
    # )


def log_input() -> str:
    return input("\n\t[ Ссылка ] ")
