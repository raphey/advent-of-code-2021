from utils.utils_09 import gen_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_09 import GameConsole, TweakedGameConsole
from inputs.input_09 import main_input

from itertools import combinations
import re


def gen_parsed(raw_input):
    for raw_item in gen_raw_items(raw_input, split_token='\n'):
        yield int(raw_item)


def part_1(raw_input, preamble=5):
    all_numbers = list(gen_parsed(raw_input))
    for i in range(preamble, len(all_numbers)):
        x = all_numbers[i]
        if x not in [a + b for a, b in combinations(all_numbers[i-preamble:i], 2)]:
            answer = x
            break
    print(f'Part1: {answer}')


def part_2(raw_input, target=127):
    all_numbers = list(gen_parsed(raw_input))
    for q in range(2, 50):
        for i in range(len(all_numbers) - (q - 1)):
            if sum(all_numbers[i:i+q]) == target:
                answer = min(all_numbers[i:i+q]) + max(all_numbers[i:i+q])
    print(f'Part2: {answer}')


sample_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


part_1(sample_input)
part_1(main_input, 25)


sample_input_2 = sample_input

part_2(sample_input_2)
part_2(main_input, 675280050)
