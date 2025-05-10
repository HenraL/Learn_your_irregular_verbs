import os
import re
import sys

# Constants
SAFE_DIR = os.getcwd()  # Or set to a fixed safe path like "/tmp/myapp"
SAFE_FILENAME_RE = re.compile(r'^[\w\-]+\.py$')

def is_safe_filename(filename):
    return bool(SAFE_FILENAME_RE.fullmatch(filename))

def secure_join(base, filename):
    path = os.path.abspath(os.path.join(base, filename))
    if not path.startswith(os.path.abspath(base)):
        raise ValueError("Unsafe file path detected.")
    return path

# User input
name = input("Enter the name of the file (must end in .py, no paths): ").strip()

if not is_safe_filename(name):
    print("Invalid filename. Only use letters, numbers, _, -, and must end in .py.")
    sys.exit(1)

try:
    full_path = secure_join(SAFE_DIR, name)
except ValueError as ve:
    print(f"Invalid path: {ve}")
    sys.exit(1)

# Secure file creation using os.open
flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL  # Prevent overwriting
mode = 0o600  # File permissions: rw-------

try:
    fd = os.open(full_path, flags, mode)
    with os.fdopen(fd, "w") as f:
        a = """# The imports\nfrom tkinter import *\nimport sys\n\n# Initialising the window\nfenetre = Tk()\n..."""
        b = """\n# The few frames\nFrame1 = Frame(fenetre, borderwidth=2, relief=F1, bg=FBG)\n...fenetre.mainloop()"""
        f.write(a)
        f.write(b)
    print(f"File securely written to: {full_path}")
except FileExistsError:
    print("Error: File already exists.")
except Exception as e:
    print(f"Unexpected error writing file: {e}")
