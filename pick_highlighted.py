#!/usr/bin/python3
import pyautogui
import pynput
from pynput.keyboard import Key, Listener as KeyboardListener
import glob

highlight_path = './img/highlight/*.png'
img_highlight_needles = glob.glob(highlight_path, recursive=False)
screenshot = pyautogui.screenshot()

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
    pyautogui.moveTo(item.left, item.top)
    pyautogui.keyDown('ctrl')
    pyautogui.click()
    pyautogui.keyUp('ctrl')

for img_highlight in img_highlight_needles:
    items = list(pyautogui.locateAll(img_highlight, screenshot))
    click_items(items)

