from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo, get_four_neighbor_indices
from inputs.input_15 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter
import heapq


sample_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = [int(x) for x in raw_item]
        parsed.append(parsed_item)
    return parsed


def part_1(raw_input):
    risk_grid = get_parsed(raw_input)
    initial_state = (0, 0, 0)   # cost, i, j
    visited = {(0, 0)}
    to_explore = [initial_state]
    heapq.heapify(to_explore)
    answer = None
    while len(to_explore) != 0:
        current_state = heapq.heappop(to_explore)
        cost, current_i, current_j = current_state
        if current_i == len(risk_grid) - 1 and current_j == len(risk_grid[0]) - 1:
            answer = cost
            break
        for i, j in get_four_neighbor_indices(risk_grid, current_i, current_j):
            if (i, j) not in visited:
                visited.add((i, j))
                new_state = (cost + risk_grid[i][j], i, j)
                heapq.heappush(to_explore, new_state)
    print(f'Part1: {answer}')


def part_2(raw_input):
    seed_risk_grid = get_parsed(raw_input)
    h, w = len(seed_risk_grid), len(seed_risk_grid[0])
    risk_grid = [[0] * 5 * w for _ in range(5 * h)]
    for i in range(len(risk_grid)):
        for j in range(len(risk_grid[0])):
            new_risk = seed_risk_grid[i % h][j % w] + (i // h) + (j // w)
            new_risk = ((new_risk - 1) % 9) + 1
            risk_grid[i][j] = new_risk
    # for row in risk_grid:
    #     print(''.join(str(x) for x in row))
    # print()
    initial_state = (0, 0, 0)   # cost, i, j
    visited = {(0, 0)}
    to_explore = [initial_state]
    heapq.heapify(to_explore)
    answer = None
    while len(to_explore) != 0:
        current_state = heapq.heappop(to_explore)
        cost, current_i, current_j = current_state
        if current_i == len(risk_grid) - 1 and current_j == len(risk_grid[0]) - 1:
            answer = cost
            break
        for i, j in get_four_neighbor_indices(risk_grid, current_i, current_j):
            if (i, j) not in visited:
                visited.add((i, j))
                new_state = (cost + risk_grid[i][j], i, j)
                heapq.heappush(to_explore, new_state)
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
