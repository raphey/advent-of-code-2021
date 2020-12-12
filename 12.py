from utils.utils_12 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_12 import GameConsole, TweakedGameConsole, memo
from inputs.input_12 import main_input

from itertools import combinations
import copy
import re


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = (raw_item[0], int(raw_item[1:]))
        parsed.append(parsed_item)
    return parsed


sample_input_0 = """F10
N3
F7
R90
F11"""

# sample_input_1 = """"""


def part_1(raw_input):
    x = 0
    y = 0
    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    dir_i = 0
    card_dict = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }
    parsed = get_parsed(raw_input)
    for cmd, amt in parsed:
        if cmd in card_dict:
            x += amt * card_dict[cmd][0]
            y += amt * card_dict[cmd][1]
        elif cmd == 'R':
            dir_i = (dir_i + amt // 90) % 4
        elif cmd == 'L':
            dir_i = (dir_i - amt // 90) % 4
        elif cmd == 'F':
            x += amt * dirs[dir_i][0]
            y += amt * dirs[dir_i][1]
    answer = abs(x) + abs(y)
    print(f'Part1: {answer}')


def get_rotated_wps(x, y, wpx, wpy, dir, amt):
    if dir == 'L':
        return get_rotated_wps(x, y, wpx, wpy, 'R', -amt)
    r_turns = (amt // 90) % 4
    if r_turns == 0:
        return wpx, wpy

    if r_turns == 2:
        return -wpx, -wpy
    if r_turns == 1:
        return wpy, -wpx
    if r_turns == 3:
        return -wpy, wpx
    else:
        print(r_turns)


def part_2(raw_input):
    x = 0
    y = 0
    wpx = 10
    wpy = 1
    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    dir_i = 0
    card_dict = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }
    parsed = get_parsed(raw_input)
    for cmd, amt in parsed:
        if cmd in card_dict:
            wpx += amt * card_dict[cmd][0]
            wpy += amt * card_dict[cmd][1]
        elif cmd == 'R':
            wpx, wpy = get_rotated_wps(x, y, wpx, wpy, 'R', amt)
        elif cmd == 'L':
            wpx, wpy = get_rotated_wps(x, y, wpx, wpy, 'L', amt)
        elif cmd == 'F':
            x += amt * wpx
            y += amt * wpy
        print(x, y, wpx, wpy)
    answer = abs(x) + abs(y)
    print(f'Part2: {answer}')


part_1(sample_input_0)
part_1(main_input)

part_2(sample_input_0)
part_2(main_input)
