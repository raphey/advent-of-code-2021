from utils.utils_13 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_13 import GameConsole, TweakedGameConsole, memo
from inputs.input_13 import main_input

from itertools import combinations
import copy
import re


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = raw_item
        parsed.append(parsed_item)
    return parsed


t0 = 1000390
# t0 = 939
bus_input = "13,x,x,41,x,x,x,x,x,x,x,x,x,997,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,619,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17"
# bus_input = "7,13,x,x,59,x,31,19"

buses = [int(b) for b in bus_input.split(',') if b != 'x']


def part_1():
    min_w = float('inf')
    min_b = -1
    for b in buses:
        w = b - (t0 % b)
        if w < min_w:
            min_w = w
            min_b = b
    answer = min_w * min_b
    print(f'Part1: {answer}')


def get_part2_bus_input():
    new_input = []
    for i, b_str in enumerate(bus_input.split(',')):
        try:
            b = int(b_str)
            new_input.append((b, (b - i) % b))
        except ValueError:
            continue
    return new_input


def crt_pair(a, b):
    p1, r1 = a
    p2, r2 = b
    for x in range(r1, p1 * p2 + r1, p1):
        if x % p2 == r2:
            return p1 * p2, x


def part_2():
    buses = get_part2_bus_input()
    current = buses[0]
    for i in range(1, len(buses)):
        current = crt_pair(current, buses[i])
    answer = current[1]
    for p, r in buses:
        assert(answer % p == r % p)
    print(f'Part2: {answer}')


part_1()

part_2()
