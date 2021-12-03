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
