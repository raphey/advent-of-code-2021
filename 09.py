from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_09 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter


sample_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = [int(x) for x in raw_item]
        parsed.append(parsed_item)
    return parsed


def get_neighbors(grid, i, j):
    neighbors = []
    if i > 0:
        neighbors += [grid[i - 1][j]]
    if i < len(grid) - 1:
        neighbors += [grid[i + 1][j]]
    if j > 0:
        neighbors += [grid[i][j - 1]]
    if j < len(grid[0]) - 1:
        neighbors += [grid[i][j + 1]]
    return neighbors


def get_neighbor_indices(grid, i, j):
    neighbors = []
    if i > 0:
        neighbors += [(i - 1, j)]
    if i < len(grid) - 1:
        neighbors += [(i + 1, j)]
    if j > 0:
        neighbors += [(i, j - 1)]
    if j < len(grid[0]) - 1:
        neighbors += [(i, j + 1)]
    return neighbors


def part_1(raw_input):
    parsed = get_parsed(raw_input)
    answer = 0
    for i in range(len(parsed)):
        for j in range(len(parsed[0])):
            value = parsed[i][j]
            if all(neighbor > value for neighbor in get_neighbors(parsed, i, j)):
                print ('low point')
                answer += (1 + value)
    print(f'Part1: {answer}')


def get_basin(grid, lp):
    basin = set()
    to_explore = [lp]
    explored = set()
    while to_explore:
        ii, jj = to_explore.pop()
        basin.add((ii, jj))
        explored.add((ii, jj))
        value = grid[ii][jj]
        successors = [(i, j) for i, j in get_neighbor_indices(grid, ii, jj) if 9 > grid[i][j] > value]
        for s in successors:
            if s not in explored:
                to_explore.append(s)
    return basin


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    low_points = []
    for i in range(len(parsed)):
        for j in range(len(parsed[0])):
            value = parsed[i][j]
            if all(neighbor > value for neighbor in get_neighbors(parsed, i, j)):
                low_points.append((i, j))
    basins = []
    for lp in low_points:
        basins.append(get_basin(parsed, lp))
    print(basins)
    basins.sort(key=len)
    basins.reverse()
    answer = 1
    print(basins)
    for b in basins[:3]:
        answer *= len(b)
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
