from utils.utils_22 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_22 import GameConsole, TweakedGameConsole, memo
from inputs.input_22 import main_input

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

            popped_state = self.states_to_explore[i]
            if i % 10000 == 0:
                print(i, popped_state)
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
    players = []
    for player in get_raw_items(raw_input, split_token='\n\n'):
        players.append(tuple(int(x) for x in player.split('\n')[1:]))
    return players


sample_input_0 = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

sample_input_1 = """"""


def part_1(raw_input):
    def get_successors(state):
        r, p1, p2 = state
        new_p1 = p1[1:]
        new_p2 = p2[1:]
        if p1[0] > p2[0]:
            new_p1 = new_p1 + (p1[0], p2[0])
        else:
            new_p2 = new_p2 + (p2[0], p1[0])
        return [(r + 1, new_p1, new_p2)]

    def is_goal(state):
        return not state[1] or not state[2]

    p1, p2 = get_parsed(raw_input)
    print(p1)
    print(p2)
    spf = SolutionPathFinder([(0, p1, p2)], get_successors, is_goal)
    solution = spf.find_solution()
    print(solution)
    answer = 0
    for i, x in enumerate(reversed(solution[1])):
        answer += (i + 1) * x
    for i, x in enumerate(reversed(solution[2])):
        answer += (i + 1) * x
    print(f'Part1: {answer}')


def part_2(raw_input):
    gfs_cache = {}
    def get_final_state(initial_state, depth):
        if initial_state in gfs_cache:
            return gfs_cache[initial_state]
        seen = set()
        p1, p2 = initial_state
        while p1 and p2:
            if depth == 0:
                print(p1, p2)
            p1_card, p1_rest = p1[0], p1[1:]
            p2_card, p2_rest = p2[0], p2[1:]
            if (p1, p2) in seen:
                p1 = p1_rest + (p1_card, p2_card)
                p2 = p2_rest
                continue
            seen.add((p1, p2))
            if p1_card <= len(p1_rest) and p2_card <= len(p2_rest):
                sub_p1, sub_p2 = get_final_state((p1_rest[:p1_card], p2_rest[:p2_card]), depth + 1)
                if sub_p1:
                    p1 = p1_rest + (p1_card, p2_card)
                    p2 = p2_rest
                    continue
                else:
                    p2 = p2_rest + (p2_card, p1_card)
                    p1 = p1_rest
                    continue
            if p1_card > p2_card:
                p1 = p1_rest + (p1_card, p2_card)
                p2 = p2_rest
            else:
                p1 = p1_rest
                p2 = p2_rest + (p2_card, p1_card)
        gfs_cache[initial_state] = (p1, p2)
        return p1, p2

    p1, p2 = get_parsed(raw_input)
    print(p1)
    print(p2)
    print('*****')
    p1, p2 = get_final_state((p1, p2), 0)
    answer = 0
    for i, x in enumerate(reversed(p1)):
        answer += (i + 1) * x
    for i, x in enumerate(reversed(p2)):
        answer += (i + 1) * x
    print(f'Part2: {answer}')

# part_1(sample_input_0)
# part_1(main_input)

# part_2(sample_input_0)
part_2(main_input)
