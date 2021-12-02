from utils import read_single_integers


def part_1(data, verbose):
    cpt = 0
    last_depth = data[0]
    for depth in data:
        if depth > last_depth:
            cpt += 1
        last_depth = depth
    return cpt


def part_2(data, verbose):
    cpt = 0
    A_depth, B_depth, C_depth = data[0], data[1], data[2]
    for depth in data[3:]:
        D_depth = depth
        if B_depth + C_depth + D_depth > A_depth + B_depth + C_depth:
            cpt += 1
        A_depth, B_depth, C_depth = B_depth, C_depth, D_depth
    return cpt


def main(args):
    data = read_single_integers(args.data_file)
    print(part_1(data, args.verbose))
    print(part_2(data, args.verbose))