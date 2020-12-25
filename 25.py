from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import GameConsole, TweakedGameConsole, memo
from inputs.input_25 import main_input

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


sample_input_0 = [5764801, 17807724]


main_input = [12578151, 5051300]

sample_input_1 = """"""


def generate_transformed_subject_numbers(sn):
    val = 1
    while True:
        val *= sn
        val %= 20201227
        yield val


def get_transformed_subject_number(sn, loop_size):
    val = 1
    for _ in range(loop_size):
        val *= sn
        val %= 20201227
    return val


def part_1(raw_input):
    card_pk, door_pk = raw_input
    for i, t in enumerate(generate_transformed_subject_numbers(7)):
        if t == card_pk:
            card_loop = i + 1
            break
        if i > 1000000:
            raise ValueError('Too much card loop iteration')

    for i, t in enumerate(generate_transformed_subject_numbers(7)):
        if t == door_pk:
            door_loop = i + 1
            break
        if i > 10000000:
            raise ValueError('Too much door loop iteration')
    answer = get_transformed_subject_number(door_pk, card_loop)
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    for x in parsed:
        pass
    answer = 0
    print(f'Part2: {answer}')

part_1(sample_input_0)
part_1(main_input)

# part_2(sample_input_0)
# part_2(main_input)
