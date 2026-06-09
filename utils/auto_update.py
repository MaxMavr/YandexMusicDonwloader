from core.downloader import download_artist
from core.logger import log_auto_update
from core.parser import parse_link
from utils.storage import load_auto_update


def auto_update():
    links = load_auto_update()

    auto_update_artists_id = []

    for link in links:
        yandex_object = parse_link(str(link))

        if yandex_object.type == 'artist':
            auto_update_artists_id.append(yandex_object.id)

    if auto_update_artists_id:
        log_auto_update()

        for idx in auto_update_artists_id:
            download_artist(artist=idx)

