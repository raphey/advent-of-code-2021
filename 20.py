from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_20 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter


sample_input = """

..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""


def get_parsed(raw_input):
    parsed = []
    sections = get_raw_items(raw_input, split_token='\n\n')
    initial_image = sections[1].split('\n')
    enhancer = sections[0]
    return enhancer, initial_image


def apply_enhancement(image_set, enhancer):
    new_image_set = set()
    to_check = set()
    for i, j in image_set:
        for a in (i - 1, i, i + 1):
            for b in (j - 1, j, j + 1):
                to_check.add((a, b))
    # print("to_check")
    # print(to_check)
    for i, j in to_check:
        lookup = ""
        for a in (i - 1, i, i + 1):
            for b in (j - 1, j, j + 1):
                lookup += "1" if (a, b) in image_set else "0"
        lookup_index = int(lookup, 2)
        new_pixel = enhancer[lookup_index]
        if new_pixel == "#":
            new_image_set.add((a, b))
        # if (i, j) == (2, 2):
        #     print(lookup)
        #     print(lookup_index)
        #     print(new_pixel)
        #     quit()
    return new_image_set


def apply_enhancement_and_flip(image_set, enhancer):
    flipped_image_set = set()
    to_check = set()
    for i, j in image_set:
        for a in (i - 1, i, i + 1):
            for b in (j - 1, j, j + 1):
                to_check.add((a, b))
    # print("to_check")
    # print(to_check)
    for i, j in to_check:
        lookup = ""
        for a in (i - 1, i, i + 1):
            for b in (j - 1, j, j + 1):
                lookup += "1" if (a, b) in image_set else "0"
        lookup_index = int(lookup, 2)
        new_pixel = enhancer[lookup_index]
        if new_pixel == ".":
            flipped_image_set.add((a, b))
        # if (i, j) == (2, 2):
        #     print(lookup)
        #     print(lookup_index)
        #     print(new_pixel)
        #     quit()
    return flipped_image_set


def apply_enhancement_and_flip_back(image_set, enhancer):
    flipped_image_set = set()
    to_check = set()
    for i, j in image_set:
        for a in (i - 1, i, i + 1):
            for b in (j - 1, j, j + 1):
                to_check.add((a, b))
    # print("to_check")
    # print(to_check)
    for i, j in to_check:
        lookup = ""
        for a in (i - 1, i, i + 1):
            for b in (j - 1, j, j + 1):
                lookup += "0" if (a, b) in image_set else "1"
        lookup_index = int(lookup, 2)
        new_pixel = enhancer[lookup_index]
        if new_pixel == "#":
            flipped_image_set.add((a, b))
        # if (i, j) == (2, 2):
        #     print(lookup)
        #     print(lookup_index)
        #     print(new_pixel)
        #     quit()
    return flipped_image_set


def part_1(raw_input):
    enhancer, initial_image = get_parsed(raw_input)
    current_image_set = set()
    for i in range(len(initial_image)):
        for j in range(len(initial_image[0])):
            if initial_image[i][j] == "#":
                current_image_set.add((i, j))
    print(len(current_image_set))
    # print("initial_image_set:")
    # print(current_image_set)
    current_image_set = apply_enhancement_and_flip(current_image_set, enhancer)
    current_image_set = apply_enhancement_and_flip_back(current_image_set, enhancer)
    # for q in range(2):
    #     current_image_set = apply_enhancement(current_image_set, enhancer)
    #     print(len(current_image_set))
    answer = len(current_image_set)
    print(f'Part1: {answer}')


def part_2(raw_input):
    enhancer, initial_image = get_parsed(raw_input)
    current_image_set = set()
    for i in range(len(initial_image)):
        for j in range(len(initial_image[0])):
            if initial_image[i][j] == "#":
                current_image_set.add((i, j))
    print(len(current_image_set))
    # print("initial_image_set:")
    # print(current_image_set)
    for i in range(25):
        current_image_set = apply_enhancement_and_flip(current_image_set, enhancer)
        current_image_set = apply_enhancement_and_flip_back(current_image_set, enhancer)
    # for q in range(2):
    #     current_image_set = apply_enhancement(current_image_set, enhancer)
    #     print(len(current_image_set))
    answer = len(current_image_set)
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
