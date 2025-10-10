from typing import List
from yandex_music import Artist


def make_track_link(song_id: str, album_id: str) -> str:
    return f'https://music.yandex.ru/album/{album_id}/track/{song_id}'


def clear_special_char(string: str) -> str:
    special_chars = '\\/:*?"<>|.'

    for ch in special_chars:
        string = string.replace(ch, '')

    return string


def make_artists_title(artists: List[Artist]) -> str:
    return ', '.join([art.name for art in artists])


def make_feats_artists_title(artists: List[Artist]) -> str:
    return 'feat. ' + ', '.join([art.name for art in artists[1:]])
