#!/bin/env python3
import autopy as ap
import time
import mouse
from pynput.mouse import Listener
import logging
import random as r

logging.basicConfig(filename="mouse_log.txt",
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')


clickOn = False


def on_move(x, y):
    global clickOn
    if clickOn and pixelPadding(x, y):
        logging.info("Mouse moved to ({0}, {1})".format(x, y))
        ap.mouse.click(delay=randOneOrTwoMs())
        print("click ({0}, {1})".format(x, y))


def on_click(x, y, button, pressed):
    if pressed:
        logging.info(
            'Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))


def on_scroll(x, y, dx, dy):
    global clickOn
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
    print(clickOn)
    clickOn = (dy == -1)


def pixelPadding(x, y):
    padding = r.randrange(4) + 3
    return x % padding == 0 and y % padding == 0


def randOneOrTwoMs():
    oneOrTwoMs = r.randrange(1) / 10 + 0.1
    noise = r.randrange(99999)/1000000
    return oneOrTwoMs + noise


with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
