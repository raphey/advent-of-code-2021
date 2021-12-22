from functools import update_wrapper
import re


def decorator(d):
    """Make function d a decorator with the original function name & docstring."""
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d


@decorator
def memo(f):
    """
    Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up.
    """
    cache = {}

    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
    return _f


parser = {}


def regex(r_string):
    if r_string not in parser:
        parsed = re.compile(r_string)
        parser[r_string] = parsed
    return parser[r_string]


def translate(string, input_chars, output_chars):
    if 'trans_map' not in globals():
        global trans_map
        trans_map = str.maketrans(input_chars, output_chars)
    return string.translate(trans_map)


def get_regex_search(string, r_string):
    m = regex(r_string).search(string)
    return m.groups()


def get_regex_findall(string, r_string):
    return regex(r_string).findall(string)


def get_raw_items(raw_input, split_token='\n'):
    raw_items = []
    for raw_item in raw_input.strip().split(split_token):
        raw_items.append(raw_item.strip())
    return raw_items


def get_four_neighbor_indices(grid, i, j):
    i_max = len(grid) - 1
    j_max = len(grid[0]) - 1
    return [(ii, jj) for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
            if 0 <= ii <= i_max and 0 <= jj <= j_max]


def get_eight_neighbor_indices(grid, i, j):
    i_max = len(grid) - 1
    j_max = len(grid[0]) - 1
    return [(ii, jj) for jj in range(j - 1, j + 2) for ii in range(i - 1, i + 2)
            if 0 <= ii <= i_max and 0 <= jj <= j_max and (ii, jj) != (i, j)]


def prod(iterable):
    product = 1
    for x in iterable:
        product *= x
    return product
