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
        parsed_item = '(' + raw_item + ')'
        parsed.append(parsed_item)
    return parsed


sample_input_0 = """1 + 2 * 3 + 4 * 5 + 6"""

sample_input_1 = """((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""


def extract_simple_expression(input_str):
    j = input_str.index(')')
    for i in range(j, -1, -1):
        if input_str[i] == '(':
            break
    else:
        raise ValueError(f'failed to get parens for {input_str}')
    return input_str[:i], input_str[i+1:j], input_str[j + 1:]


def eval_simple_str(x):
    chars = x.split()
    current = int(chars[0])
    for i in range(1, len(chars), 2):
        current = eval(str(current) + chars[i] + chars[i + 1])
    return current


def eval_simple_str_2(x):
    to_multiply = [eval_simple_str(y) for y in x.split(' * ')]
    prod = 1
    for z in to_multiply:
        prod *= z
    return prod


def eval_input_str(x):
    while True:
        pre, exp, post = extract_simple_expression(x)
        simple_expression_value = eval_simple_str(exp)
        if not pre:
            return simple_expression_value
        x = pre + str(simple_expression_value) + post


def eval_input_str_2(x):
    while True:
        pre, exp, post = extract_simple_expression(x)
        simple_expression_value = eval_simple_str_2(exp)
        if not pre:
            return simple_expression_value
        x = pre + str(simple_expression_value) + post

def part_1(raw_input):
    parsed = get_parsed(raw_input)
    answer = 0
    for x in parsed:
        answer += eval_input_str(x)
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    answer = 0
    for x in parsed:
        answer += eval_input_str_2(x)
    print(f'Part2: {answer}')


part_1(sample_input_0)
part_1(main_input)

part_2(sample_input_0)
part_2(main_input)
