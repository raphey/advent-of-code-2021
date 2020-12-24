from utils.utils_23 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_23 import GameConsole, TweakedGameConsole, memo
from inputs.input_23 import main_input

from itertools import combinations
import copy
import re
from collections import Counter


def get_parsed(raw_input):
    return [int(d) for d in raw_input]


sample_input_0 = """389125467"""

sample_input_1 = """"""


main_input = '469217538'


def part_1(raw_input):
    def get_next_state(state):
        picked_up = state[1:4]
        new_state = state[0:1] + state[4:]
        target = state[0] - 1
        min_cup = min(new_state)
        max_cup = max(new_state)
        while True:
            try:
                i = new_state.index(target)
                break
            except ValueError:
                if target > min_cup:
                    target -= 1
                else:
                    target = max_cup
        new_state = new_state[:i + 1] + picked_up + new_state[i + 1:]
        return new_state[1:] + new_state[0:1]

    parsed = get_parsed(raw_input)
    current_state = tuple(parsed)
    for i in range(100):
        print(current_state)
        current_state = get_next_state(current_state)
    print(current_state)


big = 10**6
big_2 = big * 10


def part_2_old(raw_input):
    def get_next_state(state):
        picked_up = state[1:4]
        new_state = state[0:1] + state[4:]
        target = state[0] - 1
        min_cup = min(new_state)
        max_cup = max(new_state)
        while True:
            try:
                i = new_state.index(target)
                break
            except ValueError:
                if target > min_cup:
                    target -= 1
                else:
                    target = max_cup
        new_state = new_state[:i + 1] + picked_up + new_state[i + 1:]
        return new_state[1:] + new_state[0:1]

    def get_two_key_cups(state):
        i = state.index(1)
        cup_1 = state[(i + 1) % big]
        cup_2 = state[(i + 2) % big]
        return cup_1, cup_2

    parsed = get_parsed(raw_input)
    current_state = tuple(parsed) + tuple(range(max(parsed) + 1, big + 1))
    for i in range(big_2):
        # print(i, get_two_key_cups(current_state), current_state)
        current_state = get_next_state(current_state)
    # print(i, get_two_key_cups(current_state), current_state)
    key_1, key_2 = get_two_key_cups(current_state)
    answer = key_1 * key_2
    print(f'Part2: {answer}')


verbose = True

def part_2(raw_input):
    def get_next_state(state):
        lead, state_dict = state
        picked_up_1 = state_dict[lead]
        picked_up_2 = state_dict[picked_up_1]
        picked_up_3 = state_dict[picked_up_2]
        # print('picked_up')
        # print(picked_up_1, picked_up_2, picked_up_3)

        state_dict[lead] = state_dict[picked_up_3]
        # print('lead points to:', state_dict[lead])
        target = lead - 1
        while True:
            if target in (picked_up_1, picked_up_2, picked_up_3):
                target -= 1
                continue
            if target < 1:
                target = big
                continue
            break
        # print('target:', target)
        state_dict[picked_up_3] = state_dict[target]
        # print('picked up 3 now points to:', state_dict[picked_up_3])
        state_dict[target] = picked_up_1
        new_lead = state_dict[lead]
        return new_lead, state_dict

    def get_two_key_cups(state):
        _, state_dict = state
        cup_1 = state_dict[1]
        cup_2 = state_dict[cup_1]
        return cup_1, cup_2

    parsed = get_parsed(raw_input)
    cups_tuple = tuple(parsed) + tuple(range(max(parsed) + 1, big + 1))
    cups_dict = dict(zip(cups_tuple, cups_tuple[1:]))
    cups_dict[cups_tuple[-1]] = cups_tuple[0]
    current_state = cups_tuple[0], cups_dict
    for i in range(big_2):
        if i % 100000 == 0: print(i)
        # print(i, get_two_key_cups(current_state), current_state)
        current_state = get_next_state(current_state)
    # print(i, get_two_key_cups(current_state), current_state)
    key_1, key_2 = get_two_key_cups(current_state)
    answer = key_1 * key_2
    print(f'Part2: {answer}')


# part_1(sample_input_0)
part_1(main_input)

# part_2_old(sample_input_0)
# part_2(sample_input_0)
part_2(main_input)
