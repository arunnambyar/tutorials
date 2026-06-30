"""
Simple TTL (Time To Live) cache in pure Python.

Run:
    python ttl_cache.py
"""

import time

TTL_SECONDS = 5
_cache: dict[str, tuple[str, float]] = {}


def get_value(key: str) -> str:
    now = time.time()

    if key in _cache:
        value, stored_at = _cache[key]
        age = now - stored_at
        if age < TTL_SECONDS:
            print(f"  cache HIT  '{key}' (age {age:.1f}s)")
            return value
        print(f"  cache EXPIRED '{key}' (age {age:.1f}s)")

    value = f"data-for-{key}-{int(now)}"
    _cache[key] = (value, now)
    print(f"  cache MISS '{key}' -> stored new value")
    return value


def main():
    print(f"TTL = {TTL_SECONDS} seconds\n")

    print("First call:")
    print(get_value("user"))

    print("\nSecond call (immediately - should hit cache):")
    print(get_value("user"))

    print(f"\nWaiting {TTL_SECONDS + 1} seconds...")
    time.sleep(TTL_SECONDS + 1)

    print("\nThird call (after TTL - should refresh):")
    print(get_value("user"))


if __name__ == "__main__":
    main()
