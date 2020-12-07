from utils.utils_07 import gen_raw_items, get_regex_captures, regex, translate
from inputs.input_07 import sample_input, main_input

import re


pattern_2 = re.compile(r'(\d) (\w+ \w+)')

def gen_parsed(raw_input):
    for raw_item in gen_raw_items(raw_input, split_token='\n'):
        # vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
        capture_1 = get_regex_captures(string=raw_item, r_string=r'(.*?) bags contain (.*?) bags?\.')
        if 'no other' in capture_1:
            yield capture_1[0], []
        capture_2_matches = pattern_2.findall(capture_1[1])
        yield capture_1[0], {type: count for count, type in capture_2_matches}


def contains_shiny_gold(rules, bag):
    if not rules[bag]:
        return False
    if 'shiny gold' in rules[bag]:
        return True
    return any(contains_shiny_gold(rules, bag) for bag in rules[bag])


def part_1(raw_input):
    answer = 0
    all_rules = dict()
    for x in gen_parsed(raw_input):
        all_rules[x[0]] = x[1]
    answer = len([b for b in all_rules if contains_shiny_gold(all_rules, b)])
    print(f'Part1: {answer}')


sample_input_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


def contained_bag_count(rules, bag):
    if not rules[bag]:
        return 0
    return sum(int(rules[bag][b]) * (1 + contained_bag_count(rules, b)) for b in rules[bag])


def part_2(raw_input):
    answer = 0
    all_rules = dict()
    for x in gen_parsed(raw_input):
        all_rules[x[0]] = x[1]
    answer = contained_bag_count(all_rules, 'shiny gold')
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input_2)
part_2(main_input)
