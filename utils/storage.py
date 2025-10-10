from pathlib import Path

from yandex_music import Album, Track
from config import DOWNLOAD_PATH, TEMP_PATH, STATE_FILE
from core.logger import log_artist, log_album
from utils.string import clear_special_char, make_artists_title
import json


DEFAULT_STATE = {
    "artist": '',
    "album": ''
}


def load_state():
    if not STATE_FILE.exists():
        save_state(DEFAULT_STATE)
        return DEFAULT_STATE
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(new_state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(new_state, f, ensure_ascii=False, indent=4)


def init_dir():
    DOWNLOAD_PATH.mkdir(parents=True, exist_ok=True)
    TEMP_PATH.mkdir(parents=True, exist_ok=True)
    load_state()


def get_save_track_path(album: Album, track: Track) -> Path:
    state = load_state()

    track_file_title = clear_special_char(track.title)
    album_dir_title = clear_special_char(album.title)

    track_artists_dir_title = clear_special_char(make_artists_title(track.artists))
    album_artists_dir_title = clear_special_char(make_artists_title(album.artists))

    artist_path = DOWNLOAD_PATH / album_artists_dir_title
    album_path = artist_path / album_dir_title

    if not artist_path.exists() and album_artists_dir_title != state["artist"]:
        log_artist(album_artists_dir_title, 'success')
        artist_path.mkdir()
    elif album_artists_dir_title != state["artist"]:
        log_artist(album_artists_dir_title, 'exists')

    if not album_path.exists() and album_dir_title != state["album"]:
        log_album(album_dir_title, 'success')
        album_path.mkdir()
    elif album_dir_title != state["album"]:
        log_album(album_dir_title, 'exists')

    state["artist"] = album_artists_dir_title
    state["album"] = album_dir_title
    save_state(state)

    if album_artists_dir_title != track_artists_dir_title:
        track_file_title += f" - {track_artists_dir_title}"

    return album_path / f"{track_file_title}.mp3"
