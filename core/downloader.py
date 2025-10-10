from os import getenv
from typing import Union
from dotenv import load_dotenv, find_dotenv
from yandex_music import Client, Artist, Album, Track

from core.logger import log_track
from core.decorator import decoration_track
from utils.storage import get_save_track_path

load_dotenv(find_dotenv())
yandex_client = Client(getenv('YANDEX_TOKEN'))


def _get_artist(artist: Union[str, Artist]):
    if isinstance(artist, str):
        return yandex_client.artists(artist)[0]
    return artist


def _get_album(album: Union[str, Album]):
    if isinstance(album, str):
        return yandex_client.albums(album)[0].with_tracks()
    return album.with_tracks()


def _get_track(track: Union[str, Track]):
    if isinstance(track, str):
        return yandex_client.tracks(track)[0]
    return track


def download_track(track: Union[str, Track], album: Union[str, Album] = None):
    track = _get_track(track)
    if not album:
        album = track.albums[0]
    album = _get_album(album)

    save_path = get_save_track_path(album, track)

    if save_path.exists():
        log_track(track.title, "exists")
        return

    try:
        track.download(str(save_path))
    except Exception as e:
        log_track(track.title, "error")
        return

    decoration_track(track, album, save_path)

    log_track(track.title, "success")


def download_album(album: Union[str, Album]):
    album = _get_album(album)
    for volume in album.volumes:
        for track in volume:
            download_track(track)


def download_artist(artist: Union[str, Artist]):
    artist = _get_artist(artist)
    for album in artist.get_albums():
        download_album(album)
