import os
import sys
import re
from tkinter import *

SAFE_DIR = os.getcwd()  # Define a base directory to restrict writes

# Whitelist pattern for safe filenames
SAFE_FILENAME_RE = re.compile(r'^[\w\-\.]+$')

def is_safe_filename(filename):
    return bool(SAFE_FILENAME_RE.fullmatch(filename))

def secure_join(base, *paths):
    final_path = os.path.abspath(os.path.join(base, *paths))
    if not final_path.startswith(os.path.abspath(base)):
        raise ValueError("Unsafe file path detected!")
    return final_path

def get_content():
    global e
    e = text.get("0.0", "end-1c")
    root.destroy()

# Get text from user via Tkinter
t = 1
if t == 1:
    root = Tk()
    text = Text(root)
    text.pack()
    Button(root, text="Continue", command=get_content).pack()
    root.mainloop()
else:
    with open("English.py", "r") as f:
        e = f.read()

# Get and validate filename
filename = input("Enter the name (+extension) of the file that will receive the translated content: ").strip()

if "." not in filename:
    print("No extension present in the file")
    sys.exit(1)

if not is_safe_filename(filename):
    print("Unsafe filename detected.")
    sys.exit(1)

try:
    full_path = secure_join(SAFE_DIR, filename)
except ValueError as ve:
    print(ve)
    sys.exit(1)

# Write the file safely
try:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    mode = 0o600  # Only readable/writable by the user
    fd = os.open(full_path, flags, mode)
    with os.fdopen(fd, "w") as f:
        f.write(e)
    print(f"File successfully written to: {full_path}")
except FileExistsError:
    print("Error: File already exists. Aborting to prevent overwrite.")
except Exception as ex:
    print(f"Failed to write file: {ex}")

