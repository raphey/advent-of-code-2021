from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo


from itertools import combinations, permutations
import copy
import re
from collections import Counter, defaultdict


sample_input = (4, 8)

main_input = (6, 1)


def get_parsed(raw_input):
    parsed = []
    scores = [0, 0]
    return parsed


def part_1(raw_input):
    positions = list(raw_input)
    print(positions)
    scores = [0, 0]
    die = 1
    counter = 0
    while True:
        for p in (0, 1):
            for _ in range(3):
                counter += 1
                positions[p] += die
                die = (die % 100) + 1
            positions[p] = (positions[p] - 1) % 10 + 1
            scores[p] += positions[p]
            print(scores)
            if scores[p] >= 1000:
                print(scores, counter, min(scores) * counter)
                return



def part_2(raw_input):
    positions = list(raw_input)
    print(positions)
    position_and_score_counter = defaultdict(int)
    position_and_score_counter[(positions[0], positions[1], 0, 0)] = 1
    triple_roll = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1,
    }
    while any(x < 21 and y < 21 and count > 0 for (_, _, x, y), count in position_and_score_counter.items()):
        for p in (0, 1):
            new_pos_and_score_counter = defaultdict(int)
            for k, v in position_and_score_counter.items():
                if any(score >= 21 for score in (k[2], k[3])):
                    new_pos_and_score_counter[k] += v
                    continue
                for roll, count in triple_roll.items():
                    new_pos_and_score = list(k)
                    new_pos_and_score[p] += roll
                    new_pos_and_score[p] = (new_pos_and_score[p] - 1) % 10 + 1
                    new_pos_and_score[p + 2] += new_pos_and_score[p]
                    new_pos_and_score_counter[tuple(new_pos_and_score)] += v * count
            position_and_score_counter = new_pos_and_score_counter
            print(position_and_score_counter)

    sum_1 = sum(count for (_, _, s1, s2), count in position_and_score_counter.items() if s1 > s2)
    sum_2 = sum(count for (_, _, s1, s2), count in position_and_score_counter.items() if s1 < s2)
    print(sum_1, sum_2)
    print(max(sum_1, sum_2))


# part_1(sample_input)
# part_1(main_input)

part_2(sample_input)
part_2(main_input)
