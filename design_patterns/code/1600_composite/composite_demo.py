"""
Composite pattern demo: comment thread with nested replies.

Run:
    python composite_demo.py

One Comment class acts as both leaf (no replies) and branch (has replies).
Display and reply counts roll up the tree the same way at every level.
"""

from __future__ import annotations


class Comment:
    """One node type — a leaf when it has no replies, a branch when it does."""

    def __init__(self, author: str, text: str) -> None:
        self._author = author
        self._text = text
        self._replies: list[Comment] = []

    def add_reply(self, reply: Comment) -> None:
        self._replies.append(reply)

    def author(self) -> str:
        return self._author

    def text(self) -> str:
        return self._text

    def is_leaf(self) -> bool:
        return not self._replies

    def total_replies(self) -> int:
        return sum(1 + reply.total_replies() for reply in self._replies)

    def display(self, indent: int = 0) -> None:
        prefix = "  " * indent
        if self.is_leaf():
            print(f"{prefix}- {self._author}: {self._text}")
            return

        reply_count = self.total_replies()
        suffix = f" [{reply_count} replies]" if reply_count else ""
        print(f"{prefix}+ {self._author}: {self._text}{suffix}")
        for reply in self._replies:
            reply.display(indent + 1)


def main() -> None:
    print("=== Composite: comment thread ===\n")

    # Thread shape — every node is Comment:
    # Alice (post)
    # ├── Bob → Carol, Dave
    # ├── Eve
    # └── Frank → Grace, Heidi

    post = Comment("Alice", "Can someone explain the Composite pattern?")

    # Create top-level replies — all use the same Comment class
    bob = Comment("Bob", "It treats single items and groups the same way.")
    eve = Comment("Eve", "We use it for nested menus at work.")       # will stay a leaf
    frank = Comment("Frank", "Here is a code example...")            # will become a branch

    # Attach replies to the post
    post.add_reply(bob)
    post.add_reply(eve)
    post.add_reply(frank)

    # Bob becomes a branch — add replies under Bob
    bob.add_reply(Comment("Carol", "Nice summary!"))
    bob.add_reply(Comment("Dave", "Think folder inside folder."))

    # Eve stays a leaf — no sub-replies added

    # Frank becomes a branch — add replies under Frank
    frank.add_reply(Comment("Grace", "That helped, thanks."))
    frank.add_reply(Comment("Heidi", "Saving this thread."))

    post.display(0)
    print(f"\nTotal replies in thread: {post.total_replies()}")


if __name__ == "__main__":
    main()
