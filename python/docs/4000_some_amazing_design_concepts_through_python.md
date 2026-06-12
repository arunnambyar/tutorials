# Design Ideas You Can Code in Python

Design patterns and small system ideas become much easier to understand when you see them in **real Python code**. In this chapter, we explore powerful concepts — not as heavy theory, but as **simple, practical examples** you can run and extend.

## 1. Observe file or directory changes

### What is the Observer pattern?

One object (**subject**) changes. Many other objects (**observers**) want to know about that change — without the subject knowing every observer in detail.

### How Watchdog fits in

The [`watchdog`](https://pypi.org/project/watchdog/) library watches folders and files. When something is created, changed, or deleted, your **handler** (observer) is called automatically.

**Code example: [observer_watchdog.py](../code/4000_some_amazing_design_concepts_through_python/observer_watchdog.py)**

```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"File changed: {event.src_path}")

observer = Observer()
observer.schedule(
    MyHandler(),
    path="./watched_folder",
    recursive=False
)
observer.start()

while True:
    observer.join(2)  #  Wait in seconds
```

Install the library using:

```bash
pip install watchdog
```

## 2. TTL (Time To Live) Using Python

### What is TTL?

**TTL** means *Time To Live* — how long a piece of data stays valid before it **expires**.

### How it works?
You store a value in a cache with a **time limit**. After that limit passes, the value **expires** and is no longer used.
Python's standard library does **not** include a TTL cache. The libraries like [`cachetools`](https://pypi.org/project/cachetools/) provide it ready to use.

**Code example: [ttl_cachetools.py](../code/4000_some_amazing_design_concepts_through_python/ttl_cachetools.py)**

```python
from cachetools import TTLCache


my_cache = TTLCache(maxsize=100, ttl=120)  # 120 seconds

my_cache["KEY"] = "VALUE"
print(my_cache["KEY"])
```

Install the library using:

```bash
pip install cachetools
```
