from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_24 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter, defaultdict


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
            pass


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


def part_1(raw_input):
    instructions = get_parsed(raw_input)
    answer = ""
    min_z = float('inf')
    for i in range(10**12 - 1, 0, -1):   # try 98 for 4th to last and 3rd to last digit
        str_i = str(i)
        if '0' in str_i:
            continue
        str_i = str_i[:-2] + '98' + str_i[-2:]
        inputs = [int(d) for d in str_i]
        assert len(inputs) == 14
        alu = ALU()
        for inst in instructions:
            if inst[0] == "inp":
                alu.inp(inst[1], inputs.pop(0))
            else:
                getattr(alu, inst[0])(inst[1], inst[2])
        if alu.z == 0:
            answer = str_i
            break
        else:
            if alu.z < min_z:
                print(str_i, alu.z)
                min_z = alu.z
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    answer = 0
    print(f'Part2: {answer}')


# part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
