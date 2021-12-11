from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_03 import main_input

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


sample_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def part_1(raw_input):
    parsed = get_parsed(raw_input)
    master_bits = ""
    alt_bits = ""
    for i in range(len(parsed[0])):
        zero_count = 0
        one_count = 0
        for x in parsed:
            if x[i] == "0":
                zero_count += 1
            elif x[i] == "1":
                one_count += 1
            else:
                raise ValueError(x)
        if zero_count > one_count:
            master_bits += "0"
            alt_bits += "1"
        else:
            master_bits += "1"
            alt_bits += "0"
    gamma = int(master_bits, 2)
    epsilon = int(alt_bits, 2)
    answer = epsilon * gamma
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)

    filtered = list(parsed)
    for i in range(len(parsed[0])):
        zero_count = 0
        one_count = 0
        for x in filtered:
            if x[i] == "0":
                zero_count += 1
            elif x[i] == "1":
                one_count += 1
            else:
                raise ValueError(x)
        if zero_count == one_count:
            filtered = [x for x in filtered if x[i] == "1"]
        elif zero_count > one_count:
            filtered = [x for x in filtered if x[i] == "0"]
        else:
            filtered = [x for x in filtered if x[i] == "1"]
        if len(filtered) == 1:
            break
    print(filtered)
    o2 = int(filtered[0], 2)
    filtered = list(parsed)
    for i in range(len(parsed[0])):
        master_bits = ""
        alt_bits = ""
        zero_count = 0
        one_count = 0
        for x in filtered:
            if x[i] == "0":
                zero_count += 1
            elif x[i] == "1":
                one_count += 1
            else:
                raise ValueError(x)
        if zero_count == one_count:
            filtered = [x for x in filtered if x[i] == "0"]
        elif zero_count > one_count:
            filtered = [x for x in filtered if x[i] == "1"]
        else:
            filtered = [x for x in filtered if x[i] == "0"]
        if len(filtered) == 1:
            break
    print(filtered)
    co2 = int(filtered[0], 2)
    answer = o2 * co2
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)


