from utils.utils_11 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_11 import GameConsole, TweakedGameConsole, memo
from inputs.input_11 import main_input, final_state

from itertools import combinations
import re
import copy


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = ['.'] + list(raw_item) + ['.']
        parsed.append(parsed_item)
    length = len(parsed[0])
    parsed = [['.'] * length] + parsed + [['.'] * length]
    return parsed


sample_input_0 = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

# sample_input_1 = """"""


def get_neighbor_count(grid, i, j):
    count = 0
    for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        try:
            if grid[i + di][j + dj] == '#':
                count += 1
        except IndexError:
            print(i, j, grid)
            print('oob')
            quit()
    return count


def part_1(raw_input):
    grid = get_parsed(raw_input)
    k = 0
    while True:
        changed = False
        k += 1
        new_grid = copy.deepcopy(grid)
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == '.':
                    continue
                c = get_neighbor_count(grid, i, j)
                if c == 0 and grid[i][j] == 'L':
                    changed = True
                    new_grid[i][j] = '#'
                if c >= 4 and grid[i][j] == '#':
                    changed = True
                    new_grid[i][j] = 'L'
        if changed == False:
            answer = 0
            for row in grid:
                answer += sum(1 for s in row if s == '#')
                print(''.join(row))
            break
        grid = new_grid
    print(f'Part1: {answer}')


def get_neighbor_count_2(grid, i, j):
    count = 0
    for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        for m in range(1, 2 * len(grid)):
            if i + m * di < 0 or j + m * dj < 0:
                break
            try:
                if grid[i + m * di][j + m * dj] == '#':
                    count += 1
                    break
                elif grid[i + m * di][j + m * dj] == 'L':
                    break
            except IndexError:
                break
    return count


def part_2(raw_input):
    grid = get_parsed(raw_input)
    k = 0
    while True:
        changed = False
        k += 1
        print(k)
        new_grid = copy.deepcopy(grid)
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == '.':
                    continue
                c = get_neighbor_count_2(grid, i, j)
                if c == 0 and grid[i][j] == 'L':
                    changed = True
                    new_grid[i][j] = '#'
                if c >= 5 and grid[i][j] == '#':
                    changed = True
                    new_grid[i][j] = 'L'
        print()
        for row in grid:
            print(''.join(row))
        if changed == False:
            answer = 0
            for row in grid:
                answer += sum(1 for s in row if s == '#')
                print(''.join(row))
            break
        grid = new_grid
    print(f'Part2: {answer}')


# part_1(sample_input_0)
# part_1(main_input)
# part_1(final_state)

part_2(sample_input_0)

part_2(main_input)
