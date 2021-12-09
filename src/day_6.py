from utils import read_comma_separated_int


def preprocess_data(data):
    fishes = {i:0 for i in range(9)}
    for fish in data:
        fishes[fish] += 1
    return fishes


def part_1(data):
    for i in range(80):
        day_0 = data[0]
        for i in range(8):
            data[i] = data[i+1]
        data[6] += day_0
        data[8] = day_0
    print(data)
    return sum(data.values())


def part_2(data):
    for i in range(256-80):
        day_0 = data[0]
        for i in range(8):
            data[i] = data[i+1]
        data[6] += day_0
        data[8] = day_0
    return sum(data.values())


def main(args):
    data = read_comma_separated_int(args.data_file)
    processed_data = preprocess_data(data)
    if args.verbose:
        print(processed_data)
    part_1_result = part_1(processed_data)
    if args.verbose:
        print(processed_data)
    part_2_result = part_2(processed_data)
    if args.verbose:
        print(processed_data)
    print(f'part 1 result : {part_1_result}')
    print(f'part 2 result : {part_2_result}')