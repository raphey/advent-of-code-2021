from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_06 import main_input

from itertools import combinations
import copy
import re
from collections import Counter


sample_input = """3,4,3,1,2"""


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = [int(x) for x in raw_item.split(',')]
        parsed.append(parsed_item)
    return parsed[0]


def part_1(raw_input):
    parsed = get_parsed(raw_input)
    # print(parsed)
    for i in range(80):
        length = len(parsed)
        for j in range(length):
            if parsed[j] >= 1:
                parsed[j] -= 1
            else:
                parsed[j] = 6
                parsed.append(8)
        # print(parsed)
    answer = len(parsed)
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    # print(parsed)
    fish_dict = {}
    for x in parsed:
        if x in fish_dict:
            fish_dict[x] += 1
        else:
            fish_dict[x] = 1

    for i in range(256):
        new_dict = {x:0 for x in range(9)}
        for j in range(9):
            if j not in fish_dict:
                continue
            if j == 0:
                new_dict[8] += fish_dict[j]
                new_dict[6] += fish_dict[j]
            else:
                new_dict[j - 1] += fish_dict[j]
        fish_dict = new_dict
    answer = sum(fish_dict.values())
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)


