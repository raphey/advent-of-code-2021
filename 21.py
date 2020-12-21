from utils.utils_20 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_20 import GameConsole, TweakedGameConsole, memo
from inputs.input_20 import main_input

from itertools import combinations
import copy
import re
from collections import Counter



class SolutionPathFinder(object):
    """
    taken from the projecteuler library I made
    """
    def __init__(self, initial_states, successor_fn, is_goal_fn, is_goal_impossible_fn=lambda x: False):
        self.states_to_explore = initial_states
        self.successor_fn = successor_fn
        self.is_goal_fn = is_goal_fn
        self.is_goal_impossible_fn = is_goal_impossible_fn
        self.states_explored_count = None

    def find_solution(self):
        i = 0
        while i < len(self.states_to_explore):
            # if i % 10000 == 0:
            #     print(i)
            popped_state = self.states_to_explore[i]
            # print(popped_state)
            i += 1
            self.states_explored_count = i
            if self.is_goal_fn(popped_state):
                return popped_state
            if self.is_goal_impossible_fn(popped_state):
                continue
            for successor_state in self.successor_fn(popped_state):
                self.states_to_explore.append(successor_state)
        return 'no solution'


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n\n'):
        tile_lines = get_raw_items(raw_item, split_token='\n')
        tile_num = int(get_regex_search(tile_lines[0], r'\w+ (\d+):')[0])
        tile = tuple(tile_lines[1:])
        parsed.append((tile_num, tile))
    return parsed


sample_input_0 = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""

sample_input_1 = """"""


@memo
def get_rotated_tile(tile, num_rot):
    if num_rot == 0:
        return tile
    s = len(tile)
    assert(s == len(tile[0]))
    current_tile = tile
    for _ in range(num_rot, 0, -1):
        new_tile = []
        for i in range(s):
            new_row = ''.join(list(zip(*current_tile))[i])[::-1]
            new_tile.append(new_row)
        current_tile = tuple(new_tile)
    return current_tile


def get_horizontally_flipped_tile(tile):
    return tuple(row[::-1] for row in tile)


def get_all_eight_tiles(tile):
    return ([get_rotated_tile(tile, i) for i in range(4)] +
            [get_rotated_tile(get_horizontally_flipped_tile(tile), i) for i in range(4)])


def get_right_match_guide(tiles):
    guide = []
    for i, t in enumerate(tiles):
        matches = []
        for j, u in enumerate(tiles):
            if t[0] == u[0]:
                continue
            if all(t[1][k][-1] == u[1][k][0] for k in range(len(t[1]))):
                matches.append(j)
        guide.append(matches)
    return guide


def get_down_match_guide(tiles):
    guide = []
    for i, t in enumerate(tiles):
        matches = []
        for j, u in enumerate(tiles):
            if t[0] == u[0]:
                continue
            if t[1][-1] == u[1][0]:
                matches.append(j)
        guide.append(matches)
    return guide


def get_same_id_guide(tiles):
    guide = []
    for i, t in enumerate(tiles):
        matches = []
        for j, u in enumerate(tiles):
            if t[0] == u[0]:
                matches.append(j)
        guide.append(matches)
    return guide


def pprint(tile):
    print('\n'.join(tile))
    print()


sm = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
]


sm_w = len(sm[0])
sm_h = len(sm)


def sm_squares():
    for i in range(len(sm)):
        for j in range(len(sm[0])):
            if sm[i][j] == '#':
                yield i, j


def part_1(raw_input):
    def get_successors(state):
        if not state:
            return [(i,) for i in range(len(all_tiles))]
        if len(state) < s:
            return [state + (i,) for i in right_match_guide[state[-1]]
                    if not any(i in same_id_guide[j] for j in state)]
        if len(state) % s == 0:
            return [state + (i,) for i in down_match_guide[state[-s]]
                    if not any(i in same_id_guide[j] for j in state)]
        return [state + (i,) for i in right_match_guide[state[-1]]
                if i in down_match_guide[state[-s]]
                if not any(i in same_id_guide[j] for j in state)]

    def is_goal(state):
        return len(state) == s**2

    parsed = get_parsed(raw_input)
    all_tiles = []
    for id, tile in parsed:
        all_tiles += [(id, t) for t in get_all_eight_tiles(tile)]
    s = int(len(parsed)**0.5)
    right_match_guide = get_right_match_guide(all_tiles)
    down_match_guide = get_down_match_guide(all_tiles)
    same_id_guide = get_same_id_guide(all_tiles)
    spf = SolutionPathFinder(initial_states=[tuple()], successor_fn=get_successors, is_goal_fn=is_goal)
    ss = spf.find_solution()
    # print(ss)
    solution_tiles = []
    for i in ss:
        id, tile = all_tiles[i]
        # print(id)
        # pprint(tile)
        solution_tiles.append(tile)
    answer = 1
    for i in (ss[0], ss[s - 1], ss[-s], ss[-1]):
        answer *= all_tiles[i][0]
    print(f'Part1: {answer}')

    t = len(solution_tiles[0]) - 2
    u = s * t
    grid = [['.'] * u for _ in range(u)]
    grid[0][0] = solution_tiles[0][0][0]
    grid[0][-1] = solution_tiles[s - 1][0][-1]
    grid[-1][0] = solution_tiles[-s][-1][0]
    grid[-1][-1] = solution_tiles[-1][-1][-1]
    for h in range(len(solution_tiles)):
        i, j = h // s, h % s
        for k in range(t):
            for l in range(t):
                new_val = solution_tiles[h][1 + k][1 + l]
                grid[t * i + k][t * j + l] = new_val
    grid = tuple(''.join(row) for row in grid)
    all_grid_rotations = get_all_eight_tiles(grid)
    for grid in all_grid_rotations:
        serpent_mask = set()
        pounds_count = sum(1 for i in range(u) for j in range(u) if grid[i][j] == '#')

        for i in range(u - sm_h):
            for j in range(u - sm_w):
                if all(grid[i + k][j + l] == '#' for k, l in sm_squares()):
                    # print(f'serpent found at {i}, {j}')
                    for k, l in sm_squares():
                        serpent_mask.add((i + k, j + l))
        if serpent_mask:
            break

    answer_2 = pounds_count - len(serpent_mask)
    print(f'Part2: {answer_2}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    for x in parsed:
        pass
    answer = 0
    print(f'Part2: {answer}')

part_1(sample_input_0)
part_1(main_input)

# part_2(sample_input_1)
# part_2(main_input)
