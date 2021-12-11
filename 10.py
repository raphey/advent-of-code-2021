from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_10 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter


sample_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = raw_item
        parsed.append(parsed_item)
    return parsed


openers = "([{<"
closers = ")]}>"
points = [3, 57, 1197, 25137]
points_pt_2 = [1, 2, 3, 4]

def part_1(raw_input):
    parsed = get_parsed(raw_input)
    answer = 0
    for row in parsed:
        to_close = "s"
        for i, c in enumerate(row):
            if c in openers:
                to_close += closers[openers.index(c)]
            elif c in closers:
                if to_close[-1] != c:
                    answer += points[closers.index(c)]
                    break
                else:
                    to_close = to_close[:-1]


    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    scores = []
    for row in parsed:
        to_close = "s"
        invalid = False
        for i, c in enumerate(row):
            if c in openers:
                to_close += closers[openers.index(c)]
            elif c in closers:
                if to_close[-1] != c:
                    invalid = True
                    break
                else:
                    to_close = to_close[:-1]
            if len(to_close) == 1:
                continue
        if invalid:
            continue
        score = 0
        for c in to_close[:0:-1]:
            score *= 5
            score += points_pt_2[closers.index(c)]
        scores += [score]
    scores.sort()
    answer = scores[len(scores) // 2]
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
