from inputs.input_03 import sample_input, main_input


"""
In our extended array, in row i, the occupied position j is equal to 3*i.
So in the original array, occupied position is 3 * i % w, width of original array.
"""


def part_1(raw_input_map):
    parsed_input_map = raw_input_map.split('\n')
    w = len(parsed_input_map[0])
    return sum(row[3 * i % w] == '#' for i, row in enumerate(parsed_input_map))


print(part_1(sample_input))
print(part_1(main_input))


def part_2(raw_input_map):
    product = 1
    parsed_input_map = raw_input_map.split('\n')
    w = len(parsed_input_map[0])
    for j, k in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        product *= sum(parsed_input_map[i][j * i // k % w] == '#'
                       for i in range(0, len(parsed_input_map), k))
        print(product)
    return product


print(part_2(sample_input))
print(part_2(main_input))

