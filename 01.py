from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_01 import main_input

from itertools import combinations
import copy
import re
from collections import Counter


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = int(raw_item)
        parsed.append(parsed_item)
    return parsed


sample_input = """199
200
208
210
200
207
240
269
260
263"""


def part_1(raw_input):
    parsed = get_parsed(raw_input)
    answer = 0
    for i in range(1, len(parsed)):
        if parsed[i] > parsed[i - 1]:
            answer += 1
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    answer = 0
    for i in range(1, len(parsed) - 2):
        if parsed[i] + parsed[i + 1] + parsed[i + 2] > parsed[i - 1] + parsed[i] + parsed[i + 1]:
            answer += 1
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)


