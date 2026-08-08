"""
GoF Composite pattern demo — folder and file tree.

Run:
    python composite_gof_demo.py

Classic split: File (Leaf) and Folder (Composite) share FileSystemComponent.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    """Component — common interface for files and folders."""

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def size_kb(self) -> float:
        pass

    @abstractmethod
    def display(self, indent: int = 0) -> None:
        pass


class File(FileSystemComponent):
    """Leaf — a file cannot contain other items."""

    def __init__(self, file_name: str, size_kb: float) -> None:
        self._name = file_name
        self._size_kb = size_kb

    def name(self) -> str:
        return self._name

    def size_kb(self) -> float:
        return self._size_kb

    def display(self, indent: int = 0) -> None:
        prefix = "  " * indent
        print(f"{prefix}- {self._name} ({self._size_kb} KB)")


class Folder(FileSystemComponent):
    """Composite — a folder contains files and other folders."""

    def __init__(self, folder_name: str) -> None:
        self._name = folder_name
        self._children: list[FileSystemComponent] = []

    def add(self, component: FileSystemComponent) -> None:
        self._children.append(component)

    def name(self) -> str:
        return self._name

    def size_kb(self) -> float:
        return sum(child.size_kb() for child in self._children)

    def display(self, indent: int = 0) -> None:
        prefix = "  " * indent
        print(f"{prefix}+ {self._name}/ (total {self.size_kb()} KB)")
        for child in self._children:
            child.display(indent + 1)


def main() -> None:
    print("=== GoF Composite: folder and file tree ===\n")

    # Tree shape:
    # project/
    # ├── src/
    # │   ├── main.py
    # │   └── utils.py
    # ├── docs/
    # │   └── readme.md
    # └── LICENSE

    project = Folder("project")

    src = Folder("src")
    src.add(File("main.py", 12.0))
    src.add(File("utils.py", 4.5))

    docs = Folder("docs")
    docs.add(File("readme.md", 2.0))

    project.add(src)
    project.add(docs)
    project.add(File("LICENSE", 1.0))

    project.display(0)
    print(f"\nTotal project size: {project.size_kb()} KB")


if __name__ == "__main__":
    main()
