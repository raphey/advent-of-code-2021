from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_14 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter, defaultdict


sample_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def get_parsed(raw_input):
    parsed = []
    start_string = ""
    for i, raw_item in enumerate(get_raw_items(raw_input, split_token='\n')):
        if i == 0:
            start_string = raw_item
        elif i > 1:
            parsed_item = raw_item.split(' -> ')
            parsed.append(parsed_item)
    return start_string, dict(parsed)


def part_1(raw_input):
    current_string, insertion_dict = get_parsed(raw_input)
    # print(current_string, insertion_dict)
    n = 10
    for i in range(1, n + 1):
        new_string = current_string[0]
        for j in range(len(current_string) - 1):
            pair = current_string[j:j + 2]
            to_insert = insertion_dict[pair]
            new_string += to_insert + pair[1]
        current_string = new_string
        # print(i, len(current_string), current_string)
    counts = Counter(current_string).values()
    # print(Counter(current_string))
    answer = max(counts) - min(counts)
    print(f'Part1: {answer}')


def part_2(raw_input):
    current_string, insertion_dict = get_parsed(raw_input)
    first_char, last_char = current_string[0], current_string[-1]
    modified_insertion_dict = {k: (k[0] + v, v + k[1]) for k, v in insertion_dict.items()}
    # print(modified_insertion_dict)
    counter = defaultdict(int)
    for c1, c2 in zip(current_string, current_string[1:]):
        counter[c1 + c2] += 1
    n = 40
    for i in range(1, n + 1):
        new_counter = defaultdict(int)
        for k, v in counter.items():
            p1, p2 = modified_insertion_dict[k]
            new_counter[p1] += v
            new_counter[p2] += v
        counter = new_counter
    # print(counter)
    letter_count_dict = defaultdict(int)
    for k, v in counter.items():
        # print(k)
        letter_count_dict[k[0]] += v
        letter_count_dict[k[1]] += v
        # print(letter_count_dict)
    letter_count_dict[first_char] += 1
    letter_count_dict[last_char] += 1
    # Every character double counted
    letter_counts = letter_count_dict.values()
    # print(letter_counts)
    # print(max(letter_counts))
    # print(min(letter_counts))
    answer = (max(letter_counts) - min(letter_counts)) // 2
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
