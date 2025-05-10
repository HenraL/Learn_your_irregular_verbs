import os
import re
import sys

# Constants
SAFE_DIR = os.getcwd()  # or set this to a fixed path like "/tmp/safe_output"
SAFE_FILENAME_RE = re.compile(r'^[\w\-]+\.py$')  # Only allow safe .py names

# Validate and secure filename
def is_safe_filename(filename):
    return bool(SAFE_FILENAME_RE.fullmatch(filename))

def secure_join(base, filename):
    path = os.path.abspath(os.path.join(base, filename))
    if not path.startswith(os.path.abspath(base)):
        raise ValueError("Unsafe path detected")
    return path

# Get user input
name = input("Please enter the name of the file (without path, must end in .py): ").strip()

# Validate
if not is_safe_filename(name):
    print("Invalid filename. Must be alphanumeric with dashes/underscores and end in .py")
    sys.exit(1)

try:
    full_path = secure_join(SAFE_DIR, name)
except ValueError as ve:
    print(ve)
    sys.exit(1)

# Optional: Use 'x' mode to avoid overwriting
try:
    with open(full_path, "x") as f:
        a = """# The imports\nfrom tkinter import *\nimport sys\n\n# Initialising the window\nfenetre = Tk()\n..."""
        b = """\n# The few frames\nFrame1 = Frame(fenetre, borderwidth=2, relief=F1, bg=FBG)\n...fenetre.mainloop()"""
        f.write(a)
        f.write(b)
    print(f"File created at {full_path}")
except FileExistsError:
    print("Error: File already exists. Aborting.")
except Exception as e:
    print(f"Failed to write file: {e}")
