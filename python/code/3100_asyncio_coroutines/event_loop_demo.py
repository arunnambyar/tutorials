"""Minimal generator-based event loop — illustrative, not real asyncio."""


def coroutine(name: str):
    print(f"{name}: step 1")
    yield  # pause — control returns to the event loop
    print(f"{name}: step 2")
    yield
    print(f"{name}: step 3")


def event_loop(*tasks):
    # Each task is a generator object (a coroutine under the hood)
    active = list(tasks)

    while active:
        for gen in active[:]:
            try:
                next(gen)  # run until the next yield
            except StopIteration:
                active.remove(gen)


if __name__ == "__main__":
    event_loop(coroutine("A"), coroutine("B"), coroutine("C"))
