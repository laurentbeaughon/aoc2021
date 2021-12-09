import numpy as np

from utils import read_comma_separated_int



def part_1(data):
    min_fuel = np.sum(np.abs(data - np.median(data)))
    return min_fuel


def part_2(data):
    min_fuel = float("inf")
    for i in range(min(data), max(data) + 1):
        min_fuel = min(min_fuel, sum([abs(i-x) * (abs(i-x) + 1) / 2 for x in data]))
    return min_fuel


def main(args):
    data = np.array(read_comma_separated_int(args.data_file))
    part_1_result = part_1(data)
    part_2_result = part_2(data)
    print(f'part 1 result : {part_1_result}')
    print(f'part 2 result : {part_2_result}')
