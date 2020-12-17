from utils.utils_17 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_17 import GameConsole, TweakedGameConsole, memo
from inputs.input_17 import main_input

from itertools import combinations, product
import copy
import re
from collections import Counter


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed.append([int(c == '#') for c in raw_item])
    return parsed


sample_input_0 = """.#.
..#
###"""

main_input = """.......#
....#...
...###.#
#...###.
....##..
##.#..#.
###.#.#.
....#..."""


sample_input_1 = """"""


def pprint_2d(arr):
    print()
    for row in arr:
        print(row)


@memo
def get_neighbors(i, j, k, i_max, j_max, k_max):
    neighbors = []
    for di, dj, dk in product(*[(-1, 0, 1)] * 3):
        if all(dq == 0 for dq in [di, dj, dk]):
            continue
        ii, jj, kk = i + di, j + dj, k + dk
        if any(q >= q_max for q, q_max in zip([ii, jj, kk], [i_max, j_max, k_max])):
            continue
        if any(q < 0 for q in (ii, jj, kk)):
            continue
        neighbors.append((ii, jj, kk))
    return neighbors


@memo
def get_neighbors_4d(i, j, k, l, i_max, j_max, k_max, l_max):
    neighbors = []
    for di, dj, dk, dl in product(*[(-1, 0, 1)] * 4):
        if all(dq == 0 for dq in [di, dj, dk, dl]):
            continue
        ii, jj, kk, ll = i + di, j + dj, k + dk, l + dl
        if any(q >= q_max for q, q_max in zip([ii, jj, kk, ll], [i_max, j_max, k_max, l_max])):
            continue
        if any(q < 0 for q in (ii, jj, kk, ll)):
            continue
        neighbors.append((ii, jj, kk, ll))
    return neighbors


# print(get_neighbors(2, 3, 4, 10, 10, 10))

def generate_coords(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            for k in range(len(arr[0][0])):
                yield i, j, k


def generate_coords_4d(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            for k in range(len(arr[0][0])):
                for l in range(len(arr[0][0][0])):
                    yield i, j, k, l


def part_1(raw_input):
    parsed = get_parsed(raw_input)
    size = 50
    m = size // 2
    arr = [[[0] * size for _ in range(size)] for _ in range(size)]
    for i in range(len(parsed)):
        for j in range(len(parsed[0])):
            arr[m][m + i][m + j] = parsed[i][j]
    for z in range(6):
        print(z)
        new_arr = copy.deepcopy(arr)
        for i, j, k in generate_coords(arr):
            neighbor_count = sum(arr[ii][jj][kk] for ii, jj, kk in get_neighbors(i, j, k, size, size, size))
            active = arr[i][j][k]
            if active:
                if neighbor_count in (2, 3):
                    new_arr[i][j][k] = 1
                else:
                    new_arr[i][j][k] = 0

            if not active and neighbor_count == 3:
                new_arr[i][j][k] = 1
        arr = new_arr
    answer = sum(arr[i][j][k] for i, j, k in generate_coords(arr))
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    size = 22
    m = size // 2
    arr = [[[[0] * size for _ in range(size)] for _ in range(size)] for _ in range(size)]
    for i in range(len(parsed)):
        for j in range(len(parsed[0])):
            arr[m][m][m - 4 + i][m - 4 + j] = parsed[i][j]
    for z in range(6):
        print(z)
        new_arr = copy.deepcopy(arr)
        for i, j, k, l in generate_coords_4d(arr):
            neighbor_count = sum(arr[ii][jj][kk][ll] for ii, jj, kk, ll in get_neighbors_4d(i, j, k, l, size, size, size, size))
            active = arr[i][j][k][l]
            if active:
                if neighbor_count in (2, 3):
                    new_arr[i][j][k][l] = 1
                else:
                    new_arr[i][j][k][l] = 0

            if not active and neighbor_count == 3:
                new_arr[i][j][k][l] = 1
        arr = new_arr
    answer = sum(arr[i][j][k][l] for i, j, k, l in generate_coords_4d(arr))
    print(f'Part2: {answer}')


# part_1(sample_input_0)
# part_1(main_input)

part_2(sample_input_0)
part_2(main_input)
