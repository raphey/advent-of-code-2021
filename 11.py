from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from utils.utils_25 import get_eight_neighbor_indices
from inputs.input_11 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter


sample_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = [int(x) for x in raw_item]
        parsed.append(parsed_item)
    return parsed


def generate_grid_ij(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            yield i, j


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
    if i > 0 and j > 0:
        neighbors += [(i - 1, j - 1)]
    if i > 0 and j < len(grid[0]) - 1:
        neighbors += [(i - 1, j + 1)]
    if i < len(grid) - 1 and j > 0:
        neighbors += [(i + 1, j - 1)]
    if i < len(grid) - 1 and j < len(grid[0]) - 1:
        neighbors += [(i + 1, j + 1)]
    return neighbors


def part_1(raw_input):
    octo_grid = get_parsed(raw_input)
    flashes = 0
    for k in range(100):
        flash_queue = []
        flash_queued = set()

        for i, j in generate_grid_ij(octo_grid):
            octo_grid[i][j] += 1

        for i, j in generate_grid_ij(octo_grid):
            if octo_grid[i][j] > 9:
                assert(octo_grid[i][j] == 10)
                flash_queue.append((i, j))
                flash_queued.add((i, j))

        while flash_queue:
            flash_i, flash_j = flash_queue.pop()
            flashes += 1
            for i, j in get_eight_neighbor_indices(octo_grid, flash_i, flash_j):
                octo_grid[i][j] += 1
                if octo_grid[i][j] > 9 and (i, j) not in flash_queued:
                    flash_queue.append((i, j))
                    flash_queued.add((i, j))

        for i, j in flash_queued:
            octo_grid[i][j] = 0

        print(k, flashes)
        for row in octo_grid:
            print(''.join(str(x) for x in row))

        if all(octo_grid[i][j] == 0 for i, j in generate_grid_ij(octo_grid)):
            print(k)
            quit()

    print(f'Part1: {flashes}')


def part_2(raw_input):
    octo_grid = get_parsed(raw_input)
    flashes = 0
    for k in range(10**8):
        flash_queue = []
        flash_queued = set()

        for i, j in generate_grid_ij(octo_grid):
            octo_grid[i][j] += 1

        for i, j in generate_grid_ij(octo_grid):
            if octo_grid[i][j] > 9:
                assert(octo_grid[i][j] == 10)
                flash_queue.append((i, j))
                flash_queued.add((i, j))

        while flash_queue:
            flash_i, flash_j = flash_queue.pop()
            flashes += 1
            for i, j in get_eight_neighbor_indices(octo_grid, flash_i, flash_j):
                octo_grid[i][j] += 1
                if octo_grid[i][j] > 9 and (i, j) not in flash_queued:
                    flash_queue.append((i, j))
                    flash_queued.add((i, j))

        for i, j in flash_queued:
            octo_grid[i][j] = 0

        print(k, flashes)
        for row in octo_grid:
            print(''.join(str(x) for x in row))

        if all(octo_grid[i][j] == 0 for i, j in generate_grid_ij(octo_grid)):
            print(k)
            break
    print(f'Part2: {k+1}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
