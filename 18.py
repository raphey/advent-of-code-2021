from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_18 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter

import json



sample_input = """[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"""

sample_input = "[[[[[9,8],1],2],3],4]"
sample_input = "[7,[6,[5,[4,[3,2]]]]]"
sample_input = "[[6,[5,[4,[3,2]]]],1]"
sample_input = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
sample_input = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
sample_input = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""

sample_input = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""

sample_input = """[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
[7,[5,[[3,8],[1,4]]]]"""

sample_input = """[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
[[[[4,2],2],6],[8,7]]"""





class SnailPair:
    def __init__(self, pair, depth=0, parent=None, ab=None):
        a, b = pair
        if type(a) is int:
            self.a = a
        else:
            self.a = SnailPair(a, depth=depth + 1, parent=self, ab="a")
        if type(b) is int:
            self.b = b
        else:
            self.b = SnailPair(b, depth=depth + 1, parent=self, ab="b")
        self.depth = depth
        self.parent = parent
        self.ab = ab

    def __repr__(self):
        return str((self.a, self.b, self.depth))

    def __iter__(self):
        yield self.a
        yield self.b

    def explode_left(self):
        snail = self
        while snail.ab != "b" and snail.ab is not None:
            snail = snail.parent
        if snail is None:
            return
        snail = snail.parent
        if snail is None:
            return
        if type(snail.a) is int:
            snail.a += self.a
            return
        snail = snail.a
        while type(snail.b) is not int:
            snail = snail.b
        snail.b += self.a

    def explode_right(self):
        snail = self
        while snail.ab != "a" and snail.ab is not None:
            snail = snail.parent
        # print(snail)
        if snail is None:
            return
        snail = snail.parent
        if snail is None:
            return
        if type(snail.b) is int:
            snail.b += self.b
            return
        snail = snail.b
        while type(snail.a) is not int:
            snail = snail.a
        snail.a += self.b

    def generate_subsnails(self):
        if type(self.a) is not int:
            yield self.a
            for snail in self.a.generate_subsnails():
                yield snail
        if type(self.b) is not int:
            yield self.b
            for snail in self.b.generate_subsnails():
                yield snail

    def explode(self):
        assert self.depth >= 4
        self.explode_left()
        self.explode_right()
        if self.ab == "a":
            self.parent.a = 0
        elif self.ab == "b":
            self.parent.b = 0

    def check_and_split(self):
        if type(self.a) is int and self.a >= 10:
            self.a = SnailPair((self.a // 2, (self.a + 1) // 2), depth=self.depth + 1, parent=self, ab="a")
            return True
        if type(self.a) is not int and self.a.check_and_split():
            return True
        if type(self.b) is int and self.b >= 10:
            self.b = SnailPair((self.b // 2, (self.b + 1) // 2), depth=self.depth + 1, parent=self, ab="b")
            return True
        return False

    def get_magnitude(self):
        if type(self.a) is int:
            mag_a = 3 * self.a
        else:
            mag_a = 3 * self.a.get_magnitude()
        if type(self.b) is int:
            mag_b = 2 * self.b
        else:
            mag_b = 2 * self.b.get_magnitude()
        return mag_a + mag_b


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = SnailPair(json.loads(raw_item))
        parsed.append(parsed_item)
    return parsed


def part_1(raw_input):
    parsed = get_parsed(raw_input)
    current_snail = parsed[0]
    print(current_snail)
    for snail in parsed[1:]:
        print('********')
        for ss in current_snail.generate_subsnails():
            ss.depth += 1
        current_snail.depth += 1
        for ss in snail.generate_subsnails():
            ss.depth += 1
        snail.depth += 1
        current_snail = SnailPair((current_snail, snail))
        current_snail.a.ab = "a"
        current_snail.a.parent = current_snail
        current_snail.b.ab = "b"
        current_snail.b.parent = current_snail
        print(current_snail)
        stable = False
        while not stable:
            stable = True
            split_used = False
            for subsnail in current_snail.generate_subsnails():
                if subsnail.depth >= 4:
                    subsnail.explode()
                    print("exploded! New snail:")
                    print(current_snail)
                    stable = False
                    break
            if not stable:
                continue
            for subsnail in current_snail.generate_subsnails():
                if subsnail.check_and_split():
                    print("split! New snail:")
                    print(current_snail)
                    stable = False
                    break
        print(current_snail)
    print(current_snail)
    answer = current_snail.get_magnitude()
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    mm = 0
    for i in range(len(parsed)):
        for j in range(len(parsed)):
            parsed = get_parsed(raw_input)
            if i == j:
                continue
            snail_a = parsed[i]
            snail_b = parsed[j]

            for ss in snail_a.generate_subsnails():
                ss.depth += 1
            snail_a.depth += 1
            for ss in snail_b.generate_subsnails():
                ss.depth += 1
            snail_b.depth += 1
            sum_snail = SnailPair((snail_a, snail_b))
            sum_snail.a.ab = "a"
            sum_snail.a.parent = sum_snail
            sum_snail.b.ab = "b"
            sum_snail.b.parent = sum_snail
            print(sum_snail)
            stable = False
            while not stable:
                stable = True
                for subsnail in sum_snail.generate_subsnails():
                    if subsnail.depth >= 4:
                        subsnail.explode()
                        print("exploded! New snail:")
                        print(sum_snail)
                        stable = False
                        break
                if not stable:
                    continue
                for subsnail in sum_snail.generate_subsnails():
                    if subsnail.check_and_split():
                        print("split! New snail:")
                        print(sum_snail)
                        stable = False
                        break
            mag = sum_snail.get_magnitude()
            mm = max(mag, mm)

    answer = mm
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
