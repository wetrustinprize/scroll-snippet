# Scroll Snippet

Simple scroll snippet.

- [Scroll Snippet](#scroll-snippet)
  - [How to install](#how-to-install)
  - [Configuration](#configuration)
  - [How to run](#how-to-run)
  - [How to use](#how-to-use)

## How to install

```bash
$ pip3 install -r requirements.txt
```

## Configuration

| variable       | what do                                                        | possible values |
| -------------- | -------------------------------------------------------------- | --------------- |
| `KEY_TO_HOLD`  | The key which the script will be listening                     | Any key         |
| `SCROLL_BY`    | Should the script scroll when the x position changes or the y? | `"x"` or `"y"`  |
| `SENSIBILITY`  | How much do you have to move the mouse to get a scroll         | A number        |
| `FREEZE_MOUSE` | Should the mouse stay still when holding the action button?    | A boolean       |
| `HOLD_CTRL`    | Should hold CTRL while scrolling?                              | A boolean       |
| `HOLD_SHIFT`   | Should hold SHIFT while scrolling?                             | A boolean       |
| `HOLD_ALT`     | Should hold ALT while scrolling?                               | A boolean       |

## How to run

Configure your hotkey and sensibility in the `config.py` file.

Then execute the script with `python3 .`.

## How to use

Hold the key specified in the config file and move the mouse.