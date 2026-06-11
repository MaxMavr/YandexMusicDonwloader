from core.downloader import download_artist
from core.logger import log_auto_empty_list
from core.parser import parse_link
from utils.storage import load_auto_list


def auto_update():
    links = load_auto_list()

    artist_ids = []

    for link in links:
        yandex_object = parse_link(link)

        if yandex_object.type == 'artist':
            artist_ids.append(yandex_object.id)

    if not artist_ids:
        log_auto_empty_list()
        return

    for idx in artist_ids:
        download_artist(artist=idx)
