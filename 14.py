from utils.utils_14 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_14 import GameConsole, TweakedGameConsole, memo
from inputs.input_14 import main_input

from itertools import combinations
import copy
import re
from collections import Counter


def get_parsed(raw_input):
    parsed = []
    mask_group = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        if raw_item.startswith('mask'):
            if mask_group:
                parsed.append(mask_group)
            mask = raw_item[7:]
            mask_group = []
        else:
            mem_val = get_regex_search(raw_item, r'mem\[(\d+)] = (\d+)')
            mask_group.append((mask, int(mem_val[0]), int(mem_val[1])))
    parsed.append(mask_group)
    return parsed


sample_input_0 = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

# sample_input_1 = """"""


def apply_mask(mask, num):
    num_bin_str = str(bin(num))[2:].zfill(len(mask))
    num_bin_digits = list(num_bin_str)
    for i, (num_d, mask_d) in enumerate(zip(num_bin_digits, mask)):
        if mask_d != 'X':
            num_bin_digits[i] = mask_d
    return int(''.join(num_bin_digits), 2)


# print(apply_mask('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 11))

def part_1(raw_input):
    parsed = get_parsed(raw_input)
    mem_dict = {}
    for x in parsed:
        for mask, mem, val in x:
            mem_dict[mem] = apply_mask(mask, val)
    answer = sum(mem_dict.values())
    print(f'Part1: {answer}')


def get_all_floaties(digit_str):
    # print(digit_str)
    values = []
    if 'X' not in digit_str:
        # print('returning:', [digit_str])
        return [digit_str]
    for i, d in enumerate(digit_str):
        if d == 'X':
            for float_bit in ('0', '1'):
                values += get_all_floaties(digit_str[:i] + float_bit + digit_str[i + 1:])
            break
    # print('returning:', values)
    return values


def apply_mem_mask(mask, mem):
    num_bin_str = str(bin(mem))[2:].zfill(len(mask))
    num_bin_digits = list(num_bin_str)
    print(mask)
    print(num_bin_digits)
    for i, (num_d, mask_d) in enumerate(zip(num_bin_digits, mask)):
        print(i, num_d, mask_d)
        if mask_d == '0':
            continue
        elif mask_d == '1':
            num_bin_digits[i] = '1'
        elif mask_d == 'X':
            num_bin_digits[i] = 'X'
    # print(''.join(num_bin_digits))
    return get_all_floaties(''.join(num_bin_digits))


# apply_mem_mask('000000000000000000000000000000X1001X', 42)


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    mem_dict = {}
    for x in parsed:
        for mask, mem, val in x:
            new_mems = apply_mem_mask(mask, mem)
            print(new_mems)
            for m in new_mems:
                m_int = int(m, 2)
                mem_dict[m_int] = val
    answer = sum(mem_dict.values())

    print(f'Part2: {answer}')


part_1(sample_input_0)
part_1(main_input)

# part_2(sample_input_0)
part_2(main_input)
