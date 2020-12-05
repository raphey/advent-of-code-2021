import re


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
