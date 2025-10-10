from datetime import datetime
import os
from pathlib import Path

import requests
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TPE2, TALB, TCON, TRCK, WXXX, TYER, TDRL, APIC
from yandex_music import Album, Track

from config import TEMP_PATH
from utils.string import make_feats_artists_title, clear_special_char, make_track_link


def decoration_track(track: Track, album: Album, track_path: Path):
    audio = MP3(track_path, ID3=ID3)

    if audio.tags is None:
        audio.add_tags()

    feats = make_feats_artists_title(track.artists)
    release_date = album.release_date
    img = download_img(album.cover_uri)

    # - TIT2 - Название трека (Title)
    # - TPE1 - Исполнитель (Artist)
    # - TALB - Альбом (Album)
    # - TYER - Год (Year)
    # - TPE2 - Исполнитель альбома (Album Artist)
    # - TDRL - Дата релиза (Release Time)
    # - TCON - Жанр (Genre)
    # - TRCK - Номер трека (Track Number)
    # - WXXX - URL (Website)
    # - APIC - Вложенные изображения (Attached Picture)

    # -- TPOS - Позиция диска (Disc Number)
    # -- TCOM - Композитор (Composer)
    # -- TCOP - Авторские права (Copyright)
    # -- TDRC - Дата записи (Recording Time)
    # -- TKEY - Ключ (Musical Key)
    # -- TLEN - Длительность (Length)
    # -- USER - Пользовательские теги (User Defined Text)
    # -- COMM - Комментарии (Comments) (может иметь язык)

    audio.tags.add(TIT2(encoding=3, text=track.title))
    audio.tags.add(TALB(encoding=3, text=album.title))
    audio.tags.add(TCON(encoding=3, text=album.genre))
    audio.tags.add(TPE1(encoding=3, text=track.artists[0].name))

    if track.meta_data:
        if track.meta_data.number:
            audio.tags.add(TRCK(encoding=3, text=track.meta_data.number))

    audio.tags.add(WXXX(encoding=3, text=make_track_link(track.id, str(album.id))))

    if feats != 'feat. ':
        audio.tags.add(TPE2(encoding=3, text=feats))

    if release_date:
        date = datetime.fromisoformat(release_date)
        audio.tags.add(TYER(encoding=3, text=str(date.year)))
        audio.tags.add(TDRL(encoding=3, text=date.strftime("%Y-%m-%d")))

    if img:
        with open(img, 'rb') as img_file:
            img_data = img_file.read()

        audio.tags.add(APIC(mime='image/png', type=3, desc='Cover', data=img_data))
        os.remove(img)
    audio.save()


def download_img(img_link: str) -> str:
    save_path = f"{TEMP_PATH}/{clear_special_char(img_link)}.png"
    url = "https://" + img_link.replace('%%', '1000x1000')

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        with open(save_path, 'wb') as f:
            f.write(response.content)

        return save_path
    except Exception as e:
        print(f'Ошибка при загрузке обложки: {e}')
        return ''
