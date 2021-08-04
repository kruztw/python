from pynput.keyboard import Listener

def keystrokes(key: str) -> None:
    print(key)

with Listener(on_press=(lambda event: keystrokes(event))) as (log):
    log.join()
