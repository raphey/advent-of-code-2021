from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_16 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter


sample_input = """D2FE28"""
sample_input = "8A004A801A8002F478"  # confusing
sample_input = "C0015000016115A2E0802F182340"
# sample_input = "620080001611562C8802118E34"



def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = raw_item
        parsed.append(parsed_item)
    return parsed[0]


def get_packet_version_and_type(packet):
    return int(packet[:3], 2), int(packet[3:6], 2)


def get_subpacket_string_and_end_info(packet):
    assert int(packet[3:6], 2) != 4
    if packet[6] == "0":
        num_length_bits = 15
        length = int(packet[7:7 + num_length_bits], 2)
        return packet[7 + num_length_bits: 7 + num_length_bits + length], None, packet[7 + num_length_bits + length:]
    else:
        num_length_bits = 11
        num_packets = int(packet[7:7 + num_length_bits], 2)
        return packet[7 + num_length_bits:], num_packets, None


def parse_literal_packet(packet_string):
    version, type = get_packet_version_and_type(packet_string)
    assert type == 4
    concat = ""
    i = 6
    while True:
        lead, rest = packet_string[i], packet_string[i + 1: i + 5]
        i += 5
        concat += rest
        if lead == "0":
            break
    remainder = packet_string[i:]
    if len(remainder) < 6:
        remainder = ""
    return version, int(concat, 2), remainder


def parse_nonliteral_packet(packet_string):
    version, type = get_packet_version_and_type(packet_string)
    assert type != 4
    version_total = version
    value_total = 0
    print(f"***nonliteral call on {packet_string}")
    print(version_total, value_total)
    subpacket_string, end_info, remainder = get_subpacket_string_and_end_info(packet_string)
    if end_info is None:
        sub_version_total, sub_value_total = parse(subpacket_string)
        # still could be a remainder
        version_total += sub_version_total
        value_total += sub_value_total
    else:
        for j in range(end_info):
            sub_version_total, sub_value_total, remainder = parse_one(subpacket_string)
            version_total += sub_version_total
            value_total += sub_value_total
            subpacket_string = remainder
    print(f"nonliteral call on {packet_string} returning {(version_total, value_total, remainder)}")
    return version_total, value_total, remainder


def parse_one(packet_string):
    if len(packet_string) < 11:
        return 0, 0, ""
    _, type = get_packet_version_and_type(packet_string)
    if type == 4:
        version_total, value_total, remainder = parse_literal_packet(packet_string)
    else:
        version_total, value_total, remainder = parse_nonliteral_packet(packet_string)
    return version_total, value_total, remainder


def parse(packet_string):
    print('parsing:', packet_string)
    if len(packet_string) < 11:
        return 0, 0
    version_total, value_total, remainder = parse_one(packet_string)
    print(f"parsed one off {packet_string}, now: {(version_total, value_total, remainder)}")
    if remainder:
        subversion_total, subvalue_total = parse(remainder)
        version_total += subversion_total
        value_total += subvalue_total
    return version_total, value_total


# print(parse("110100101111111000101000"))
# print(parse("0101001000100100"))
# print(parse("00111000000000000110111101000101001010010001001000000000"))


def part_1(raw_input):
    parsed = get_parsed(raw_input)
    bits = ""
    for hex_char in parsed:
        bits += str(bin(16 + int(hex_char, 16)))[3:]
    print(bits)
    version_total, value_total = parse(bits)
    answer = version_total
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)

    answer = 0
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
