from utils.utils_08 import gen_raw_items, get_regex_search, get_regex_findall, regex, translate
from inputs.input_08 import sample_input, main_input

import re


def gen_parsed(raw_input):
    for i, raw_item in enumerate(gen_raw_items(raw_input, split_token='\n')):
        items = get_regex_search(raw_item, r'(\w+) (\S+)')
        yield items[0], int(items[1])


class GameConsole(object):

    def __init__(self, commands):
        self.commands = commands
        self.accumulator = 0
        self.i = 0
        self.visited = set()
        self.finished = False
        self.command_dict = {
            'acc': self.acc,
            'jmp': self.jmp,
            'nop': self.nop,
        }

    def acc(self, x):
        self.accumulator += x
        self.i += 1

    def jmp(self, x):
        self.i += x

    def nop(self, _):
        self.i += 1

    def should_terminate(self):
        return self.i in self.visited

    def execute_one_command(self):
        self.visited.add(self.i)
        command, amount = self.commands[self.i]
        self.command_dict[command](amount)

    def get_exit_code(self):
        return 0

    def execute(self):
        while not self.should_terminate():
            self.execute_one_command()
        return self.get_exit_code()


class TweakedGameConsole(GameConsole):
    def __init__(self, commands, tweak_j):
        super(TweakedGameConsole, self).__init__(commands)
        self.tweak_j = tweak_j

    def should_terminate(self):
        return self.i in self.visited or self.i >= len(self.commands)

    def execute_one_command(self):
        self.visited.add(self.i)
        command, amount = self.commands[self.i]
        if self.i == self.tweak_j:
            if command == 'jmp':
                command = 'nop'
            elif command == 'nop':
                command = 'jmp'
        self.command_dict[command](amount)

    def get_exit_code(self):
        return 0 if self.i >= len(self.commands) else 1


def part_1(raw_input):
    all_instructions = list(gen_parsed(raw_input))
    gc = GameConsole(all_instructions)
    gc.execute()
    answer = gc.accumulator
    print(f'Part1: {answer}')


def part_2(raw_input):
    all_instructions = list(gen_parsed(raw_input))
    for j in range(len(all_instructions)):
        tgc = TweakedGameConsole(all_instructions, tweak_j=j)
        exit_code = tgc.execute()
        if exit_code == 0:
            break
    answer = tgc.accumulator
    print(f'Part2: {answer}')



part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
