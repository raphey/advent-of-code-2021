from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_12 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter, defaultdict


sample_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = tuple(raw_item.split('-'))
        parsed.append(parsed_item)
    return parsed


def get_graph_dictionary(edge_tuples):
    graph = defaultdict(list)
    for x, y in edge_tuples:
        graph[x].append(y)
        graph[y].append(x)
    return graph


def get_small_caves(edge_tuples):
    small_caves = set()
    for x, y in edge_tuples:
        if x.islower():
            small_caves.add(x)
        if y.islower():
            small_caves.add(y)
    return small_caves


def get_all_paths(cave_graph, small_cave_set):
    initial_state = ("start",)
    to_explore = [initial_state]
    complete_paths = []
    while to_explore:   # Assume no two big caves are connected
        state = to_explore.pop()
        if state[-1] == "end":
            complete_paths.append(state)
            continue
        successors = [state + (x,) for x in cave_graph[state[-1]] if not (x in small_cave_set and x in state)]
        for successor in successors:
            to_explore.append(successor)
    return complete_paths


def get_all_paths_pt_2(cave_graph, small_cave_set):
    initial_state = (("start",), False)
    to_explore = [initial_state]
    complete_paths = []
    while to_explore:   # Assume no two big caves are connected
        state = to_explore.pop()
        if state[0][-1] == "end":
            complete_paths.append(state)
            continue
        if state[1]:
            successors = [(state[0] + (x,), True) for x in cave_graph[state[0][-1]] if not (x in small_cave_set and x in state[0])]
        else:
            successors = []
            neighbors = [x for x in cave_graph[state[0][-1]] if x != "start"]
            for x in neighbors:
                if x not in small_cave_set or x not in state[0]:
                    successors.append((state[0] + (x,), False))
                else:
                    successors.append((state[0] + (x,), True))
        for successor in successors:
            to_explore.append(successor)
    complete_paths.sort()
    # for p in complete_paths:
    #     print(p)
    return complete_paths



def part_1(raw_input):
    edge_tuples = get_parsed(raw_input)
    small_cave_set = get_small_caves(edge_tuples)
    cave_graph = get_graph_dictionary(edge_tuples)
    all_paths = get_all_paths(cave_graph, small_cave_set)
    answer = len(all_paths)
    print(f'Part1: {answer}')


def part_2(raw_input):
    edge_tuples = get_parsed(raw_input)
    small_cave_set = get_small_caves(edge_tuples)
    cave_graph = get_graph_dictionary(edge_tuples)
    all_paths = get_all_paths_pt_2(cave_graph, small_cave_set)
    answer = len(all_paths)
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
