from utils import read_vents


def move(t1, t0):
        if t1 == t0:
            return 0
        return abs(t1 - t0) / (t1 - t0)


def part_1(data, verbose):
    map = {}
    for x0, y0, x1, y1 in data:
        if x0 != x1 and y0 != y1:
            continue
        while x0 != x1 or y0 != y1:
            map[(x0, y0)] = map.get((x0, y0), 0) + 1
            x0 += move(x1, x0)
            y0 += move(y1, y0)
        map[(x0, y0)] = map.get((x0, y0), 0) + 1
        if verbose:
            print(f'processing line ({x0}, {y0}) -> ({x1}, {y1})')
    return sum((1 for x in map.values() if x > 1))


def part_2(data, verbose):
    map = {}
    for x0, y0, x1, y1 in data:
        while x0 != x1 or y0 != y1:
            map[(x0, y0)] = map.get((x0, y0), 0) + 1
            x0 += move(x1, x0)
            y0 += move(y1, y0)
        map[(x0, y0)] = map.get((x0, y0), 0) + 1
        if verbose:
            print(f'processing line ({x0}, {y0}) -> ({x1}, {y1})')
    return sum((1 for x in map.values() if x > 1))


def main(args):
    data = read_vents(args.data_file)
    part_1_result = part_1(data, args.verbose)
    part_2_result = part_2(data, args.verbose)
    print(f'part 1 result : {part_1_result}')
    print(f'part 2 result : {part_2_result}')