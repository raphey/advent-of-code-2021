from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_25 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter, defaultdict


sample_input = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = raw_item
        parsed.append(parsed_item)
    return parsed


def get_right_and_down_cucumber_sets(input_map):
    right_cucumbers = set()
    down_cucumbers = set()
    for i in range(len(input_map)):
        for j in range(len(input_map[0])):
            if input_map[i][j] == '>':
                right_cucumbers.add((i, j))
            elif input_map[i][j] == 'v':
                down_cucumbers.add((i, j))
    return right_cucumbers, down_cucumbers


def pprint(rs, ds, h, w):
    print()
    for i in range(h):
        row_str = ''
        for j in range(w):
            if (i, j) in rs:
                row_str += '>'
            elif (i, j) in ds:
                row_str += 'v'
            else:
                row_str += '.'
        print(row_str)

def part_1(raw_input):
    initial_map = get_parsed(raw_input)
    rc, dc = get_right_and_down_cucumber_sets(initial_map)
    h = len(initial_map)
    w = len(initial_map[0])
    for k in range(10**6):
        if k % 1000 == 0:
            print(k)
        # pprint(rc, dc, h, w)
        new_rc = set()
        new_dc = set()
        for i, j in rc:
            new_i, new_j = i, (j + 1) % w
            # print(i, j, new_i, new_j)
            # if not any(((new_i, new_j) in s) for s in (rc, dc, new_rc, new_dc)):
            if ((new_i, new_j) not in rc) and ((new_i, new_j) not in dc) and ((new_i, new_j) not in new_rc) and ((new_i, new_j) not in new_dc):
                new_rc.add((new_i, new_j))
            else:
                new_rc.add((i, j))
        for i, j in dc:
            new_i, new_j = (i + 1) % h, j
            # if not any(((new_i, new_j) in s) for s in (dc, new_rc, new_dc)):
            if ((new_i, new_j) not in dc) and ((new_i, new_j) not in new_rc) and ((new_i, new_j) not in new_dc):
                new_dc.add((new_i, new_j))
            else:
                new_dc.add((i, j))
        if new_rc == rc and new_dc == dc:
            print("stable")
            break
        dc = new_dc
        rc = new_rc

    answer = k + 1
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    answer = 0
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
