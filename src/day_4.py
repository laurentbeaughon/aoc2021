from utils import read_bingo


def check(board, num):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == num:
                
                board[y][x] = None
                if (all(board[i][x] is None for i in range(5))
                    or all(board[y][i] is None for i in range(5))):
                    return True
    return False


def score(board, num):
    s = sum(n for line in board for n in line if n)
    return num * s


def part_1(numbers, boards, verbose):
    for num in numbers:
        if verbose:
            print(f"checking number {num}")
        for board in boards:
            if check(board, num):
                if verbose:
                    print(f"board {board} won !")
                return score(board, num)
    return 0


def part_2(numbers, boards, verbose):
    winners = set()
    scores = []
    for num in numbers:
        if verbose:
            print(f"checking number {num}")
        for i, board in enumerate(boards):
            if i in winners:
                continue
            if check(board, num):
                scores.append(score(board, num))
                winners.add(i)
                if verbose:
                    print(f"board {board} won !")
    return scores[-1]

def main(args):
    numbers, boards = read_bingo(args.data_file)
    part_1_result = part_1(numbers, boards, args.verbose)
    part_2_result = part_2(numbers, boards, args.verbose)
    print(f'part 1 result : {part_1_result}')
    print(f'part 2 result : {part_2_result}')