#!/usr/bin/python3
from subprocess import Popen, PIPE

top_left_x = None
top_left_y = None
width = None
height = None

def line_have_coords(line):
    return "Absolute upper-left X" in line \
        or "Absolute upper-left Y" in line \
        or "Width:" in line \
        or "Height:" in line

def parse_geometry(str):
    return [int(s) for s in str.split() if s.isdigit()][0]

win_info_stdout = Popen(['xwininfo', '-name', 'Path of Exile'], universal_newlines=True, stdout=PIPE)

for line in win_info_stdout.stdout:
    if "Absolute upper-left X" in line:
        top_left_x = parse_geometry(line)
    if "Absolute upper-left Y" in line:
        top_left_y = parse_geometry(line)
    if "Width:" in line:
        width = parse_geometry(line)
    if "Height:" in line:
        height = parse_geometry(line)

# print("Game window coordinates:")
# print("top_left_x: ", top_left_x)
# print("top_left_y: ", top_left_y)
# print("width: ", width)
# print("height: ", height)


