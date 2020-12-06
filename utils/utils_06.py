import re


def regex(r_string):
    if 'parser' not in globals():
        global parser
        parser = re.compile(r_string)
    return parser


def translate(string, input_chars, output_chars):
    if 'trans_map' not in globals():
        global trans_map
        trans_map = str.maketrans(input_chars, output_chars)
    return string.translate(trans_map)


def get_regex_captures(string, r_string):
    m = regex(r_string).search(string)
    return m.groups()


def gen_raw_items(raw_input, split_token='\n'):
    for raw_item in raw_input.strip().split(split_token):
        yield raw_item.strip()
