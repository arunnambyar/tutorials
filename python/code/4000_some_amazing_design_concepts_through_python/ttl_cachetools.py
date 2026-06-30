"""
TTL cache using the cachetools library (built-in TTL support).

Run:
    pip install cachetools
    python ttl_cachetools.py
"""

import time

from cachetools import TTLCache
from datetime import datetime


TTL_SECONDS = 5
my_cache = TTLCache(maxsize=100, ttl=TTL_SECONDS)


def main():
    print(f"\nUsing cachetools.TTLCache (ttl={TTL_SECONDS} SECONDS)")

    set_time = datetime.now()
    my_cache["NAME"] = "ARUN"

    print(f"\nValue after: {datetime.now() - set_time} seconds of setting")
    print(f"VALUE: {my_cache['NAME']}")

    time.sleep(2)

    print(f"\nValue after: {datetime.now() - set_time} seconds of setting")
    print(f"VALUE: {my_cache['NAME']}")

    time.sleep(5)

    print(f"\nValue after: {datetime.now() - set_time} seconds of setting")
    print("WILL BE KEY ERROR >>>")
    print(f"VALUE: {my_cache['NAME']}")


if __name__ == "__main__":
    main()
