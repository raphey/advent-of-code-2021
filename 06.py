from utils.utils_06 import gen_raw_items, get_regex_captures, my_regex, my_char_trans
from inputs.input_06 import sample_input, main_input


def gen_parsed(raw_input):
    for raw_item in gen_raw_items(raw_input):
        binary = my_char_trans(raw_item, 'FBLR', '0101')
        fbs, lrs = binary[:7], binary[7:]
        yield int(fbs, 2), int(lrs, 2)


def part_1(raw_input):
    for x in gen_parsed(raw_input):
        pass
    answer = 0
    print(f'Part1: {answer}')


def part_2(raw_input):
    for x in gen_parsed(raw_input):
        pass
    answer = 0
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)

