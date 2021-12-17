from utils.utils_25 import get_raw_items, get_regex_search, get_regex_findall, regex, translate
from utils.utils_25 import memo
from inputs.input_16 import main_input

from itertools import combinations, permutations
import copy
import re
from collections import Counter


sample_input = """D2FE28"""  # 6
sample_input = "8A004A801A8002F478"  # 16
sample_input = "620080001611562C8802118E34"
sample_input = "C0015000016115A2E0802F182340"
sample_input = "A0016C880162017C3686B18A3D4780"



def get_parsed(raw_input):
    parsed = []
    for raw_item in get_raw_items(raw_input, split_token='\n'):
        parsed_item = raw_item
        parsed.append(parsed_item)
    return parsed[0]


def get_packet_version_and_type(packet):
    return int(packet[:3], 2), int(packet[3:6], 2)


class Packet:
    def __init__(self, bits):
        self.version, self.type = get_packet_version_and_type(bits)
        self.bits = bits
        self.subpackets = []

    def get_remainder(self):
        raise NotImplemented

    def get_version_total(self):
        raise NotImplemented

    def evaluate(self):
        raise NotImplemented

    def __repr__(self):
        return str((self.version, self.type, self.bits, self.subpackets))


class ValuePacket(Packet):
    def __init__(self, bits):
        super().__init__(bits)
        assert self.type == 4
        self.value_bits = list(self.generate_value_bits())

    def generate_value_bits(self):
        i = 6
        while True:
            lead_bit, value_bits = self.bits[i], self.bits[i + 1: i + 5]
            yield value_bits
            i += 5
            if lead_bit == "0":
                break

    def get_remainder(self):
        remainder_start = 6 + 5 * len(self.value_bits)
        remainder = self.bits[remainder_start:]
        if len(remainder) < 11:
            remainder = ""
        return remainder

    def get_version_total(self):
        return self.version

    def evaluate(self):
        return int(''.join(self.value_bits), 2)


class OperatorPacket(Packet):
    def __init__(self, bits):
        super().__init__(bits)
        assert self.type != 4
        self.length_type = bits[6]
        self.remainder = None
        self.set_subpackets_lti_zero() if self.length_type == "0" else self.set_subpackets_lti_one()

    def get_remainder(self):
        return self.remainder

    def set_subpackets_lti_zero(self):
        subpacket_bit_count = int(self.bits[7:22], 2)
        to_parse = self.bits[22: 22 + subpacket_bit_count:]
        # print(to_parse)
        # print('to parse:', to_parse)
        while len(to_parse) >= 11:
            subpacket = get_packet(to_parse)
            to_parse = subpacket.get_remainder()
            self.subpackets.append(subpacket)
        self.remainder = self.bits[22 + subpacket_bit_count:]
        if len(self.remainder) < 11:
            self.remainder = ""

    def set_subpackets_lti_one(self):
        subpacket_count = int(self.bits[7:18], 2)
        to_parse = self.bits[18:]
        for i in range(subpacket_count):
            subpacket = get_packet(to_parse)
            to_parse = subpacket.get_remainder()
            self.subpackets.append(subpacket)
        self.remainder = to_parse
        if len(self.remainder) < 11:
            self.remainder = ""

    def get_remainder(self):
        return self.remainder

    def get_version_total(self):
        return self.version + sum(sp.get_version_total() for sp in self.subpackets)

    def evaluate(self):
        raise NotImplemented


class SumPacket(OperatorPacket):
    def evaluate(self):
        return sum(sp.evaluate() for sp in self.subpackets)


class ProductPacket(OperatorPacket):
    def evaluate(self):
        product = 1
        for sp in self.subpackets:
            product *= sp.evaluate()
        return product


class MinimumPacket(OperatorPacket):
    def evaluate(self):
        return min(sp.evaluate() for sp in self.subpackets)


class MaximumPacket(OperatorPacket):
    def evaluate(self):
        return max(sp.evaluate() for sp in self.subpackets)


class GreaterThanPacket(OperatorPacket):
    def evaluate(self):
        v1 = self.subpackets[0].evaluate()
        v2 = self.subpackets[1].evaluate()
        return int(v1 > v2)


class LessThanPacket(OperatorPacket):
    def evaluate(self):
        v1 = self.subpackets[0].evaluate()
        v2 = self.subpackets[1].evaluate()
        return int(v1 < v2)


class EqualToPacket(OperatorPacket):
    def evaluate(self):
        v1 = self.subpackets[0].evaluate()
        v2 = self.subpackets[1].evaluate()
        return int(v1 == v2)


def get_packet(bits):
    # print(f"get_packet called with {bits}")
    _, packet_type = get_packet_version_and_type(bits)
    packet_type_list = [
        SumPacket,
        ProductPacket,
        MinimumPacket,
        MaximumPacket,
        ValuePacket,
        GreaterThanPacket,
        LessThanPacket,
        EqualToPacket
    ]
    return packet_type_list[packet_type](bits)



vp = ValuePacket('110100101111111000101000')

# print(vp)
# print(vp.evaluate())

# op = OperatorPacket('00111000000000000110111101000101001010010001001000000000')
# print(op)

# op2 = OperatorPacket('11101110000000001101010000001100100000100011000001100000')
# print(op2)

# op3 = OperatorPacket('101010000000000000101111010001111000')
# print(op3)
# quit()


def part_1(raw_input):
    parsed = get_parsed(raw_input)
    bits = ""
    for hex_char in parsed:
        bits += str(bin(16 + int(hex_char, 16)))[3:]
    packet = get_packet(bits)
    answer = packet.get_version_total()
    print(f'Part1: {answer}')


def part_2(raw_input):
    parsed = get_parsed(raw_input)
    bits = ""
    for hex_char in parsed:
        bits += str(bin(16 + int(hex_char, 16)))[3:]
    packet = get_packet(bits)
    answer = packet.evaluate()
    print(f'Part2: {answer}')


part_1(sample_input)
part_1(main_input)

part_2(sample_input)
part_2(main_input)
