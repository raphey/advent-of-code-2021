from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_02 import main_input

from itertools import combinations
import copy
import re
from collections import Counter


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        dir_str, amt_str = raw_item.split()
        parsed.append((dir_str, int(amt_str)))
    return parsed


sample_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def part_1(raw_input):
    parsed = get_parsed(raw_input)
    depth = 0
    fwd = 0
    for dir, amt in parsed:
        if dir == "forward":
            fwd += amt
        elif dir == "down":
            depth += amt
        elif dir == "up":
            depth -= amt
        else:
            raise ValueError((dir, amt))
    answer = depth * fwd
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    aim = 0
    depth = 0
    fwd = 0
    for dir, amt in parsed:
        if dir == "forward":
            fwd += amt
            depth += aim * amt
        elif dir == "down":
            aim += amt
        elif dir == "up":
            aim -= amt
        else:
            raise ValueError((dir, amt))
    answer = depth * fwd
    print(f'Part1: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)


