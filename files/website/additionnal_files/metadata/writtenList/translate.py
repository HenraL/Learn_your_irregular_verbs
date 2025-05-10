import os
import re
import sys
from tkinter import *

# --- Configuration ---
SAFE_DIR = os.getcwd()  # Change this to a fixed directory if needed
SAFE_FILENAME_RE = re.compile(r'^[\w\-\.]+\.[a-zA-Z0-9]{1,5}$')  # Allow basic safe extensions (e.g., .txt, .py)

def is_safe_filename(filename):
    """Check if the filename contains only safe characters and includes an extension."""
    return bool(SAFE_FILENAME_RE.fullmatch(filename))

def secure_join(base, *paths):
    """Join paths and prevent escaping the base directory."""
    final_path = os.path.abspath(os.path.join(base, *paths))
    if not final_path.startswith(os.path.abspath(base)):
        raise ValueError("Unsafe file path detected.")
    return final_path

# --- GUI input for text ---
def get_text_from_gui():
    def GetContent(*args):
        nonlocal user_input
        user_input = text_widget.get("0.0", "end-1c")
        window.destroy()

    user_input = ""
    window = Tk()
    text_widget = Text(window)
    text_widget.pack()

    Button(window, text="Continue", command=GetContent).pack()
    window.mainloop()
    return user_input

# --- Entry Point ---
try:
    t = 1
    if t == 1:
        e = get_text_from_gui()
    else:
        with open("English.py", "r") as f:
            e = f.read()

    # --- Get filename and sanitize ---
    filename = input("Enter the name (+extension) of the file that will receive the translated content: ").strip()

    if not is_safe_filename(filename):
        print("Invalid filename. Only alphanumerics, dots, dashes, underscores, and a valid extension are allowed.")
        sys.exit(1)

    try:
        full_path = secure_join(SAFE_DIR, filename)
    except ValueError as ve:
        print(ve)
        sys.exit(1)

    # --- Write file safely ---
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    mode = 0o600  # rw-------

    try:
        fd = os.open(full_path, flags, mode)
        with os.fdopen(fd, 'w') as f:
            f.write(e)
        print(f"File saved safely to: {full_path}")
    except FileExistsError:
        print("Error: File already exists. Aborting.")
    except Exception as err:
        print(f"Failed to write file: {err}")

except Exception as outer_err:
    print(f"Unexpected error: {outer_err}")
