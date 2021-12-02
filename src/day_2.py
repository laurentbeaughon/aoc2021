from utils import read_word_integer


def part_1(data, verbose):
    x, z = 0, 0
    for command, value in data:
        if command == 'forward':
            x += value
        if command == 'down':
            z += value
        if command == 'up':
            z -= value
        if verbose:
            print(f'going {command} for {value} units, pos is now at ({x};{z})')
    return x*z


def part_2(data, verbose):
    x, z, aim = 0, 0, 0
    for command, value in data:
        if command == 'forward':
            x += value
            z += value * aim
            if verbose:
                print(f'going {command} for {value} units with aim {aim}, pos is now at ({x};{z})')
        if command == 'down':
            aim += value
            if verbose:
                print(f'turning down, aim is now {aim}')
        if command == 'up':
            aim -= value
            if verbose:
                print(f'turning up, aim is now {aim}')
    return x*z


def main(args):
    data = read_word_integer(args.data_file)
    part_1_result = part_1(data, args.verbose)
    part_2_result = part_2(data, args.verbose)
    print(f'part 1 result : {part_1_result}')
    print(f'part 2 result : {part_2_result}')