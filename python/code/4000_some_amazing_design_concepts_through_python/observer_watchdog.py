"""
Observer design pattern using the watchdog library.

Run:
    pip install watchdog
    python observer_watchdog.py

Then create or edit a file inside ./watched_folder
"""
import time

from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


WATCH_DIR = Path(__file__).parent / "watched_folder"


class PrintChangeHandler(FileSystemEventHandler):
    """Observer: reacts when the file system (subject) changes."""

    def on_created(self, event):
        print(f"[created]  {event.src_path}")

    def on_modified(self, event):
        print(f"[modified] {event.src_path}")

    def on_deleted(self, event):
        print(f"[deleted]  {event.src_path}")


def main():
    WATCH_DIR.mkdir(exist_ok=True)

    print(f"Watching: {WATCH_DIR.resolve()}")
    print("Create or edit a file here. Press Ctrl+C to stop.\n")

    observer = Observer()
    observer.schedule(PrintChangeHandler(), str(WATCH_DIR), recursive=False)
    observer.start()

    try:
        while True:
            observer.join(1)
            print("Waiting for changes...")
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
