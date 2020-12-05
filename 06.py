import re
from inputs.input_05 import sample_input, main_input


def my_regex(regex):
    if 'parser' not in globals():
        global parser
        parser = re.compile(regex)
    return parser


def my_char_trans(string, input_chars, output_chars):
    if 'trans_map' not in globals():
        global trans_map
        trans_map = str.maketrans(input_chars, output_chars)
    return string.translate(trans_map)


def get_regex_captures(string, regex):
    m = my_regex(regex).search(string)
    return m.groups()


def gen_raw_items(raw_input, split_token='\n'):
    for raw_item in raw_input.split(split_token):
        if raw_item:    # watch out for leading/trailing empty strings
            yield raw_item


def gen_parsed(raw_input):
    for raw_item in gen_raw_items(raw_input):
        if not raw_item: continue
        binary = my_char_trans(raw_item, 'FBLR', '0101')
        fbs, lrs = binary[:7], binary[7:]
        yield int(fbs, 2), int(lrs, 2)


def part_1(raw_input):
    answer = max(8 * x + y for x, y in gen_parsed(raw_input))
    print(f'Part1 answer with input of length {len(raw_input)}: {answer}')


def part_2(raw_input):
    ids = {8 * x + y for x, y in gen_parsed(raw_input)}
    for id in ids:
        if id + 1 not in ids and id + 2 in ids:
            answer = id + 1
            break
    print(f'Part2 answer with input of length {len(raw_input)}: {answer}')


part_1(sample_input)
part_1(main_input)

# part_2(sample_input)
part_2(main_input)

