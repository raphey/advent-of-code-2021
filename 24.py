from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_24 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter, defaultdict
from random import sample, randint


sample_input = """inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2"""


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = tuple(raw_item.split())
        parsed.append(parsed_item)
    return parsed


def get_reversed_instructions(instructions):
    rev_inst = [("inp", "z", 0)]
    for inst in instructions[::-1]:
        if inst[0] == "add":
            rev_inst.append(("sub",) + inst[1:])
        if inst[0] == "sub":
            rev_inst.append(("add",) + inst[1:])
        if inst[0] == "mul":
            rev_inst.append(("div",) + inst[1:])
        if inst[0] == "div":
            rev_inst.append(("mul",) + inst[1:])

class ALU:
    def __init__(self):
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0

    def get_b_val(self, b):
        try:
            return int(b)
        except ValueError:
            return getattr(self, b)

    def inp(self, a, value):
        setattr(self, a, value)

    def add(self, a, b):
        b_val = self.get_b_val(b)
        setattr(self, a, getattr(self, a) + b_val)

    def mul(self, a, b):
        b_val = self.get_b_val(b)
        setattr(self, a, getattr(self, a) * b_val)

    def div(self, a, b):
        b_val = self.get_b_val(b)
        setattr(self, a, getattr(self, a) // b_val)

    def mod(self, a, b):
        b_val = self.get_b_val(b)
        setattr(self, a, getattr(self, a) % b_val)

    def eql(self, a, b):
        b_val = self.get_b_val(b)
        setattr(self, a, 1 if getattr(self, a) == b_val else 0)

    def __repr__(self):
        return str((self.w, self.x, self.y, self.z))

    def is_legit(self):
        return self.z == 0


def get_mutated(start_str, k):
    new_str = start_str
    for i in sample(range(13), k):
        new_str = new_str[:i + 1] + str(randint(1, 9)) + new_str[i + 2:]  # keep leading digit
        # new_str = new_str[:i] + str(randint(1, 9)) + new_str[i + 1:]
    return new_str

def part_1(raw_input):
    instructions = get_parsed(raw_input)
    answer = ""
    short_list = []
    for current_best_str, z_min in [
        # ('81299897999854', 10),
        # ('81299897999852', 8),
        # ('81299897999853', 9),
        # ('85299897999895', 11),
        # ('81299567999854', 10),
        # ('81299897999851', 7),
        # ('82299897999864', 10),
        # ('81255897999851', 7),
        # ('81299897998754', 10),
        # ('81299897999855', 11),
        # ('81299897998754', 10),
        # ('81299897999852', 8),
        # ('81299897997654', 10),
        # ('81299787999851', 7),
        # ('81299897999851', 7),
        # ('85299897999896', 0)
        # '81299897999856',
        #  '82299897999866',
        #  '83299347999876',
        #  '84266897999886',
        #  '84299897999886',
        #  '85211897999896',
        #  '85222457999896',
        #  '85222897999896',
        #  '85233897999896',
        #  '85244895799896',
        #  '85244897992196',
        #  '85244897999896',
        #  '85255893599896',
        #  '85266897999896',
        #  '85277897999896',
        #  '85288237999896',
        #  '85288897999896',
        #  '85299127999896',
        #  '85299237999896',
        #  '85299347999896',
        #  '85299456899896',
        #  '85299457999896',
        #  '85299677999896',
        #  '85299891399896',
        #  '85299893599896',
        #  '85299895799896',
        #  '85299896899896',
        #  '85299897992196',
        #  '85299897993296',
        #  '85299897994396',
        #  '85299897997696',
        #  '85299897998796',
        #  '85299897999896'
        ('95299897999896', 12)
    ]:
        for i in range(10000):
            str_i = get_mutated(current_best_str, 4)
            # if '0' in str_i:
            #     continue
            inputs = [int(d) for d in str_i]
            assert len(inputs) == 14
            alu = ALU()
            for inst in instructions:
                if inst[0] == "inp":
                    alu.inp(inst[1], inputs.pop(0))
                else:
                    getattr(alu, inst[0])(inst[1], inst[2])
            print(alu.z)
            if alu.z == 0:
                short_list.append(str_i)
                # break
            elif alu.z < z_min:
                print(str_i, z_min)
    print(sorted(set(short_list)))
    print(max(short_list))
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    answer = 0
    print(f'Part2: {answer}')


# part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
