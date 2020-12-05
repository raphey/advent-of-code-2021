import re
from inputs.input_05 import sample_input, main_input


def get_regex_captures(string, regex):
    if 'parser' not in globals():
        global parser
        parser = re.compile(regex)
    m = parser.search(string)
    return m.groups()


def generate_parsed_input(raw_input):
    for raw_input_item in raw_input.split('\n'):
        if not raw_input_item: continue
        fbs, lrs = raw_input_item[:7], raw_input_item[7:]
        yield (int(fbs.replace('F', '0').replace('B', '1'), 2),
               int(lrs.replace('L', '0').replace('R', '1'), 2))


def part_1(raw_input):
    print('Part 1')
    max_id = 0
    for x, y in generate_parsed_input(raw_input):
        id = 8 * x + y
        max_id = max(max_id, id)
    print(max_id)


def part_2(raw_input):
    print('Part 2')
    ids = sorted([8 * x + y for x, y in generate_parsed_input(raw_input)])
    id_set = set(ids)
    for id in ids:
        if id + 1 not in id_set and id + 2 in id_set:
            print(id + 1)


part_1(sample_input)
part_1(main_input)

# part_2(sample_input)
part_2(main_input)

