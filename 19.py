from utils.utils_18 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_18 import GameConsole, TweakedGameConsole, memo
from inputs.input_18 import main_input

from itertools import combinations
import copy
import re
from collections import Counter


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = raw_item
        parsed.append(parsed_item)
    return parsed


sample_input_0 = """"""

sample_input_1 = """"""


def part_1(raw_input):
    parsed = get_parsed(raw_input)
    for x in parsed:
        pass
    answer = 0
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    for x in parsed:
        pass
    answer = 0
    print(f'Part2: {answer}')

part_1(sample_input_0)
# part_1(main_input)

# part_2(sample_input_1)
# part_2(main_input)
