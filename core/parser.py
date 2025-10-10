import re
from dataclasses import dataclass
from typing import Optional, Literal

LINK_PATTERNS = {
    "track": re.compile(r"https://music\.yandex\.ru/album/(\d+)/track/(\d+)|https://music\.yandex\.ru/track/(\d+)"),
    "album": re.compile(r"https://music\.yandex\.ru/album/(\d+)"),
    "artist": re.compile(r"https://music\.yandex\.ru/artist/(\d+)")
}


@dataclass
class MusicLinkInfo:
    type: Literal["track", "album", "artist", "unknown"]
    id: Optional[str] = None


def parse_link(link: str) -> MusicLinkInfo:
    if match := LINK_PATTERNS["track"].match(link):
        return MusicLinkInfo("track", match.group(2) or match.group(3))

    if match := LINK_PATTERNS["album"].match(link):
        return MusicLinkInfo("album", match.group(1))

    if match := LINK_PATTERNS["artist"].match(link):
        return MusicLinkInfo("artist", match.group(1))

    return MusicLinkInfo("unknown")