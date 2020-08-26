#!/usr/bin/python3
import pyautogui
import glob
import game_window as poe
from random import randint
import mss
import mss.tools
from PIL import Image

# Png samples that will be located on screenshoot
highlight_path = './img/highlight/*.png'
img_highlight_needles = glob.glob(highlight_path, recursive=False)

# No more click's than this value.
inventory_limit = 60
items_moved_to_inventory = 0

def click_items(items):
    global items_moved_to_inventory
    for item in items:
        click(item)
        items_moved_to_inventory += 1
        if items_moved_to_inventory == inventory_limit:
            break


def click(item):
    # Absolute position plus some noise
    left = item.left + poe.left - randint(0, 20)
    top = item.top + poe.top - randint(0, 20)

    pyautogui.moveTo(left, top, 0.08, _pause=False)
    pyautogui.keyDown('ctrl')
    pyautogui.click()
    pyautogui.keyUp('ctrl')


with mss.mss() as sct:
    # The screen part to capture
    region = {"top": poe.top, "left": poe.left, "width": poe.width, "height": poe.height}
    # Grab the data
    sct_img = sct.grab(region)
    # Create the Image in PIL format
    screenshot = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
    for img_highlight in img_highlight_needles:
        items = list(pyautogui.locateAll(img_highlight, screenshot))
        click_items(items)
