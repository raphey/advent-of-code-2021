from utils.utils_08 import gen_raw_items, get_regex_search, get_regex_findall, regex, translate
from inputs.input_08 import sample_input, main_input

import re


accumulator = 0

def gen_parsed(raw_input):
    for i, raw_item in enumerate(gen_raw_items(raw_input, split_token='\n')):
        items = get_regex_search(raw_item, r'(\w+) (.*)')
        yield items[0], int(items[1])


def part_1(raw_input):
    global accumulator
    accumulator = 0
    all_instructions = list(gen_parsed(raw_input))
    i = 0
    visited = set()
    while True:
        command, value = all_instructions[i]
        if i in visited:
            break
        visited.add(i)
        if command == 'nop':
            i += 1
            continue
        elif command == 'acc':
            accumulator += value
            i += 1
            continue
        elif command == 'jmp':
            i += value
    answer = accumulator
    print(f'Part1: {answer}')


def part_2(raw_input):
    global accumulator
    all_instructions = list(gen_parsed(raw_input))
    finished = False
    for q in range(len(all_instructions)):
        print(q)
        i = 0
        accumulator = 0
        visited = set()
        while True:
            if i == len(all_instructions):
                answer = accumulator
                print(answer)
                finished = True
                break
            command, value = all_instructions[i]
            if i == q:
                if command == 'nop':
                    command = 'jmp'
                elif command == 'jmp':
                    command = 'nop'
            if i in visited:
                break
            visited.add(i)
            if command == 'nop':
                i += 1
                continue
            elif command == 'acc':
                accumulator += value
                i += 1
                continue
            elif command == 'jmp':
                i += value
        if finished:
            break
    print(f'Part2: {answer}')



part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
