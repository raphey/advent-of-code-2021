from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo, AstarSolutionPathFinder
from inputs.input_23 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter, defaultdict


"""
very messy. please continue reading only as a cautionary tale
big takeaways: 
- if I'd known it would take so long, I'd have thought more about the
underlying data structure. I had some nice helper functions, but not enough.
- when I still allowed pointless moves within a column, things were much slower.
Restricting the number of available branches is really important.
- debugging by working backwards from the step-by-step example was useful.
- pretty printing was useful
- too much repetition and hardcoding, in retrospect.
- nice to be able to reuse an AStar solution finder I already made.
"""

sample_input = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""

'''sample_input = """#############
#...........#
###B#A#C#D###
  #A#B#C#D#
  #########"""'''

sample_input = """#############
#.........A.#
###.#B#C#D###
  #A#B#C#D#
  #########"""

sample_input = """#############
#.....D.D.A.#
###.#B#C#.###
  #A#B#C#.#
  #########"""

sample_input = """#############
#.....D.....#
###.#B#C#D###
  #A#B#C#A#
  #########"""

sample_input = """#############
#.........A.#
###.#B#C#D###
  #A#B#C#D#
  #########"""

sample_input = """#############
#.....D.D.A.#
###.#B#C#.###
  #A#B#C#.#
  #########"""

sample_input = """#############
#.....D.....#
###.#B#C#D###
  #A#B#C#A#
  #########"""

sample_input = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""


def get_parsed(raw_input):
    parsed = []
    for raw_item in raw_input.split('\n'):
        parsed_item = raw_item
        parsed.append(parsed_item)
    return parsed


def part_1(raw_input):
    def is_wall(i, j):
        return text_map[i][j] == "#"

    def in_room(room_id, i, j):
        room_dict = {'A': [(2, 3), (3, 3)], 'B': [(2, 5), (3, 5)], 'C': [(2, 7), (3, 7)], 'D': [(2, 9), (3, 9)]}
        return (i, j) in room_dict[room_id]

    def in_hallway(i, j):
        return i == 1

    def in_entrance(i, j):
        return i == 1 and j in (3, 5, 7, 9)

    def in_any_room(i, j):
        return any(in_room(c, i, j) for c in 'ABCD')

    def is_occupied(locs, i, j):
        return any((i, j) in loc_pair for loc_pair in locs)

    text_map = get_parsed(raw_input)
    locations = []
    for apod in 'ABCD':
        apod_locs = []
        for i in (1, 2, 3):
            for j, c in enumerate(text_map[i]):
                if c == apod:
                    apod_locs.append((i, j))
        locations.append(tuple(apod_locs))
    locations = tuple(locations)

    def get_heuristic_cost(cost, locs):
        heuristic = cost
        for k in range(4):
            step_cost = 10**k
            for i, j in locs[k]:
                if in_room('ABCD'[k], i, j):
                    # in correct room
                    if is_occupied(locs, i + 1, j):
                        if (i + 1, j) not in locs[k]:
                            heuristic += step_cost * 4
                    elif not is_wall(i + 1, j):
                        heuristic += step_cost
                    continue
                if in_any_room(i, j):
                    # in wrong room
                    heuristic += step_cost * (2 + abs(j - (2 * k + 3)))
                else:
                    heuristic += step_cost * (1 + abs(j - (2 * k + 3)))
        return heuristic

    state = ((get_heuristic_cost(0, locations), 0), locations)

    initial_states = [state]

    def is_goal(state):
        cost, locs = state
        return all(in_room("ABCD"[k], i, j) for k in range(4) for i, j in locs[k])

    def pprint(state):
        base = [list(row) for row in text_map]
        for row in base:
            for j in range(len(row)):
                if row[j] in 'ABCD':
                    row[j] = '.'
        for k in range(4):
            for i, j in state[1][k]:
                base[i][j] = 'ABCD'[k]
        print()
        print(f"Cost: {state[0]}")
        print(f"locations: {state[1]}")
        for row in base:
            print(''.join(row))

    global print_ticker
    print_ticker = 0

    def get_successors(state):
        global print_ticker
        print_ticker += 1
        if print_ticker % 1000 == 0:
            print('getting successors for:')
            pprint(state)
        (_, cost), locs = state
        for k in range(4):
            step_cost = 10**k
            for z, (i0, j0) in enumerate(locs[k]):
                i_other, j_other = locs[k][1 - z]
                # condition moving from hallway into room
                if in_hallway(i0, j0):
                    target_j = 2 * k + 3
                    start_j, end_j = sorted([j0, target_j])
                    if not is_occupied(locs, 2, target_j) and not is_occupied(locs, 1, target_j) and not any(is_occupied(locs, 1, jj) for jj in range(start_j + 1, end_j)):
                        if is_occupied(locs, 3, target_j):
                            if (3, target_j) not in locs[k]:
                                continue # can't block someone in
                            new_locs = list(locs)
                            new_locs[k] = ((2, target_j), (i_other, j_other))
                            new_cost = cost + (end_j - start_j + 1) * step_cost
                            yield (get_heuristic_cost(new_cost, new_locs), new_cost), tuple(new_locs)
                            continue
                        else:
                            new_locs = list(locs)
                            new_locs[k] = ((3, target_j), (i_other, j_other))
                            new_cost = cost + (end_j - start_j + 2) * step_cost
                            yield (get_heuristic_cost(new_cost, new_locs), new_cost), tuple(new_locs)
                            continue

                # move into hallway condition
                if in_any_room(i0, j0):
                    if i0 == 2:  # moving out to hall from top room position
                        if not in_room('ABCD'[k], i0, j0) or (is_occupied(locs, i0 + 1, j0) and (i0 + 1, j0) not in locs[k]):
                            # either in the wrong room (so ok to leave) or in correct room, blocking someone in
                            if not is_occupied(locs, i0 - 1, j0):
                                for j in range(j0 + 1, 100):
                                    if is_wall(1, j) or is_occupied(locs, 1, j):
                                        break
                                    if in_entrance(1, j):
                                        continue
                                    new_locs = list(locs)
                                    new_locs[k] = ((1, j), (i_other, j_other))
                                    new_cost = cost + step_cost * (1 + j - j0)
                                    yield (get_heuristic_cost(new_cost, new_locs), new_cost), tuple(new_locs)
                                for j in range(j0 - 1, -100, -1):
                                    if is_wall(1, j) or is_occupied(locs, 1, j):
                                        break
                                    if in_entrance(1, j):
                                        continue
                                    new_locs = list(locs)
                                    new_locs[k] = ((1, j), (i_other, j_other))
                                    new_cost = cost + step_cost * (1 + j0 - j)
                                    yield (get_heuristic_cost(new_cost, new_locs), new_cost), tuple(new_locs)
                    else:  # i0 == 3
                        if not in_room('ABCD'[k], i0, j0) and not is_occupied(locs, 2, j0):
                            if not is_occupied(locs, 1, j0):
                                for j in range(j0 + 1, 100):
                                    if is_wall(1, j) or is_occupied(locs, 1, j):
                                        break
                                    if in_entrance(1, j):
                                        continue
                                    new_locs = list(locs)
                                    new_locs[k] = ((1, j), (i_other, j_other))
                                    new_cost = cost + step_cost * (2 + j - j0)
                                    yield (get_heuristic_cost(new_cost, new_locs), new_cost), tuple(new_locs)
                                for j in range(j0 - 1, -100, -1):
                                    if is_wall(1, j) or is_occupied(locs, 1, j):
                                        break
                                    if in_entrance(1, j):
                                        continue
                                    new_locs = list(locs)
                                    new_locs[k] = ((1, j), (i_other, j_other))
                                    new_cost = cost + step_cost * (2 + j0 - j)
                                    yield (get_heuristic_cost(new_cost, new_locs), new_cost), tuple(new_locs)


    spf = AstarSolutionPathFinder(initial_states, successor_fn=get_successors, is_goal_fn=is_goal)
    solution = spf.find_solution()
    pprint(solution)
    answer = solution[0][1]
    print(f'Part1: {answer}')


def part_2(raw_input):
    def is_wall(i, j):
        return text_map[i][j] == "#"

    def in_room(room_id, i, j):
        room_dict = {'A': [(i, 3) for i in range(2, 6)], 'B': [(i, 5) for i in range(2, 6)], 'C': [(i, 7) for i in range(2, 6)], 'D': [(i, 9) for i in range(2, 6)]}
        return (i, j) in room_dict[room_id]

    def in_hallway(i, j):
        return i == 1

    def in_entrance(i, j):
        return i == 1 and j in (3, 5, 7, 9)

    def in_any_room(i, j):
        return any(in_room(c, i, j) for c in 'ABCD')

    def is_occupied(locs, i, j):
        return any((i, j) in loc_pair for loc_pair in locs)

    text_map = get_parsed(raw_input)
    text_map = text_map[:3] + ["  #D#C#B#A#", "  #D#B#A#C#"] + text_map[3:]
    locations = []
    for apod in 'ABCD':
        apod_locs = []
        for i in range(1, 6):
            for j, c in enumerate(text_map[i]):
                if c == apod:
                    apod_locs.append((i, j))
        locations.append(tuple(apod_locs))
    locations = tuple(locations)

    def get_heuristic_cost(cost, locs):
        heuristic = cost
        for k in range(4):
            step_cost = 10**k
            for i, j in locs[k]:
                if in_room('ABCD'[k], i, j):
                    # in correct room
                    if is_occupied(locs, i + 1, j):
                        if (i + 1, j) not in locs[k]:
                            heuristic += step_cost * 4
                    elif not is_wall(i + 1, j):
                        heuristic += step_cost
                    continue
                if in_any_room(i, j):
                    # in wrong room
                    heuristic += step_cost * (2 + abs(j - (2 * k + 3)))
                else:
                    heuristic += step_cost * (1 + abs(j - (2 * k + 3)))
        return heuristic

    state = ((get_heuristic_cost(0, locations), 0), locations)

    initial_states = [state]

    def is_goal(state):
        _, locs = state
        return all(in_room("ABCD"[k], i, j) for k in range(4) for i, j in locs[k])

    def pprint(state):
        base = [list(row) for row in text_map]
        for row in base:
            for j in range(len(row)):
                if row[j] in 'ABCD':
                    row[j] = '.'
        for k in range(4):
            for i, j in state[1][k]:
                base[i][j] = 'ABCD'[k]
        print()
        print(f"Cost: {state[0]}")
        print(f"locations: {state[1]}")
        for row in base:
            print(''.join(row))

    global print_ticker
    print_ticker = 0

    def get_successors(state):
        global print_ticker
        print_ticker += 1
        if print_ticker % 1000 == 0:
            print('getting successors for:')
            pprint(state)
        (_, cost), locs = state
        for k in range(4):
            step_cost = 10**k
            for z, (i0, j0) in enumerate(locs[k]):
                others = tuple(locs[k][q] for q in range(4) if q != z)
                # condition moving from hallway into room
                if in_hallway(i0, j0):
                    target_j = 2 * k + 3
                    start_j, end_j = sorted([j0, target_j])

                    if not is_occupied(locs, 2, target_j) and not is_occupied(locs, 1, target_j) and not any(is_occupied(locs, 1, jj) for jj in range(start_j + 1, end_j)):
                        if any(is_occupied(locs, q, target_j) and (q, target_j) not in locs[k] for q in range(3, 6)):
                            continue # can't block someone in
                        if is_occupied(locs, 3, target_j):
                            new_locs = list(locs)
                            new_locs[k] = ((2, target_j),) + others
                            new_cost = cost + (end_j - start_j + 1) * step_cost
                            yield (get_heuristic_cost(new_cost, new_locs), new_cost), tuple(new_locs)
                            continue
                        elif is_occupied(locs, 4, target_j):
                            new_locs = list(locs)
                            new_locs[k] = ((3, target_j),) + others
                            new_cost = cost + (end_j - start_j + 2) * step_cost
                            yield (get_heuristic_cost(new_cost, new_locs), new_cost), tuple(new_locs)
                            continue
                        elif is_occupied(locs, 5, target_j):
                            new_locs = list(locs)
                            new_locs[k] = ((4, target_j),) + others
                            new_cost = cost + (end_j - start_j + 3) * step_cost
                            yield (get_heuristic_cost(new_cost, new_locs), new_cost), tuple(new_locs)
                            continue
                        else:
                            new_locs = list(locs)
                            new_locs[k] = ((5, target_j),) + others
                            new_cost = cost + (end_j - start_j + 4) * step_cost
                            yield (get_heuristic_cost(new_cost, new_locs), new_cost), tuple(new_locs)
                            continue

                # move into hallway condition
                if in_any_room(i0, j0):
                    for d in range(2, 6):
                        if i0 == d:
                            if not in_room('ABCD'[k], i0, j0) or any((is_occupied(locs, i0 + q, j0) and (i0 + q, j0) not in locs[k]) for q in range(1, 4)):
                                # either in the wrong room (so ok to leave) or in correct room, blocking someone in
                                if not any(is_occupied(locs, q, j0) for q in range(i0 - 1, 0, -1)):
                                    for j in range(j0 + 1, 100):
                                        if is_wall(1, j) or is_occupied(locs, 1, j):
                                            break
                                        if in_entrance(1, j):
                                            continue
                                        new_locs = list(locs)
                                        new_locs[k] = ((1, j),) + others
                                        new_cost = cost + step_cost * (d - 1 + j - j0)
                                        yield (get_heuristic_cost(new_cost, new_locs), new_cost), tuple(new_locs)
                                    for j in range(j0 - 1, -100, -1):
                                        if is_wall(1, j) or is_occupied(locs, 1, j):
                                            break
                                        if in_entrance(1, j):
                                            continue
                                        new_locs = list(locs)
                                        new_locs[k] = ((1, j),) + others
                                        new_cost = cost + step_cost * (d - 1 + j0 - j)
                                        yield (get_heuristic_cost(new_cost, new_locs), new_cost), tuple(new_locs)


    spf = AstarSolutionPathFinder(initial_states, successor_fn=get_successors, is_goal_fn=is_goal)
    solution = spf.find_solution()
    pprint(solution)
    answer = solution[0][1]
    print(f'Part1: {answer}')
    quit()


# part_1(sample_input)
# part_1(main_input)

# part_2(sample_input)
part_2(main_input)
