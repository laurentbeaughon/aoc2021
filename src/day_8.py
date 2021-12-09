from itertools import groupby
from utils import read_seven_segment
from tqdm import tqdm


_LETTERS_ = 'abcdefg'
_DIGITS_ = {
    'cf': '1',
    'acf': '7',
    'bcdf': '4',
    'acdeg': '2',
    'acdfg': '3',
    'abdfg': '5',
    'abcefg': '0',
    'abdefg': '6',
    'abcdfg': '9',
    'abcdefg': '8',
}
_CLUES_BY_LENGTH_ = {
    2: 'cf',
    3: 'acf',
    4: 'bcdf',
    5: 'adg',
    6: 'abfg',
    7: 'abcdefg',
}

def match_pos(line):
    possible_match = {x: set(_LETTERS_) for x in _LETTERS_}
    for word in line[0]:
        for letter in _CLUES_BY_LENGTH_[len(word)]:
            possible_match[letter] = possible_match[letter].intersection(set(word))
    # We might still have letters with multiple possible segments,
    # but we know that there is only one solution.
    # We then take the first working match.
    known = {}
    while any(possible_match.values()):
        all_known = set(known.values())
        for letter, possibilities in possible_match.items():
            possibilities -= all_known
            if len(possibilities) == 1:
                known[letter] = possibilities.pop()
    # reverse the matching for easier translation
    match = {letter: trans for trans, letter in known.items()}
    return match


def part_1(data):
    cpt = 0
    for line in data:
        dig_1 = sum([len(code) == 2 for code in line[1]])
        dig_4 = sum([len(code) == 4 for code in line[1]])
        dig_7 = sum([len(code) == 3 for code in line[1]])
        dig_8 = sum([len(code) == 7 for code in line[1]])
        cpt += dig_1 + dig_4 + dig_7 + dig_8
    return cpt


def part_2(data):
    cpt = 0
    for line in tqdm(data):
        match = match_pos(line)
        number = "".join(
            _DIGITS_["".join(sorted([match[letter] for letter in word]))]
            for word in line[1]
        )
        cpt += int(number)
    return cpt

def main(args):
    data = read_seven_segment(args.data_file)
    part_1_result = part_1(data)
    part_2_result = part_2(data)
    print(f'part 1 result : {part_1_result}')
    print(f'part 2 result : {part_2_result}')
