# Coroutines with asyncio

<p align="center">
    <img src="../static/3000_parallel_processing/asyncio_burger.png" width="90%">
</p>

<p align="center"><strong>Fig:</strong> Async I/O - one counter; quick orders leave immediately, long-wait orders sit on the bench while the counter keeps serving. Less resource is required: one cook and one staff at counter</p>

See the picture of the burger shop above. There is **one counter** — Counter 1 — with a single staff member taking orders. Customers stand in a **queue**, waiting their turn.

If orders are **quick**, the customer pays, and leaves right away — no waiting bench needed. But if orders are **long**, the staff gives the customer an order slip and sends them to the **waiting bench**. The counter immediately serves the next person in line.

**Coroutines** work the same way. Each customer is a task. When a task must wait for something slow — a network call, disk read, or database query — it sits on the **waiting bench**. In code, that pause is `await`. The **event loop** (the counter staff) does not stand still; it keeps serving the next customer in line and checks the bench from time to time: *Is order #101 ready yet?* When it is, that task picks up where it left off.

Notice the kitchens in the background: only **one kitchen is active**; the others are locked. Same here — asyncio uses only **one process, one thread and one CPU core**.

> | Burger shop | In Python |
> |-------------|-----------|
> | **Counter 1 (staff)** | The **event loop** — one thread that schedules work |
> | **Queue** | **Coroutines / tasks** waiting to run |
> | **Waiting bench (long orders)** | A coroutine **paused at `await`** while I/O completes |
> | **Quick order (no wait)** | A task that finishes immediately, without sitting on the bench |
> | **Kitchen (one active, others locked)** | **One CPU core** doing work at a time |

<br/>

In plain terms:

- A **normal function** (also called as **subroutine** in many languages) runs from start to finish — it does not stop in the middle.
- A **coroutine** can pause when it has to wait, let other tasks run, and then continue from where it left off.

## How coroutines are internally working in python ?

> [!IMPORTANT]
> A **coroutine** is a function that can **pause in the middle** of its work and **resume later** from the same spot. In Python, this builds on the same idea as **generators** — both can stop partway through and continue again (generators use `yield`; async coroutines use `await`).

> [!IMPORTANT]
> Python also runs an **event loop** — a loop that manages many coroutines together. It decides which coroutine runs next, which ones are waiting, and when a paused coroutine is ready to resume. In our burger shop example, the event loop is the **counter staff** keeping the queue and the waiting bench moving.

<p align="center">
    <img src="../static/3100_asyncio_coroutines/event_loop_demo.gif" width="90%">
</p>

<p align="center"><strong>Fig:</strong> Event loop ticks — level-1 coroutines (A, B, C) and a nested level-2 coroutine (B1). Colors: grey = not run, blue = running, yellow = waiting, green = completed.</p>

Source: [`event_loop_animation.py`](../code/3100_asyncio_coroutines/event_loop_animation.py)

### One another image to explain the eventloop and coroutine

<p align="center">
    <img src="../static/3100_asyncio_coroutines/control_flow_demo.gif" width="90%">
</p>

<p align="center"><strong>Fig:</strong> Control (red arrow) moves forward into coroutines and <strong>returns</strong> to parents and the loop. After Coro C finishes, the loop resumes A → A1 → A2, then B → B1. Colors: grey = not run, blue = running, yellow = waiting, green = completed.</p>

Source: [`control_flow_animation.py`](../code/3100_asyncio_coroutines/control_flow_animation.py)


### Below code explain how it is internally organized

> [!NOTE]
> This is just for illustrative purpose. Not the actual implementation

```python
def coroutine():
    print("coroutine: step 1")
    yield                          # pause — control returns to the event loop
    print("coroutine: step 2")
    yield
    print("coroutine: done")


def event_loop(*tasks):
    # Each task is a generator object (a coroutine under the hood)
    active = [task() for task in tasks]

    while active:
        for gen in active[:]:
            try:
                next(gen)          # run until the next yield
            except StopIteration:
                active.remove(gen)


event_loop(coroutine)
```

**Output:**
```
coroutine: step 1
coroutine: step 2
coroutine: done
```

The **event loop** calls `next()` on each coroutine. At **`yield`**, the coroutine pauses and the loop is free to run other tasks. When the loop calls `next()` again, the coroutine resumes where it left off.

