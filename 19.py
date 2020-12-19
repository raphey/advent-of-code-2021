from utils.utils_19 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_19 import GameConsole, TweakedGameConsole, memo
from inputs.input_19 import main_input

from itertools import combinations
from itertools import product
import copy
import re
from collections import Counter


def get_parsed(raw_input):
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
    rule_list = [None] * (max(k for k in (rule_dict)) + 1)
    for k, v in rule_dict.items():
        rule_list[k] = v
    return tuple(rule_list), tuple(split_messages)


def get_string_combinations(string_tuples):
    # print('get_string_combinations')
    # print(string_tuples)
    # print(tuple(''.join(x) for x in product(*string_tuples)))
    return set(''.join(x) for x in product(*string_tuples))


@memo
def get_string_set(rules, i):
    # print(i, type(i))
    if type(rules[i]) is str:
        return {rules[i]}
    if type(rules[i][0]) is int:    # concat case
        return set(get_string_combinations([get_string_set(rules, x) for x in rules[i]]))
    # pipe case
    x = set(get_string_combinations([get_string_set(rules, x) for x in rules[i][0]]))
    y = set(get_string_combinations([get_string_set(rules, x) for x in rules[i][1]]))
    return x | y


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


def part_1(raw_input):
    rule_list, messages = get_parsed(raw_input)
    answer = 0
    for m in messages:
        if m in get_string_set(rule_list, 0):
            answer += 1

    print(f'Part1: {answer}')


def part_2(raw_input):
    def are_chunks_valid(cs):

        # format of rule 0 string is:
        # (42)+ (31)+, where first count > second

        count_42 = 0
        count_31 = 0
        for j, c in enumerate(cs):

            if c in strings_42:
                count_42 += 1
            else:
                break
        for k in range(j, len(cs)):
            if cs[k] in strings_31:
                count_31 += 1
            else:
                return False
        return count_42 > count_31 and count_31

    rule_list, messages = get_parsed(raw_input)
    answer = 0

    strings_31 = get_string_set(rule_list, 31)
    strings_42 = get_string_set(rule_list, 42)

    # 42 and 31 have no overlap, which isn't necessary here, but
    # would be for this to work with, say, (31)+ (42)+ and more 42 than 31.
    assert(len([x for x in strings_42 if x in strings_31]) == 0)
    q = len(list(strings_42)[0])

    for i, m in enumerate(messages):
        m_chunks = [m[i: i + q] for i in range(0, len(m), q)]
        if are_chunks_valid(m_chunks):
            answer += 1
    print(f'Part2: {answer}')


part_1(sample_input_0)
part_1(main_input)

part_2(sample_input_1)
part_2(main_input)
