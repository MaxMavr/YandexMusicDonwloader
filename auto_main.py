from utils.auto_update import auto_update
from utils.storage import init_dir, save_state, DEFAULT_STATE, append_auto_list
from core.logger import log_invalid_link, log_auto_header, log_input, log_not_artist
from core.downloader import download_artist
from core.parser import parse_link


init_dir()
log_auto_header()
auto_update()

while True:
    link = log_input()
    yandex_object = parse_link(link)

    if yandex_object.type == 'unknown':
        log_invalid_link()
        continue

    if yandex_object.type == 'artist':
        download_artist(artist=yandex_object.id)
        append_auto_list(link)

    elif yandex_object.type in ['track', 'album']:
        log_not_artist()

    save_state(DEFAULT_STATE)
