from utils.utils_10 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_10 import GameConsole, TweakedGameConsole
from utils.utils_11 import memo
from inputs.input_10 import main_input

from collections import Counter
from itertools import combinations
import re


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = int(raw_item)
        parsed.append(parsed_item)
    return parsed


sample_input_0 = """16
10
15
5
1
11
7
19
6
12
4"""

sample_input_1 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


def part_1(raw_input):
    parsed = get_parsed(raw_input)
    sp = sorted(parsed)
    sp = [0] + sp + [sp[-1] + 3]
    diffs = [sp[i] - sp[i - 1] for i in range(1, len(sp))]
    counts = Counter(diffs)
    answer = counts[1] * counts[3]
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    da = max(parsed) + 3
    adapters = set([0] + parsed + [da])

    @memo
    def rec(target):
        if target == 0:
            return 1
        count = 0
        for i in range(1, 4):
            if target - i in adapters:
                count += rec(target - i)
        return count

    answer = rec(da)
    print(f'Part2: {answer}')


part_1(sample_input_0)
part_1(sample_input_1)
part_1(main_input)

part_2(sample_input_0)
part_2(sample_input_1)
part_2(main_input)
