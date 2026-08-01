# Python `@decorator` vs Design Patterns

## On this page

- [The common confusion](#the-common-confusion)
- [Adapter implementation using decorator](#adapter-implementation-using-decorator)
- [Is `@decorator` the Decorator pattern?](#is-python-decorator-the-decorator-design-pattern)

## The common confusion

After reading about the [Adapter pattern](1500_adapter.md), a natural question appears:

> An Adapter role can be achieved using a Python decorator — so why is the Adapter design pattern important? Isn't it just a subgroup of Python decorators?

**Short answer: No.**

Think of it this way: a Python `@decorator` is **syntax** — a built-in way to wrap a function or class. Design patterns such as **Adapter** and **Decorator** are **architecture choices** — named ways to structure classes and objects.

Python decorators make many patterns *easier to write*, but the syntax does not replace the architectural reasoning behind the patterns.

Patterns you can implement with a Python decorator — fully or in a **simplified form** — are given below:

| Pattern | What the decorator typically does |
|---|---|
| [**Adapter**](1500_adapter.md) | Translates a function's parameters or return value to match a legacy interface |
| [**Decorator**](2000_decorator.md) | Wraps a function or class to add behavior while keeping the same call surface |
| [**Proxy**](1700_proxy.md) | Adds access control, lazy loading, caching, or logging around a callable |
| [**Singleton**](1000_singleton.md) | Ensures a class creates or returns only one shared instance |
| [**Facade**](1800_facade.md) | Exposes one simple decorated entry point that hides several underlying calls |


## Adapter implementation using decorator

Here, the decorator plays a small Adapter role: the **caller** uses a new function signature (`user_id`), and the wrapper **translates** that call into what the **legacy function** already expects (`id_str`). The old function stays unchanged — only the wrapper sits in between.

```python
# Function-level signature adapter: translates the new caller interface
# (user_id: int) into the legacy function interface (id_str: str)
def adapt_legacy_fetch(func):
    def wrapper(user_id: int):
        # New caller passes user_id; legacy function expects id_str
        return func(id_str=f"USER-ID-{user_id}")
    return wrapper


@adapt_legacy_fetch
def legacy_get_user(id_str: str):
    return {"id": id_str, "status": "active"}


# Client code uses the new signature
print(legacy_get_user(101))
```


## Is Python `@decorator` the Decorator design pattern?

**Not automatically.** They share a name, but they are not the same thing.

| | **Python `@decorator`** | **Decorator design pattern** |
|---|---|---|
| **What it is** | Language feature — syntactic sugar for higher-order functions | Object-oriented structural pattern |
| **Mechanism** | Wraps a function or class at definition time | Wraps an object instance that shares the same interface |
| **Primary goal** | Reuse wrapper logic around callables | Add responsibilities dynamically without changing the interface |
| **Typical use** | Logging, auth checks, timing, simple wrappers | Stack behaviors on an object at runtime |


<br/>
<p>
    <span style="float: left;">
        <a href="1500_adapter.md">Previous: Adapter</a>
        &nbsp;
        <a href="1600_composite.md">Next: Composite</a>
    </span>
    <span style="float: right;">
        <a href="../../README.md">Home</a>
        &nbsp;|&nbsp;
        <a href="index.md">Back to Design Patterns Index</a>
    </span>
</p>
