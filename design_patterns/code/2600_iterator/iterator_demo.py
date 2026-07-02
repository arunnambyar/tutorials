"""
Iterator pattern demo: cycle through music tracks.

Run:
    python iterator_demo.py

The playlist exposes an iterator so the head unit walks tracks one by one.
"""

from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next_track(self) -> str:
        pass


class Playlist:
    def __init__(self, tracks: list[str]) -> None:
        self._tracks = tracks

    def create_iterator(self) -> Iterator:
        return _PlaylistIterator(self._tracks)


class _PlaylistIterator(Iterator):
    def __init__(self, tracks: list[str]) -> None:
        self._tracks = tracks
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._tracks)

    def next_track(self) -> str:
        track = self._tracks[self._index]
        self._index += 1
        return track


class HeadUnit:
    def play_all(self, playlist: Playlist) -> None:
        iterator = playlist.create_iterator()
        track_num = 1
        while iterator.has_next():
            track = iterator.next_track()
            print(f"  [{track_num}] Now playing: {track}")
            track_num += 1


def main() -> None:
    print("=== Iterator: music playlist ===\n")

    road_trip = Playlist(
        [
            "Highway Star - Deep Purple",
            "Life is a Highway - Tom Cochrane",
            "Radar Love - Golden Earring",
        ]
    )

    print("[HeadUnit] Starting playlist")
    HeadUnit().play_all(road_trip)
    print("[HeadUnit] Playlist finished")


if __name__ == "__main__":
    main()
