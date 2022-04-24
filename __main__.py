from pynput import keyboard, mouse
from time import sleep

from config import KEY_TO_HOLD, SCROLL_BY, SENSIBILITY, FREEZE_MOUSE, HOLD_ALT, HOLD_CTRL, HOLD_SHIFT

keyboardController = keyboard.Controller()
mouseController = mouse.Controller()

is_holding = False
last_mouse_position = (0, 0)
scroll = 0


def mouse_move(x, y):
    global is_holding, last_mouse_position, mouseController, scroll

    # Callback for when the mouse is moved
    if not is_holding:
        # Check if should freeze the mouse position
        if not FREEZE_MOUSE:
            last_mouse_position = (x, y)
        return

    # Gets which position has changed
    x_changed = last_mouse_position[0] - x
    y_changed = last_mouse_position[1] - y

    # Adds to the scroll variable according to the SCROLL_BY config
    if x_changed != 0 and SCROLL_BY == "x":
        scroll = scroll + SENSIBILITY * (-1 if x_changed < 0 else 1)
    elif y_changed != 0 and SCROLL_BY == "y":
        scroll = scroll + SENSIBILITY * (-1 if y_changed < 0 else 1)

    # Checks if should scroll or not
    total_scroll = 0

    if scroll > 1:
        total_scroll = 1
        scroll = scroll - 1

    if scroll < -1:
        total_scroll = -1
        scroll = scroll + 1

    # Holds the keys
    if HOLD_CTRL:
        keyboardController.press(keyboard.Key.ctrl)
    if HOLD_SHIFT:
        keyboardController.press(keyboard.Key.shift)
    if HOLD_ALT:
        keyboardController.press(keyboard.Key.alt)

    # Scrolls the mouse
    mouseController.scroll(0, total_scroll)

    # Releases the keys
    if HOLD_CTRL:
        keyboardController.release(keyboard.Key.ctrl)
    if HOLD_SHIFT:
        keyboardController.release(keyboard.Key.shift)
    if HOLD_ALT:
        keyboardController.release(keyboard.Key.alt)

    # Check if should freeze the mouse position
    if FREEZE_MOUSE:
        mouseController.position = last_mouse_position
    else:
        last_mouse_position = (x, y)


def keyboard_press(key):
    global is_holding, mouseController, last_mouse_position

    if is_holding:
        return

    # Callback for when the key is pressed
    try:
        key_char = key.char

        # Check if the key is the one specified in the config
        if key_char == KEY_TO_HOLD and not is_holding:
            # Check if should freeze the mouse position
            if FREEZE_MOUSE:
                last_mouse_position = mouseController.position

            is_holding = True
    except AttributeError:
        return


def keyboard_release(key):
    global is_holding

    # Callback for when the key is released
    try:
        key_char = key.char

        # Check if the key is the one specified in the config
        if key_char == KEY_TO_HOLD and is_holding:
            is_holding = False
    except AttributeError:
        return


# Listener for the keyboard
listener = keyboard.Listener(
    on_press=keyboard_press,
    on_release=keyboard_release)
listener.start()

# Listener for the mouse
listener = mouse.Listener(on_move=mouse_move)
listener.start()

while True:
    sleep(1)
