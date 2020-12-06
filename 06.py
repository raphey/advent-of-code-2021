from utils.utils_06 import gen_raw_items, get_regex_captures, regex, translate
from inputs.input_06 import sample_input, main_input


def gen_parsed(raw_input):
    # Reminder, no solving, just parsing--works for part 1 and part 2
    for raw_item in gen_raw_items(raw_input, split_token='\n\n'):
        yield set(''.join(raw_item.split('\n')))


def gen_parsed_2(raw_input):
    for raw_item in gen_raw_items(raw_input, split_token='\n\n'):
        yield set(x for x in 'abcdefghijklmnopqrstuvwxyz' if all(x in p for p in raw_item.split('\n') if p))

def part_1(raw_input):
    answer = sum(len(x) for x in gen_parsed(raw_input))
    print(f'Part1: {answer}')


def part_2(raw_input):
    print(list(gen_parsed_2(raw_input))[-1])
    answer = sum(len(x) for x in gen_parsed_2(raw_input))
    print(f'Part2: {answer}')


input_debug = """dwqxfekvtn
wknsetqdfxv
dfqknxevtw
edtwfqxvnk
wtfkmrdhevqnx
"""

part_1(sample_input)
part_1(main_input)

# part_2(sample_input)
part_2(main_input)
part_2(input_debug)
