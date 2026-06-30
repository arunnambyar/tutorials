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


event_loop(coroutine("A"), coroutine("B"), coroutine("C"))
```

**Output:**
```
A: step 1
B: step 1
C: step 1
A: step 2
B: step 2
C: step 2
A: step 3
B: step 3
C: step 3
```

Source: [`event_loop_demo.py`](../code/3100_asyncio_coroutines/event_loop_demo.py)

The **event loop** calls `next()` on each coroutine in turn. At **`yield`**, the coroutine pauses and the loop moves on to the next task. When every task has yielded once, the loop starts another round — so steps from A, B, and C are **interleaved**. When a coroutine has no more code after its last `yield`, `next()` raises **`StopIteration`** and the loop removes that task.


## Advantages of concurrency

The previous example showed many tasks taking turns in one loop. While one task **waits**, others can **move forward**. That is the main win.

### **Below shows some use cases of _coroutines_ or _async I/O_**

**1. Waiting for slow work (I/O) does not block everything**

Network calls, file reads, and database queries spend most of their time **waiting** — not using the CPU.

*Simple example:* Task A starts a web request and pauses at `await`. While the response travels over the network, the loop runs Task B and Task C. When the response arrives, Task A resumes. One thread handled all three without sitting idle during the wait.

**2. Many independent jobs can make progress together**

Sometimes your program has several things that should run cuncurrently — not one after another in a strict line.

*Simple example:* 
 - A game loop updates player input, enemy AI, and the scoreboard in the same frame.
  - A UI app refreshes the clock while also handling button clicks.

**3. Many tasks, one thread — less overhead than many processes**

Each new **process** costs extra memory and setup. Coroutines share one process and one thread, so you can run **many** waiting tasks without spawning a process per task.

*Simple example:* A server handling 1,000 open client connections with asyncio uses far less memory than 1,000 separate processes — because most connections are just waiting for data, and the event loop switches between them cheaply.

## The building blocks of concurrency

Python async concurrency rests on two pieces working together:

> | Component | What it does | Burger shop |
> |-----------|--------------|---------------|
> | **Coroutine** | A task that can **pause** and **resume** mid-work | A customer — may sit on the **waiting bench** while a long order cooks |
> | **Event loop** | Chooses which coroutine runs next, and when to wake a paused one | The **counter staff** — serves the queue and checks the bench |

**Coroutines** are the work itself — functions that stop at `await` (or `yield` in our generator demo) and pick up again later.

**The event loop** is the manager — it keeps active tasks in a queue, runs each until it pauses, then moves on to the next. When I/O is ready, it resumes the waiting coroutine.

## Non-blocking waiting - the core idea behind **Concurrency**

Concurrency in python only works as expected when slow tasks **do not block the `control flow` while it waits**. If you are using blocking calls inside coroutines, the coroutine will not give you any advantages.

### Blocking vs non-blocking I/O

| | Blocking call | Non-blocking call |
|---|---|---|
| **Example** | `requests.get(url)`, blocking `socket.recv()` | async `aiohttp`, or `socket.setblocking(False)` |
| **While waiting** | Control sits inside the function | Call returns immediately; task pauses and resumed later |

> [!IMPORTANT]
> A single **blocking** call on the event-loop freezes **every** coroutine until that call finishes — nothing else can run in the meantime.

The animations below contrast **blocking** and **non-blocking** I/O on the same event loop.

<p align="center">
    <img src="../static/3100_asyncio_coroutines/blocking_flow_demo.gif" width="90%">
</p>

<p align="center"><strong>Fig:</strong> Blocking flow — the event loop freezes until each call returns.</p>


<p align="center">
    <img src="../static/3100_asyncio_coroutines/control_flow_demo.gif" width="90%">
</p>

<p align="center"><strong>Fig:</strong> Non-blocking flow — the loop switches tasks while I/O waits.</p>

As explained above, the non-blocking calls are very important in coroutines.

### What is a `non-blocking` call ?

**Let me explain this with an example — posting data to a server**

Suppose you call **`requests.post()`** to send data to a server. That single call does not finish quickly. It waits while:

- your data travels to the server
- the server processes it
- the response travels back to you

Your program **cannot move on** until all of that is done. The program controll sits inside `requests.post()` the whole time. That is a **blocking** call.

A **non-blocking** (async) approach works differently. You **start** the request, then **return control to the event loop** right away (via `await` or `yield`). While the work happens in lower layer of the network or in server, the loop can run **other coroutines**. When the response is ready, the loop **resumes** the previous task.

Non-blocking I/O needs **async-friendly libraries**. The popular `requests` library is **blocking only**. So are calls like `time.sleep()`. For asyncio, use alternatives such as **`aiohttp`**, **`httpx`** (async mode), or **`asyncio.sleep()`**.

> [!NOTE]
> **Try it yourself:** Go through the custom nonblocking http post library, coroutines and event-loop [`nonblocking_http.py`](../code/3100_asyncio_coroutines/nonblocking_http.py) sends an HTTP POST using a **custom event loop** and generator-based coroutines (`yield`) — no asyncio, threads, or multiprocessing. Socket helpers live in [`nonblock/http.py`](../code/3100_asyncio_coroutines/nonblock/http.py). It explains how non-blocking is implemented and managed.


### Why can't we use `threads or processes` to achieve **non-blocking calls?**

Threads and processes can be used to create non-blocking calls. But each thread or process costs extra memory and setup. Asyncio event-loops can manage **many** waiting tasks on **one** thread, which is lighter when most time is spent waiting (web servers, API clients, chat apps).

### What kinds of tasks can be improved by coroutines?

Some type of tasks take a long time to finish. Here are common examples:

1. Sending or receiving data over the **network**
2. Running **database** queries
3. **Reading or writing** files on disk
4. **Video or audio** processing
5. **Heavy data** processing

Items 1–3 are **I/O-bound** — the program spends most of its time **waiting** on i/o devices (network, disk, or database).

Items 4–5 are **CPU-bound** — the **CPU** does the heavy work.

Non-blocking coroutines help to improve the performance of **I/O-bounded** tasks, where waiting is the bottleneck. Because when the task is waiting in network, the CPU is free to do useful work elsewhere. Then event-loops can switch the control to the other coroutines.

**CPU-bounded** tasks are different: they keep the CPU busy the whole time. The CPU has no free time to hand over the control to other work. Pausing and switching coroutines does not help here.

> **Why?** Asyncio runs on **one process, one thread and one CPU core** at a time. Switching coroutines only benificial when one task **stops using the CPU** — for example, while it is waiting on the network. In CPU-bound work, the core stays busy calculating. Switching to another coroutine on the same thread does not run two calculations at same time; it just **takes turns**, and the total CPU work stays the same. You may even add **extra overhead** from pausing and resuming. To finish CPU-heavy jobs faster, run them in **parallel** across multiple cores — Go through my parallel processing tutorial for more details [Parallel Processing](./3000_parallel_processing.md).


