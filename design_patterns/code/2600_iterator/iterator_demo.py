"""
Iterator pattern demo. Run: python iterator_demo.py
"""

from abc import ABC, abstractmethod


# --- Iterator ---

class Iterator(ABC):
    """GoF Iterator: traverse without exposing the aggregate's structure."""

    @abstractmethod
    def first(self) -> None:
        pass

    @abstractmethod
    def next(self) -> None:
        pass

    @abstractmethod
    def is_done(self) -> bool:
        pass

    @abstractmethod
    def current_item(self) -> str:
        pass


class PlaylistIterator(Iterator):
    """GoF ConcreteIterator: holds position; knows Playlist internals."""

    def __init__(self, playlist: "Playlist") -> None:
        self._playlist = playlist
        self._index = 0

    def first(self) -> None:
        self._index = 0

    def next(self) -> None:
        self._index += 1

    def is_done(self) -> bool:
        return self._index >= len(self._playlist._tracks)

    def current_item(self) -> str:
        return self._playlist._tracks[self._index]


# --- Aggregate ---

class Aggregate(ABC):
    """GoF Aggregate: factory for an Iterator over this collection."""

    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass


class Playlist(Aggregate):
    """GoF ConcreteAggregate: stores tracks; creates PlaylistIterator."""

    def __init__(self, tracks: list[str]) -> None:
        self._tracks = list(tracks)

    def create_iterator(self) -> Iterator:
        return PlaylistIterator(self)


# --- Client ---

class HeadUnit:
    """GoF Client: uses Aggregate + Iterator only — never reads _tracks."""

    def play_all(self, aggregate: Aggregate) -> None:
        iterator = aggregate.create_iterator()
        iterator.first()

        n = 1
        while not iterator.is_done():
            track = iterator.current_item()
            print(f"  [{n}] Now playing: {track}")
            n += 1
            iterator.next()


# --- Demo ---

def main() -> None:
    print("=== Iterator: music playlist ===\n")

    road_trip = Playlist(
        [
            "Highway Star - Deep Purple",
            "Life is a Highway - Tom Cochrane",
            "Radar Love - Golden Earring",
        ]
    )

    print("[Client] Starting playlist")
    HeadUnit().play_all(road_trip)
    print("[Client] Playlist finished")


if __name__ == "__main__":
    main()
