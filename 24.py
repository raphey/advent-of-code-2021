from utils.utils_24 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_24 import GameConsole, TweakedGameConsole, memo
from inputs.input_24 import main_input

from itertools import combinations
import copy
import re
from collections import Counter


dir_key = {
    'e': (2, 0),
    'w': (-2, 0),
    'ne': (1, 1),
    'nw': (-1, 1),
    'se': (1, -1),
    'sw': (-1, -1)
}

def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        dirs = []
        i = 0
        while i < len(raw_item):
            c = raw_item[i]
            i += 1
            if c in 'ns':
                c += raw_item[i]
                i += 1
            dirs.append(dir_key[c])
        parsed.append(dirs)
    return parsed


sample_input_0 = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

sample_input_1 = """"""


def part_1(raw_input):
    flipped = set()
    parsed = get_parsed(raw_input)
    ref = (0, 0)
    for dirs in parsed:
        x, y = ref
        for dx, dy in dirs:
            x += dx
            y += dy
        if (x, y) in flipped:
            flipped.remove((x, y))
        else:
            flipped.add((x, y))
    answer = len(flipped)
    print(f'Part1: {answer}')


def part_2(raw_input, days=100):
    flipped = set()
    parsed = get_parsed(raw_input)
    ref = (0, 0)
    for dirs in parsed:
        x, y = ref
        for dx, dy in dirs:
            x += dx
            y += dy
        if (x, y) in flipped:
            flipped.remove((x, y))
        else:
            flipped.add((x, y))
    for i in range(days):
        print(i)
        new_flipped = set()
        for x in range(-days * 2, days * 2):
            for y in range(-days * 2, days * 2):
                neighbors = 0
                for dx, dy in dir_key.values():
                    if (x + dx, y + dy) in flipped:
                        neighbors += 1
                if (x, y) in flipped and neighbors in (1, 2):
                    new_flipped.add((x, y))
                elif neighbors == 2:
                    new_flipped.add((x, y))
        flipped = new_flipped
    answer = len(flipped)
    print(f'Part2: {answer}')

part_1(sample_input_0)
part_1(main_input)

part_2(sample_input_0)
part_2(main_input)
