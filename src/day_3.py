from utils import read_chars


def gamma_rate(data):
    l = len(data)
    sums = [sum([int(line[j]) for line in data]) for j in range(len(data[0]))]
    most_common_bin =  [x > l/2 for x in sums]
    return ''.join(['1' if x else '0' for x in most_common_bin])


def epsilon_rate(gamma_rate):
    return ''.join(['1' if x=='0' else '0' for x in gamma_rate])


def part_1(data, verbose):
    gr = gamma_rate(data)
    er = epsilon_rate(gr)
    int_gr = int(gr, 2)
    int_er = int(er, 2)
    if verbose:
        print(f'gamma_rate = {gr}, epsilon_rate = {er}')
        print(f'gamma_rate = {int_gr}, epsilon_rate = {int_er}')
    return int_gr * int_er


def find_value(data, bit_criteria, step, verbose=False):
    if len(data) == 1:
        return data[0]
    value = sum([int(line[step]) for line in data])
    if bit_criteria == 'most_common':
        if value >= len(data)/2:
            criteria = '1'
        else:
            criteria = '0'
    elif bit_criteria == 'least_common':
        if value >= len(data)/2:
            criteria = '0'
        else:
            criteria = '1'
    data_truncated = [x for x in data if x[step] in criteria]
    if verbose:
        print(f'step {step}')
        print(f'criteria: {criteria}')
        print(f'there are now {len(data_truncated)} values left')
    return find_value(data_truncated, bit_criteria, step+1, verbose)


def part_2(data, verbose):
    ogr = ''.join(find_value(data, 'most_common', 0, verbose))
    csr = ''.join(find_value(data, 'least_common', 0, verbose))
    int_ogr = int(ogr, 2)
    int_csr = int(csr, 2)
    if verbose:
        print(f'oxygen_generator_rating = {ogr}, CO2_scrubber_rating = {csr}')
        print(f'oxygen_generator_rating = {int_ogr}, CO2_scrubber_rating = {int_csr}')
    return int_ogr * int_csr


def main(args):
    data = read_chars(args.data_file)
    part_1_result = part_1(data, args.verbose)
    part_2_result = part_2(data, args.verbose)
    print(f'part 1 result : {part_1_result}')
    print(f'part 2 result : {part_2_result}')