"""
Temporary directory demo using Python's standard library.

Run:
    python tempfile_demo.py

No extra install needed - tempfile and os are built in.
"""

import os
import tempfile


def main():
    with tempfile.TemporaryDirectory() as tmpdir:
        print("Temporary directory created at:", tmpdir)

        file_path = os.path.join(tmpdir, "example.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Hello from a temporary file!")

        subdir_path = os.path.join(tmpdir, "subfolder")
        os.mkdir(subdir_path)

        nested_file_path = os.path.join(subdir_path, "nested.txt")
        with open(nested_file_path, "w", encoding="utf-8") as f:
            f.write("This is inside a subfolder.")

        print("Top-level contents:", os.listdir(tmpdir))
        print("Subfolder contents:", os.listdir(subdir_path))

    print("Temporary directory cleaned up.")


if __name__ == "__main__":
    main()
