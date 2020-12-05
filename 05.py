from inputs.input_05 import sample_input, main_input


def generate_parsed_input(raw_input):
    for parsed_input_item in raw_input.split('\n'):
        yield parsed_input_item


def part_1(raw_input):
    for x in generate_parsed_input(raw_input):
        pass


def part_2(raw_input):
    for x in generate_parsed_input(raw_input):
        pass


part_1(sample_input)
# part_1(main_input)


# part_2(sample_input)
# part_2(main_input)

