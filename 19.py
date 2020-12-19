from utils.utils_19 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_19 import GameConsole, TweakedGameConsole, memo
from inputs.input_19 import main_input, main_input_2

from itertools import combinations
from itertools import product
import copy
import re
from collections import Counter


def get_char_rule(c):
    return lambda x: x == c


@memo
def get_all_string_split_indices(string_length, num_sections):
    return list(combinations(range(1, string_length), num_sections - 1))


@memo
def get_all_string_parts(x, num_parts):
    asp = []
    for splits in get_all_string_split_indices(len(x), num_parts):
        splits = [0] + list(splits) + [len(x)]
        # print(splits)
        string_parts = [x[i:j] for i, j in zip(splits, splits[1:])]
        asp.append(string_parts)
    return asp


def get_concat_rule(rule_dict, rule_nums):
    def concat_rule(x):
        all_string_parts = get_all_string_parts(x, len(rule_nums))
        for sp in all_string_parts:
            if all(rule_dict[i](p) for i, p in zip(rule_nums, sp)):
                return True
        return False
    return concat_rule


def get_pipe_rule(rule_dict, rule_nums_a, rule_nums_b):
    concat_rule_a = get_concat_rule(rule_dict, rule_nums_a)
    concat_rule_b = get_concat_rule(rule_dict, rule_nums_b)
    return lambda x: concat_rule_a(x) or concat_rule_b(x)


def get_parsed(raw_input):
    rules, messages = get_raw_items(raw_input, split_token='\n\n')
    rule_dict = {}
    for r_line in get_raw_items(rules, split_token='\n'):
        rule_num, rest = r_line.split(': ')
        rule_num = int(rule_num)
        if '"' in rest:
            c = rest.split('"')[1]
            rule_dict[rule_num] = get_char_rule(c)
        elif '|' in rest:
            first, second = rest.split(' | ')
            index_list_a = [int(p) for p in first.split(' ')]
            index_list_b = [int(p) for p in second.split(' ')]
            rule_dict[rule_num] = get_pipe_rule(rule_dict, index_list_a, index_list_b)
        else:
            rule_indices = [int(p) for p in rest.split(' ')]
            rule_dict[rule_num] = get_concat_rule(rule_dict, rule_indices)

    split_messages = get_raw_items(messages, split_token='\n')
    return rule_dict, split_messages


def alt_get_parsed(raw_input):
    rules, messages = get_raw_items(raw_input, split_token='\n\n')
    rule_dict = {}
    # turn every rule into a set of valid characters
    full_rules = []
    for r_line in get_raw_items(rules, split_token='\n'):
        rule_num, rest = r_line.split(': ')
        rule_num = int(rule_num)
        if '"' in rest:
            c = rest.split('"')[1]
            rule_dict[rule_num] = [c,]
            full_rules.append(rule_num)
        elif '|' in rest:
            first, second = rest.split(' | ')
            index_list_a = [int(p) for p in first.split(' ')]
            index_list_b = [int(p) for p in second.split(' ')]
            rule_dict[rule_num] = [index_list_a, index_list_b]
        else:
            rule_indices = [int(p) for p in rest.split(' ')]
            rule_dict[rule_num] = rule_indices
    while full_rules:
        to_assign = full_rules.pop()  # rule_to_assign
        for i, rule_list in rule_dict.items():
            if type(rule_list[0]) is list:
                for j in range(len(rule_list)):
                    for k in range(len(rule_list[j])):
                        if rule_list[k]:   # fix
                            pass



    split_messages = get_raw_items(messages, split_token='\n')
    return rule_dict, split_messages


def get_string_combinations(string_tuples):
    # print('get_string_combinations')
    # print(string_tuples)
    # print(tuple(''.join(x) for x in product(*string_tuples)))
    return tuple(''.join(x) for x in product(*string_tuples))


string_validity = dict()

def is_in_messages(string, messages):
    try:
        return string_validity[string]
    except KeyError:
        validity = any(string in m for m in messages)
        string_validity[string] = validity
        return validity


def get_string_combinations_2(string_tuples, messages, max_length=88):
    # print('get_string_combinations')
    # print(string_tuples)
    # print(tuple(''.join(x) for x in product(*string_tuples)))
    combinations = set()
    for x in product(*string_tuples):
        x_str = ''.join(x)
        if len(x_str) <= max_length and is_in_messages(x_str, messages):
            combinations.add(x_str)
    return combinations



@memo
def get_string_set(rules, i, messages):
    # print(i, type(i))
    if type(rules[i]) is str:
        return set(rules[i])
    if type(rules[i][0]) is int:    # concat case
        return set(get_string_combinations([get_string_set(rules, x) for x in rules[i]]), messages)
    # pipe case
    # print('pipe case')
    x = set(get_string_combinations([get_string_set(rules, x) for x in rules[i][0]]), messages)
    y = set(get_string_combinations([get_string_set(rules, x) for x in rules[i][1]]), messages)
    return x | y
    # print('*!@#*$!@*$')
    # print(set.union(set(get_string_combinations([get_string_set(rules, x) for x in rules[i][0]])),
    #       set(get_string_combinations([get_string_set(rules, x) for x in rules[i]][1]))))
    # quit()
    # return (set(get_string_combinations([get_string_set(rules, x) for x in rules[i][0]])) |
    #         set(get_string_combinations([get_string_set(rules, x) for x in rules[i]][1])))


@memo
def get_string_set_2(rules, i, depth, messages):
    # print(depth)
    # print(i, type(i))
    if type(rules[i]) is str:
        return set(rules[i])
    if depth > MAX_DEPTH:
        return {''}
    if type(rules[i][0]) is int:    # concat case
        return get_string_combinations_2([get_string_set_2(rules, x, depth + 1, messages) for x in rules[i]], messages)
    # pipe case
    # print('pipe case')

    x = get_string_combinations_2([get_string_set_2(rules, x, depth + 1, messages) for x in rules[i][0]], messages)
    # if depth > MAX_DEPTH:
    #     return x
    y = get_string_combinations_2([get_string_set_2(rules, x, depth + 1, messages) for x in rules[i][1]], messages)
    return x | y
    # print('*!@#*$!@*$')
    # print(set.union(set(get_string_combinations([get_string_set(rules, x) for x in rules[i][0]])),
    #       set(get_string_combinations([get_string_set(rules, x) for x in rules[i]][1]))))
    # quit()
    # return (set(get_string_combinations([get_string_set(rules, x) for x in rules[i][0]])) |
    #         set(get_string_combinations([get_string_set(rules, x) for x in rules[i]][1])))




def alt_get_parsed_2(raw_input):
    rules, messages = get_raw_items(raw_input, split_token='\n\n')
    rule_dict = {}

    for r_line in get_raw_items(rules, split_token='\n'):
        rule_num, rest = r_line.split(': ')
        rule_num = int(rule_num)

        if '"' in rest:
            c = rest.split('"')[1]
            rule_dict[rule_num] = c
        elif '|' in rest:
            first, second = rest.split(' | ')
            index_list_a = tuple(int(p) for p in first.split(' '))
            index_list_b = tuple(int(p) for p in second.split(' '))
            rule_dict[rule_num] = (index_list_a, index_list_b)
        else:
            rule_indices = tuple(int(p) for p in rest.split(' '))
            rule_dict[rule_num] = rule_indices
    split_messages = get_raw_items(messages, split_token='\n')
    rule_list = [None] * (10 * len(rule_dict))
    for k, v in rule_dict.items():
        rule_list[k] = v
    return tuple(rule_list), tuple(split_messages)


# print(get_string_combinations([('a',), ('bc', 'de'), ('fgh', 'ijk', 'lmn')]))

sample_input_0 = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''

sample_input_1 = '''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''


sample_input_2 = '''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31 | 42 11 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42 | 42 8
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''


def part_1(raw_input):
    rule_list, messages = alt_get_parsed_2(raw_input)
    for i, rule in enumerate(rule_list):
        print(i, rule)
    answer = 0
    for m in messages:
        if m in get_string_set(rule_list, 0):
            answer += 1

    print(f'Part1: {answer}')


MAX_DEPTH = 5


def part_2(raw_input):
    rule_list, messages = alt_get_parsed_2(raw_input)
    # for i, rule in enumerate(rule_list):
    #     print(i, rule)
    answer = 0
    z = get_string_set_2(rule_list, 0, 0, messages)
    print(f'done getting_string_set, length {len(z)}')
    for m in messages:
        if m in get_string_set_2(rule_list, 0, 0, messages):
            answer += 1
    print(f'Part2: {answer}')


# part_1(sample_input_0)
# part_1(main_input)

# part_2(sample_input_0)
# part_2(sample_input_1)
# part_2(sample_input_2)
# part_2(main_input)
part_2(main_input_2)
