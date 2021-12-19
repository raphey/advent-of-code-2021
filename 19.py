from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_19 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter


sample_input = """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14"""


def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n\n'):
        parsed_item = [tuple(int(x) for x in line.split(',')) for line in raw_item.split('\n')[1:]]
        parsed.append(parsed_item)
    return parsed


def get_transformation_fn(tm):
    def transform(triple):
        x, y, z = triple
        new_x = tm[0][0] * x + tm[0][1] * y + tm[0][2] * z
        new_y = tm[1][0] * x + tm[1][1] * y + tm[1][2] * z
        new_z = tm[2][0] * x + tm[2][1] * y + tm[2][2] * z
        return new_x, new_y, new_z
    return transform



def get_all_3d_transformations():
    transformation_matrices = [
        # all preserved
        ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
        # rot around z axis
        ((0, 1, 0), (-1, 0, 0), (0, 0, 1)),
        ((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
        ((0, -1, 0), (1, 0, 0), (0, 0, 1)),
        # rot around x axis
        ((1, 0, 0), (0, 0, -1), (0, 1, 0)),
        ((1, 0, 0), (0, -1, 0), (0, 0, -1)),
        ((1, 0, 0), (0, 0, 1), (0, -1, 0)),
        # rot around y axis
        ((0, 0, -1), (0, 1, 0), (1, 0, 0)),
        ((-1, 0, 0), (0, 1, 0), (0, 0, -1)),
        ((0, 0, 1), (0, 1, 0), (-1, 0, 0)),
        # 6 edge-preserving flips
        ((0, 1, 0), (1, 0, 0), (0, 0, -1)),
        ((0, -1, 0), (-1, 0, 0), (0, 0, -1)),
        ((0, 0, 1), (0, -1, 0), (1, 0, 0)),
        ((0, 0, -1), (0, -1, 0), (-1, 0, 0)),
        ((-1, 0, 0), (0, 0, 1), (0, 1, 0)),
        ((-1, 0, 0), (0, 0, -1), (0, -1, 0)),
        # 8 long diagonal rotations
        ((0, 1, 0), (0, 0, 1), (1, 0, 0)),
        ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
        ((0, 0, -1), (1, 0, 0), (0, -1, 0)),
        ((0, 1, 0), (0, 0, -1), (-1, 0, 0)),
        ((0, 0, -1), (-1, 0, 0), (0, 1, 0)),
        ((0, -1, 0), (0, 0, 1), (-1, 0, 0)),
        ((0, 0, 1), (-1, 0, 0), (0, -1, 0)),
        ((0, -1, 0), (0, 0, -1), (1, 0, 0)),
    ]
    all_transformations = []
    for tm in transformation_matrices:
        # new_coords = []
        # for x, y, z in coordinate_list:
        #     new_x = tm[0][0] * x + tm[0][1] * y + tm[0][2] * z
        #     new_y = tm[1][0] * x + tm[1][1] * y + tm[1][2] * z
        #     new_z = tm[2][0] * x + tm[2][1] * y + tm[2][2] * z
        #     new_coords.append((new_x, new_y, new_z))
        # all_transformations.append(new_coords)
        all_transformations.append(get_transformation_fn(tm))
    return all_transformations


def get_all_shifts(coordinate_list, size=100):
    all_shifts = []
    for i in range(-size, size + 1):
        for j in range(-size, size + 1):
            for k in range(-size, size + 1):
                shifted_list = [(x + i, y + j, z + k) for x, y, z in coordinate_list]
                all_shifts.append(shifted_list)
    return all_shifts


def get_all_pairing_transformations(coords_1, coords_2):
    for x1, y1, z1 in coords_1:
        for triple in coords_2:
            for trans in get_all_3d_transformations():
                x2, y2, z2 = trans(triple)
                dx, dy, dz = x1 - x2, y1 - y2, z1 - z2
                yield [(x + dx, y + dy, z + dz) for x, y, z in trans]


def get_trans_and_shift_fn(trans_fn, dx, dy, dz):
    def trans_and_shift_fn(triple):
        tx, ty, tz = trans_fn(triple)
        return tx + dx, ty + dy, tz + dz
    return trans_and_shift_fn


def get_all_pairing_transforms(coords_1, coords_2):
    for x1, y1, z1 in coords_1:
        for triple in coords_2:
            for trans in get_all_3d_transformations():
                x2, y2, z2 = trans(triple)
                dx, dy, dz = x1 - x2, y1 - y2, z1 - z2
                yield get_trans_and_shift_fn(trans, dx, dy, dz)


transformation_test = [(-1,-1,1),
                       (-2,-2,2),
                       (-3,-3,3),
                       (-2,-3,1),
                       (5,6,-4),
                       (8,0,7),]
# for trans in get_all_3d_transformations(transformation_test):
#     print(trans)


def part_1(raw_input):
    scanners = get_parsed(raw_input)
    trans_dict = {}
    for q in range(len(scanners)):
        q_coords = scanners[q]
        q_set = set(q_coords)
        for r in range(len(scanners)):
            if r == q:
                continue
            r_coords = scanners[r]
            for trans in get_all_pairing_transforms(q_coords, r_coords):
                trans_set = set(trans(triple) for triple in r_coords)
                intersection = q_set.intersection(trans_set)
                if len(intersection) >= 12:
                    print(f"scanner {q} intersects with scanner {r}")
                    min_x = min(x for x, y, z in trans_set)
                    max_x = max(x for x, y, z in trans_set)
                    min_y = min(y for x, y, z in trans_set)
                    max_y = max(y for x, y, z in trans_set)
                    min_z = min(z for x, y, z in trans_set)
                    max_z = max(z for x, y, z in trans_set)
                    if any(((x, y, z) not in trans_set and min_x <= x <= max_x and min_y <= y <= max_y and min_z <= z <= max_z) for x, y, z in q_set):
                        print('False intersection!')
                        break
                    trans_dict[(r, q)] = trans
                    break
    paths_to_zero = {0: []}
    while len(paths_to_zero) < len(scanners):
        for (a, b), fn in trans_dict.items():
            if a in paths_to_zero:
                continue
            if b == 0:
                paths_to_zero[a] = [fn]
            elif b in paths_to_zero:
                paths_to_zero[a] = [fn] + paths_to_zero[b]
    print(paths_to_zero)
    beacons = set(scanners[0])
    for i in range(len(scanners)):
        current = scanners[i]
        for fn in paths_to_zero[i]:
            current = [fn(triple) for triple in current]
        beacons.update(current)
    answer = len(beacons)
    print(f'Part1: {answer}')


test_list = [(10, 0), (16, 0), (18, 0), (8, 1), (7, 2), (8, 2), (14, 2), (21, 2), (13, 3), (17, 3), (28, 3), (28, 4), (11, 5), (27, 5), (31, 5), (10, 6), (15, 6), (16, 6), (30, 6), (2, 7), (18, 7), (20, 7), (24, 7), (1, 8), (2, 8), (18, 9), (24, 9), (0, 10), (6, 10), (21, 10), (27, 10), (31, 10), (5, 11), (15, 11), (26, 11), (32, 11), (14, 12), (19, 12), (23, 12), (3, 13), (25, 13), (2, 14), (12, 14), (24, 14), (29, 14), (6, 15), (11, 15), (17, 15), (28, 15), (31, 15), (0, 16), (6, 16), (3, 17), (15, 17), (25, 17), (26, 17), (0, 18), (7, 18), (9, 18), (21, 18), (12, 19), (7, 20), (22, 20), (2, 21), (10, 21), (18, 21), (20, 22), (24, 22), (12, 23), (7, 24), (9, 24), (14, 24), (22, 24), (13, 25), (17, 25), (11, 26), (17, 26), (5, 27), (10, 27), (33, 27), (3, 28), (4, 28), (15, 28), (32, 28), (14, 29), (6, 30), (5, 31), (10, 31), (15, 31), (11, 32), (28, 32), (27, 33)]

print(len(test_list))

def part_2(raw_input):
    scanners = get_parsed(raw_input)
    trans_dict = {}
    for q in range(len(scanners)):
        q_coords = scanners[q]
        q_set = set(q_coords)
        for r in range(len(scanners)):
            if r == q:
                continue
            r_coords = scanners[r]
            for trans in get_all_pairing_transforms(q_coords, r_coords):
                trans_set = set(trans(triple) for triple in r_coords)
                intersection = q_set.intersection(trans_set)
                if len(intersection) >= 12:
                    print(f"scanner {q} intersects with scanner {r}")
                    min_x = min(x for x, y, z in trans_set)
                    max_x = max(x for x, y, z in trans_set)
                    min_y = min(y for x, y, z in trans_set)
                    max_y = max(y for x, y, z in trans_set)
                    min_z = min(z for x, y, z in trans_set)
                    max_z = max(z for x, y, z in trans_set)
                    if any(((x, y, z) not in trans_set and min_x <= x <= max_x and min_y <= y <= max_y and min_z <= z <= max_z) for x, y, z in q_set):
                        print('False intersection!')
                        break
                    trans_dict[(r, q)] = trans
                    break
    paths_to_zero = {0: []}
    while len(paths_to_zero) < len(scanners):
        for (a, b), fn in trans_dict.items():
            if a in paths_to_zero:
                continue
            if b == 0:
                paths_to_zero[a] = [fn]
            elif b in paths_to_zero:
                paths_to_zero[a] = [fn] + paths_to_zero[b]
    scanner_locations = [(0, 0, 0)]
    for i in range(len(scanners)):
        current = (0, 0, 0)
        for fn in paths_to_zero[i]:
            current = fn(current)
        scanner_locations.append(current)
    mmd = 0
    for (x1, y1, z1), (x2, y2, z2) in combinations(scanner_locations, 2):
        md = abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)
        mmd = max(md, mmd)
    answer = mmd
    print(f'Part2: {answer}')


# part_1(sample_input)
# part_1(main_input)

part_2(sample_input)
part_2(main_input)
