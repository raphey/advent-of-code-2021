from utils.utils_07 import gen_raw_items, get_regex_captures, regex, translate
from inputs.input_07 import sample_input, main_input


def gen_parsed(raw_input):
    for raw_item in gen_raw_items(raw_input, split_token='\n'):
        yield raw_item


def part_1(raw_input):
    answer = 0
    for x in gen_parsed(raw_input):
        pass
    print(f'Part1: {answer}')


def part_2(raw_input):
    answer = 0
    for x in gen_parsed(raw_input):
        pass
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
