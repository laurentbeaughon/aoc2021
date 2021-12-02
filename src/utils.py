def read_single_integers(filename):
    with open(filename) as f:
        data = [int(line) for line in f.readlines()]
    return data