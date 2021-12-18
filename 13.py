from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_13 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter


sample_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def get_parsed(raw_input):
    coords, directions = get_raw_items(raw_input, split_token='\n\n')
    parsed_coords = []
    parsed_directions = []
    for line in coords.split('\n'):
        x_str, y_str = line.split(',')
        parsed_coords.append((int(x_str), int(y_str)))
    for line in directions.split('\n'):
        q, r = line.split()[-1].split('=')
        parsed_directions.append((q, int(r)))
    return parsed_coords, parsed_directions


def apply_fold(paper, fold):
    fold_axis, fold_value = fold
    if fold_axis == "y":
        print('in here')
        new_paper = [[0] * len(paper[0]) for _ in range(fold_value)]
        print('qwer')
        for row in new_paper:
            print(''.join(str(x) for x in row))
        for i in range(0, fold_value):
            for j in range(len(paper[0])):
                new_paper[i][j] = paper[i][j]
        print('tyuiop')
        for row in new_paper:
            print(''.join(str(x) for x in row))
        for i in range(1, len(paper) - fold_value):
            for j in range(len(paper[0])):
                new_paper[fold_value - i][j] = max(new_paper[fold_value - i][j], paper[fold_value + i][j])
        return new_paper

    if fold_axis == "x":
        new_paper = [[0] * fold_value for _ in range(len(paper))]
        for i in range(len(paper)):
            for j in range(fold_value):
                new_paper[i][j] = paper[i][j]

            for j in range(1, len(paper[0]) - fold_value):
                new_paper[i][fold_value - j] = max(new_paper[i][fold_value - j], paper[i][fold_value + j])
        return new_paper


def part_1(raw_input):
    coords, directions = get_parsed(raw_input)
    max_x = max(x for x, _ in coords)
    max_y = max(y for _, y in coords)
    paper = [[0] * (max_x + 1) for _ in range(max_y + 1)]
    for x, y in coords:
        paper[y][x] = 1

    for row in paper:
        print(''.join(str(x) for x in row))

    for fold in directions[:1]:
        paper = apply_fold(paper, fold)
        print()
        for row in paper:
            print(''.join(str(x) for x in row))

    answer = sum(x for line in paper for x in line)
    print(f'Part1: {answer}')


def part_2(raw_input):
    coords, directions = get_parsed(raw_input)
    max_x = max(x for x, _ in coords)
    max_y = max(y for _, y in coords)
    paper = [[0] * (max_x + 1) for _ in range(max_y + 1)]
    for x, y in coords:
        paper[y][x] = 1

    for row in paper:
        print(''.join(str(x) for x in row))

    for fold in directions:
        paper = apply_fold(paper, fold)
        print()
        for row in paper:
            print(''.join(str(x) for x in row))

    for row in paper:
        print(''.join(str(x) for x in row).replace('0', ' ').replace('1', '$'))

part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
