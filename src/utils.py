def read_single_integers(filename):
    with open(filename) as f:
        data = [int(line) for line in f.readlines()]
    return data


def read_word_integer(filename):
    data = []
    with open(filename) as f:
        for line in f.readlines():
            command, value = line.split()
            data.append([command, int(value)])
    return data


def read_chars(filename):
    data = []
    with open(filename) as f:
        for line in f.readlines():
            data.append([char for char in line.strip()])
    return data


def read_bingo(filename):
    boards = []
    with open(filename) as f:
        numbers = [int(num) for num in f.readline().split(',')]
        while f.readline():
            board = []
            for i in range(5):
                board.append([int(num) for num in f.readline().strip().replace("  ", " ").split(" ")])
            boards.append(board)
    return numbers, boards


def read_vents(filename):
    with open(filename) as f:
        data = []
        for line in f.readlines():
            a, b, c, d = [int(i) for x in line.split(' -> ') for i in x.split(',')]
            data.append([a, b, c, d])
    return data


def read_comma_separated_int(filename):
    with open(filename) as f:
        return [int(val) for val in f.readline().split(',')]
