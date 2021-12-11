from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_07 import main_input

from itertools import combinations
import copy
import re
from collections import Counter


sample_input = """16,1,2,0,4,2,7,1,2,14"""


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = [int(x) for x in raw_item.split(',')]
        parsed.append(parsed_item)
    return parsed[0]  # change me


def part_1(raw_input):
    parsed = get_parsed(raw_input)
    print(parsed)
    mean = sum(parsed) / len(parsed)
    midpoint = int(mean)
    minimum_fuel = 10**12
    for i in range(midpoint - 2000, midpoint + 2000):
        fuel_used = sum(abs(x - i) for x in parsed)
        minimum_fuel = min(fuel_used, minimum_fuel)
    answer = minimum_fuel
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    print(parsed)
    mean = sum(parsed) / len(parsed)
    rms = (sum(x**2 for x in parsed) / len(parsed))**0.5
    print(rms)
    midpoint = int(mean)
    minimum_fuel = 10**12
    for i in range(midpoint - 2000, midpoint + 2000):
        fuel_used = sum(abs(x - i) * (abs(x - i) + 1) // 2 for x in parsed)
        minimum_fuel = min(fuel_used, minimum_fuel)
    answer = minimum_fuel
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)


