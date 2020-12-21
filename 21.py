from utils.utils_21 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_21 import GameConsole, TweakedGameConsole, memo
from inputs.input_21 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        ingredients, allergens = get_regex_search(raw_item, r'(.*) \(contains (.*)\)')
        parsed.append((tuple(ingredients.split()), tuple(allergens.split(', '))))
    return parsed


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


sample_input_0 = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

sample_input_1 = """"""


def part_1(raw_input):
    def is_goal(state):
        return state[0] == len(dataset)

    def get_successors(state):
        line_number, assigned_ings, assigned_alls = state
        next_ings, next_alls = dataset[line_number]
        free_alls = []
        for allergen in next_alls:
            if allergen not in assigned_alls:
                free_alls.append(allergen)
            else:
                i = assigned_alls.index(allergen)
                if assigned_ings[i] not in next_ings:
                    return []
        free_ings = [ing for ing in next_ings if ing not in assigned_ings]
        if len(free_alls) > len(free_ings):
            return []
        successors = []
        for ings_to_assign in combinations(free_ings, len(free_alls)):
            for alls_to_assign in permutations(free_alls):
                new_assigned_ings = assigned_ings + tuple(ings_to_assign)
                new_assigned_alls = assigned_alls + tuple(alls_to_assign)
                successors.append((line_number + 1, new_assigned_ings, new_assigned_alls))
        return successors

    dataset = get_parsed(raw_input)
    # dataset.sort(key)
    print(dataset[0])
    ingredient_counts = dict(Counter(x for row in dataset for x in row[0]))
    print(ingredient_counts)
    allergen_counts = dict(Counter(x for row in dataset for x in row[1]))
    print(allergen_counts)
    dataset.sort(key=lambda x: ('wheat' not in x[1], 'dairy' not in x[1]))
    for allergen in allergen_counts:
        print(allergen)
        print(set.intersection(*(set(x[0]) for x in dataset if allergen in x[1])))
    intial_states = [
        (0, ('qmrps', 'cljf', 'qnvx', 'qsjszn'), ('nuts', 'dairy', 'shellfish', 'wheat'))
    ]
    spf = SolutionPathFinder(intial_states, get_successors, is_goal)
    solution = spf.find_solution()
    print(solution)
    answer = 0
    for ing, count in ingredient_counts.items():
        if ing not in solution[1]:
            answer += count
    print(f'Part1: {answer}')
    answer_2 = ','.join(x[1] for x in sorted(zip(solution[2], solution[1])))
    print(f'Part2: {answer_2}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    for x in parsed:
        pass
    answer = 0
    print(f'Part2: {answer}')

# part_1(sample_input_0)
part_1(main_input)

# part_2(sample_input_1)
# part_2(main_input)
