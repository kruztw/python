from zipfile import ZipFile
from pynput.keyboard import Listener as keyboardListener
from pynput.mouse import Listener as mouseListener
from pynput.keyboard import Key
import time


keys = []

def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

def on_press(key):
    print("press ", key)

def on_release(key):
    print("release ", key)

def moveTo(x, y):
    print(f"moveTo: ({x}, {y})")


def click(x, y, button, is_press):
    print(f"Mouse button: {button} in ({x}, {y}) {'press' if is_press else 'release'}")


def scroll(x1, y1, x2, y2):
    if x2:
        print(f"scroll from ({x1}, {y1}) into { 'right' if x2 > 0 else 'left'}")
    else:
        print(f"scroll from ({x1}, {y1}) into { 'buttom' if y2 > 0 else 'upper'}")

def main():
    listener1 = mouseListener(on_move=moveTo, on_click=click, on_scroll=scroll)
    listener2 = keyboardListener(on_press=on_press, on_release=on_release)
    listener1.start()
    listener2.start()
    time.sleep(10)
    listener1.stop()
    listener2.stop()

if __name__ == '__main__':
    main()
