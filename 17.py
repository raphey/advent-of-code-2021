from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
# from inputs.input_17 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter


sample_input =(20,30,-10,-5)
main_input = (236,262,-78,-58)


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = raw_item
        parsed.append(parsed_item)
    return parsed


def update_probe(x, y, vx, vy):
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    vy -= 1
    return x, y, vx, vy


def try_shot(vx0, vy0, x_min, x_max, y_min, y_max):
    max_height = 0
    x, y = 0, 0
    vx, vy = vx0, vy0
    hit = False
    while x <= x_max:
        x, y, vx, vy = update_probe(x, y, vx, vy)
        max_height = max(y, max_height)
        if (x_min <= x <= x_max) and (y_min <= y <= y_max):
            hit = True
    return hit, max_height


def part_1(raw_input):
    def try_shot(vx0, vy0):
        max_height = 0
        x, y = 0, 0
        vx, vy = vx0, vy0
        hit = False
        while x <= x_max and y > y_min:
            x, y, vx, vy = update_probe(x, y, vx, vy)
            max_height = max(y, max_height)
            if (x_min <= x <= x_max) and (y_min <= y <= y_max):
                hit = True
        return hit, max_height

    x_min, x_max, y_min, y_max = raw_input
    mmh = 0
    counter = 0
    for vx0 in range(1, 1000):
        for vy0 in range(1, 1000):
            hit, mh = try_shot(vx0, vy0)
            if hit:
                mmh = max(mmh, mh)
    answer = mmh
    print(f'Part1: {answer}')


def part_2(raw_input):
    def try_shot(vx0, vy0):
        max_height = 0
        x, y = 0, 0
        vx, vy = vx0, vy0
        hit = False
        while x <= x_max and y > y_min:
            x, y, vx, vy = update_probe(x, y, vx, vy)
            max_height = max(y, max_height)
            if (x_min <= x <= x_max) and (y_min <= y <= y_max):
                hit = True
        return hit, max_height

    x_min, x_max, y_min, y_max = raw_input
    mmh = 0
    counter = 0
    for vx0 in range(1, 3000):
        for vy0 in range(-1000, 3000):
            hit, mh = try_shot(vx0, vy0)
            if hit:
                counter += 1
                mmh = max(mmh, mh)
    answer = counter
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
