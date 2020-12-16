from utils.utils_14 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_14 import GameConsole, TweakedGameConsole, memo
from inputs.input_14 import main_input

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


sample_input_0 = [0,3,6]

# sample_input_1 = """"""

main_input = [12,1,16,3,11,0]


def part_1(raw_input, target=2020):
    spoken = raw_input
    history_dict_1 = {}
    history_dict_2 = {}
    for i, x in enumerate(spoken):
        history_dict_1[x] = i   # no duplicates in input

    for i in range(len(raw_input), target):
        last = spoken[-1]
        if last not in history_dict_2:
            y = 0
        else:
            y = history_dict_1[last] - history_dict_2[last]
        if y in history_dict_1:
            history_dict_2[y] = history_dict_1[y]
        history_dict_1[y] = i
        spoken.append(y)

    answer = spoken[-1]
    print(f'Part1: {answer}')
    print(len(history_dict_1))
    print(len(history_dict_2))


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    for x in parsed:
        pass
    answer = 0
    print(f'Part2: {answer}')


part_1(sample_input_0)
part_1(main_input)
part_1(main_input, 30000000)

# part_2(sample_input_0)
# part_2(main_input)
