from inputs.input_04 import sample_input, main_input, valid_passports, invalid_passports

# Messy, trying for speed (30m)


def part_1(raw_input):
    passports = [dict(keyval.split(':') for keyval in passport.split()) for passport in raw_input.split('\n\n')]
    required_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        # 'cid',    # not required
    ]
    return len([p for p in passports if all(k in p for k in required_fields)])


validation_fns = {
        'byr': lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
        'iyr': lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
        'eyr': lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
        'hgt': lambda x: (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193) or (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76),
        'hcl': lambda x: x[0] == '#' and all(d in '1234567890abcdef' for d in x[1:]),
        'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        'pid': lambda x: len(x) == 9 and all(d in '1234567890' for d in x),
        # 'cid',    # not required
    }


def is_passport_valid(passport_dict):
    return all(field in passport_dict and fn(passport_dict[field]) for field, fn in validation_fns.items())


def part_2(raw_input):
    passports = [dict(keyval.split(':') for keyval in passport.split()) for passport in raw_input.split('\n\n')]
    print(f'total number of passports: {len(passports)}')
    return len([p for p in passports if is_passport_valid(p)])


def print_validity(raw_input):
    passports = [dict(keyval.split(':') for keyval in passport.split()) for passport in raw_input.split('\n\n')]
    print([is_passport_valid(p) for p in passports])


print(part_1(sample_input))
print(part_1(main_input))


print_validity(valid_passports)
print_validity(invalid_passports)


print(part_2(sample_input))
print(part_2(main_input))

