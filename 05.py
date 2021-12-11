from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_05 import main_input

from itertools import combinations
import copy
import re
from collections import Counter


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = get_regex_search(raw_item, r"(\d+),(\d+) -> (\d+),(\d+)")
        # intermediate_parsed_item = raw_item.split()
        # print(parsed_item)
        # parsed_item = intermediate_parsed_item[0].split(',') + intermediate_parsed_item[2].split(',')
        parsed.append(tuple(int(x) for x in parsed_item))
    return parsed


sample_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def apply_to_grid(grid, a, b, c, d):
    print('(******')
    print(a, b, c, d)
    if a == c:
        for j in range(b, d + 1):
            grid[a][j] += 1
    elif b == d:
        for i in range(a, c + 1):
            grid[i][b] += 1
    else:
        print(a, b, c, d)
    # for row in grid:
    #     print(row)


def apply_to_grid_2(grid, a, b, c, d):
    print('(******')
    print(a, b, c, d)
    if a == c:
        delta_x = 0
    elif a > c:
        delta_x = -1
    else:
        delta_x = 1
    if b == d:
        delta_y = 0
    elif b > d:
        delta_y = -1
    else:
        delta_y = 1

    i, j = a, b
    grid[i][j] += 1
    while not (i == c and j == d):
        i += delta_x
        j += delta_y
        grid[i][j] += 1


def part_1(raw_input):
    parsed = get_parsed(raw_input)
    answer = 0
    max_row = max(max(a, c) for a, _, c, _ in parsed)
    max_col = max(max(b, d) for a, b, c, d in parsed)
    grid = [[0] * (max_col + 1) for _ in range(max_row + 1)]
    print(max_row, max_col)
    for a, b, c, d in parsed:
        if a > c:
            a, c = c, a
        if b > d:
            b, d = d, b
        print(a, b, c, d)
        apply_to_grid(grid, a, b, c, d)
    # for row in grid:
    #     print(row)
    answer = 0
    for row in grid:
        for cell in row:
            if cell >= 2:
                answer += 1
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    answer = 0
    max_row = max(max(a, c) for a, _, c, _ in parsed)
    max_col = max(max(b, d) for a, b, c, d in parsed)
    grid = [[0] * (max_col + 1) for _ in range(max_row + 1)]
    print(max_row, max_col)
    for a, b, c, d in parsed:
        print(a, b, c, d)
        apply_to_grid_2(grid, a, b, c, d)
    # for row in grid:
    #     print(row)
    answer = 0
    for row in grid:
        for cell in row:
            if cell >= 2:
                answer += 1
    print(f'Part2: {answer}')

part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)


