from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_08 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter


sample_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        left, right = raw_item.split(' | ')
        parsed.append((left.split(), right.split()))
    return parsed


def part_1(raw_input):
    parsed = get_parsed(raw_input)
    answer = 0
    for _, right in parsed:
        answer += sum(1 for x in right if len(x) in {2, 3, 4, 7})
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    decoded = []
    # find two set
    answer = 0
    for left, right in parsed:
        decoded += [(-1 * len(left), -1 * len(right))]
        for x in left + right:
            if len(x) == 2:
                two_set = set(x)
                break
        else:
            raise ValueError(f"No two length, {left + right}")
        print(two_set)
        # find a
        for x in left + right:
            if len(x) == 3:
                a = [q for q in x if q not in two_set][0]
                break
        else:
            raise ValueError(f"No three length, {left + right}")
        print(f"a = {a}")
        # find c
        for x in left + right:
            if len(x) == 6:
                two_set_intersection = set(x).intersection(two_set)
                assert(len(two_set_intersection) in {1, 2})
                if len(two_set_intersection) == 2:
                    continue
                f = list(two_set_intersection)[0]
                break
        else:
            raise ValueError(f"No six length which is a 6, {left + right}")
        print(f"f = {f}")
        c = [x for x in two_set if x != f][0]
        print(f"c = {c}")
        # find bdset
        for x in left + right:
            if len(x) == 4:
                bd_set = set(q for q in x if q not in two_set)
                break
        else:
            raise ValueError(f"No six length which is a 6 length, {left + right}")
        print(bd_set)
        # find b and d
        for x in left + right:
            if len(x) == 6:
                bd_intersection = set(x).intersection(bd_set)
                if len(bd_intersection) == 2:
                    continue
                b = list(bd_intersection)[0]
                d = list(q for q in bd_set if q != b)[0]
                break
        else:
            raise ValueError(f"No six length which is a 0, {left + right}")
        print(f"b = {b}")
        print(f"d = {d}")

        print('whee')
        print(right)
        digits = ""
        for q in right:
            print(f"q: {q}")
            if len(q) == 6 and d not in q:
                digits += '0'
            elif len(q) == 2:
                digits += '1'
            elif len(q) == 5 and f not in q:
                digits += '2'
            elif len(q) == 5 and b not in q:
                digits += '3'
            elif len(q) == 4:
                digits += '4'
            elif len(q) == 5:
                digits += '5'
            elif len(q) == 6 and c not in q:
                digits += '6'
            elif len(q) == 3:
                digits += '7'
            elif len(q) == 7:
                digits += '8'
            elif len(q) == 6:
                digits += '9'
            else:
                raise ValueError(f"failed to translate {q}")
        print(digits)
        answer += int(digits)

    print(f'Part2: {answer}')


def part_2_alt(raw_input):
    def is_mapping_valid(encoded_digits, trans):
        return all(''.join(sorted(x.translate(trans))) in digit_dict for x in encoded_digits)

    digit_dict = {
        'abcefg': '0',
        'cf': '1',
        'acdeg': '2',
        'acdfg': '3',
        'bcdf': '4',
        'abdfg': '5',
        'abdefg': '6',
        'acf': '7',
        'abcdefg': '8',
        'abcdfg': '9',
    }
    parsed = get_parsed(raw_input)
    answer = 0
    for left, right in parsed:
        for permutation in permutations('abcdefg'):
            permuted_letters = ''.join(permutation)
            translator = str.maketrans('abcdefg', permuted_letters)
            if is_mapping_valid(left + right, translator):
                digits = ''
                for x in right:
                    digits += digit_dict[''.join(sorted(x.translate(translator)))]
                answer += int(digits)
    print(f'Part2: {answer}')

part_1(sample_input)
part_1(main_input)

part_2_alt(sample_input)
part_2_alt(main_input)


"""
Shortly after solving it: why did I try to do the explicit logic, when there were only 5040
permutations to check? 
"""