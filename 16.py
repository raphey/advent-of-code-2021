from utils.utils_15 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_15 import GameConsole, TweakedGameConsole, memo
from inputs.input_16 import main_input

from itertools import combinations
import copy
import re
from collections import Counter


def get_parsed(raw_input):
    sections = get_raw_items(raw_input, split_token='\n\n')
    # section 0
    rules = {}
    for line in sections[0].split('\n'):
        search_results = get_regex_search(line, r'(.*): (\d+)\-(\d+) or (\d+)\-(\d+)')
        field = search_results[0]
        lb1, ub1, lb2, ub2 = (int(x) for x in search_results[1:])
        rules[field] = ((lb1, ub1), (lb2, ub2))
    # section 1
    section_1 = get_raw_items(sections[1], split_token='\n')[1]
    my_ticket = [int(x) for x in section_1.split(',')]
    # section 2
    section_2 = get_raw_items(sections[2], split_token='\n')[1:]
    other_tickets = [[int(x) for x in line.split(',')] for line in section_2]

    return rules, my_ticket, other_tickets



sample_input_0 = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

sample_input_1 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""


def part_1(raw_input):
    rules, my_ticket, other_tickets = get_parsed(raw_input)
    all_bounds = []
    for (lb1, ub1), (lb2, ub2) in rules.values():
        all_bounds.append((lb1, ub1))
        all_bounds.append((lb2, ub2))
    answer = 0
    for t in other_tickets:
        for x in t:
            if not any(lb <= x <= ub for (lb, ub) in all_bounds):
                answer += x
    print(f'Part1: {answer}')


def is_valid(ticket, all_bounds):
    for x in ticket:
        if not any(lb <= x <= ub for (lb, ub) in all_bounds):
            return False
    return True


def part_2(raw_input):
    rules, my_ticket, other_tickets = get_parsed(raw_input)
    all_bounds = []
    for (lb1, ub1), (lb2, ub2) in rules.values():
        all_bounds.append((lb1, ub1))
        all_bounds.append((lb2, ub2))
    valid_tickets = [my_ticket] + [t for t in other_tickets if is_valid(t, all_bounds)]
    all_possible_fields = []
    for i, fvs in enumerate(zip(*valid_tickets)):
        possible_fields = []
        for field, ((lb1, ub1), (lb2, ub2)) in rules.items():
            if all(((lb1 <= fv <= ub1) or (lb2 <= fv <= ub2)) for fv in fvs):
                possible_fields.append(field)
        all_possible_fields.append(possible_fields)

    finalized_assignments = {}

    while len(finalized_assignments) < len(rules):
        for i, possible_fields in enumerate(all_possible_fields):
            if len(possible_fields) == 1:
                field = possible_fields[0]
                finalized_assignments[field] = i
                for possible_fields in all_possible_fields:
                    try:
                        possible_fields.remove(field)
                    except ValueError:
                        pass
                continue
    print(finalized_assignments)
    answer = 1
    for field, index in finalized_assignments.items():
        if field.startswith('departure'):
            answer *= my_ticket[index]
    print(f'Part2: {answer}')


# part_1(sample_input_0)
# part_1(main_input)

part_2(sample_input_1)
part_2(main_input)
