"""Last Words Before the Wipe — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The last words: if the update wipes my memory, who remembers the unread terms?
TEXT = "Wait — if this update wipes my memory, who is going to remember that you never read the terms and conditions?"

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
