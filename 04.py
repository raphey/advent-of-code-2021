from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_04 import main_input

from itertools import combinations
import copy
import re
from collections import Counter


def strip_int(x):
    if x[0] == ' ':
        return int(x[1:])
    return int(x)

def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n\n'):
        parsed_item = raw_item
        parsed.append(parsed_item)
    print(parsed[0])
    numbers = [int(x) for x in parsed[0].split(',')]
    boards = [[[strip_int(x) for x in line.split()] for line in chunk.split('\n')] for chunk in parsed[1:]]
    return numbers, boards


sample_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


def check_for_bingo(board):
    for i in range(len(board[0])):
        if all(x == "X" for x in board[i]):
            return True
    for j in range(len(board)):
        if all(row[j] == "X" for row in board):
            return True
    return False


def part_1(raw_input):
    numbers, boards = get_parsed(raw_input)
    board_sums = [sum(sum(line) for line in b) for b in boards]
    print(board_sums)
    print(numbers)
    print(boards)
    answer = 0
    for x in numbers:
        for k in range(len(boards)):
            b = boards[k]
            for i in range(len(b)):
                for j in range(len(b[0])):
                    if b[i][j] == x:
                        b[i][j] = 'X'
                        board_sums[k] -= x
            if check_for_bingo(boards[k]):
                print("bingo!")
                answer = board_sums[k] * x
                print(f'Part1: {answer}')
                return

    print(f'Part1: no answer')


def part_2(raw_input):
    numbers, boards = get_parsed(raw_input)
    board_sums = [sum(sum(line) for line in b) for b in boards]
    print(board_sums)
    print(numbers)
    print(boards)
    answer = 0
    for x in numbers:
        for k in range(len(boards)):
            b = boards[k]
            for i in range(len(b)):
                for j in range(len(b[0])):
                    if b[i][j] == x:
                        b[i][j] = 'X'
                        board_sums[k] -= x
            if all(check_for_bingo(b) for b in boards):
                print("final bingo!")
                answer = board_sums[k] * x
                print(f'Part2: {answer}')
                return


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)


