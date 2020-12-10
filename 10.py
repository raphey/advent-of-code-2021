from utils.utils_10 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_10 import GameConsole, TweakedGameConsole
from inputs.input_10 import main_input

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
    sorted_parsed = sorted(parsed)
    sorted_parsed = [0] + sorted_parsed + [sorted_parsed[-1] + 3]
    ones = 0
    threes = 0
    for i in range(len(sorted_parsed) - 1):
        if sorted_parsed[i + 1] - sorted_parsed[i] == 1:
            ones += 1
        elif sorted_parsed[i + 1] - sorted_parsed[i] == 3:
            threes += 1
        else:
            print(sorted_parsed[i-1:i+2])
            quit()
    answer = ones * threes
    print(ones, threes)
    print(f'Part1: {answer}')


sample_input_2 = sample_input_1


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    sorted_parsed = sorted(parsed)
    sorted_parsed = [0] + sorted_parsed + [sorted_parsed[-1] + 3]
    adapter_bools = [i in sorted_parsed for i in range(sorted_parsed[-1])]
    rec_memo = {}
    def rec(target):
        if target == 0:
            return 1
        if target in rec_memo:
            return rec_memo[target]
        count = 0
        for i in range(1, 4):
            if adapter_bools[target - i]:
                count += rec(target - i)
        rec_memo[target] = count
        return count

    answer = rec(sorted_parsed[-1])
    print(f'Part2: {answer}')


# part_1(sample_input_0)
# part_1(main_input)

part_2(sample_input_0)
part_2(main_input)
