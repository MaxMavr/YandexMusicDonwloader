from utils.storage import init_dir, save_state, DEFAULT_STATE
from core.logger import log_invalid_link, log_header, log_input
from core.downloader import download_track, download_album, download_artist
from core.parser import parse_link


init_dir()
log_header()

while True:
    link = log_input()
    yandex_object = parse_link(link)

    if yandex_object.type == 'unknown':
        log_invalid_link()
        continue

    if yandex_object.type == 'track':
        download_track(track=yandex_object.id)

    elif yandex_object.type == 'album':
        download_album(album=yandex_object.id)

    elif yandex_object.type == 'artist':
        download_artist(artist=yandex_object.id)

    save_state(DEFAULT_STATE)
