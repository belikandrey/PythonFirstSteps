from random import randint


def create_matrix(size):
    arr = []
    counter = 1
    for i in range(size):
        row = []
        for j in range(size):
            row.append(counter)
            counter += 1
        arr.append(row)
    return arr


def init(count):
    arr = create_matrix(count)
    arr[len(arr) // 2][len(arr) // 2] = 'X'
    return arr


def print_matrix(arr):
    for i in arr:
        for j in i:
            print(str(j) + '\t', end='')
        print()
    print()


def make_move(arr, val, is_user=False):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == val:
                if is_user:
                    arr[i][j] = 'O'
                else:
                    arr[i][j] = 'X'
                return True
    return False


def get_user_input():
    return input('Enter your move : ')


def validate_user_input(val, count):
    try:
        val = int(val)
    except ValueError:
        return False

    return 1 <= val <= count ** 2


def check_row(arr, i):
    first = arr[i][0]
    for j in range(1, len(arr[i])):
        if arr[i][j] != first:
            return False
    return True


def check_column(arr, i):
    first = arr[0][i]
    for j in range(1, len(arr)):
        if arr[j][i] != first:
            return False
    return True


def check_main_diagonal(arr):
    first = arr[0][0]

    for j in range(1, len(arr)):
        if arr[j][j] != first:
            return False
    return True


def check_side_diagonal(arr):
    first = arr[0][len(arr) - 1]

    for j in range(1, len(arr)):
        if arr[j][len(arr) - j - 1] != first:
            return False
    return True


def print_results(char):
    if char == 'X':
        print('Computer Won!')
    elif char == 'O':
        print('You Won!')
    else:
        print('Friendship Won!')


def check_game_status(arr):
    result = False

    for i in range(len(arr)):
        if check_row(arr, i):
            print_results(arr[i][0])
            result = True

        if check_column(arr, i):
            print_results(arr[0][i])
            result = True

        if check_main_diagonal(arr):
            print_results(arr[0][0])
            result = True

        if check_side_diagonal(arr):
            print_results(arr[0][len(arr[0]) - 1])
            result = True

        if result:
            return result

    valid_moves = get_valid_moves(arr)
    if len(valid_moves) < 1:
        print_results('')
        return True

    return result


def get_valid_moves(arr):
    valid_moves = []
    for i in arr:
        for j in i:
            if j != 'O' and j != 'X':
                valid_moves.append(j)
    return valid_moves


def computer_move(arr):
    valid_moves = get_valid_moves(arr)
    move_ind = randint(0, len(valid_moves) - 1)
    make_move(arr, valid_moves[move_ind])


def user_move(arr):
    val = get_user_input()
    if not validate_user_input(val, len(arr)):
        print('Enter valid number. Must be more than 0 and less than 10')
        return False
    return make_move(arr, int(val), True)


def play(arr):
    is_user_last_move = False

    while not check_game_status(arr):
        if is_user_last_move:
            computer_move(arr)
        else:
            if not user_move(arr):
                continue
        print_matrix(arr)
        is_user_last_move = not is_user_last_move


def validate_game_mode(mode):
    try:
        mode = int(mode)
        if 1 <= mode <= 8:
            return True
    except ValueError:
        return False
    return False


def get_game_mode():
    while True:
        val = input('Enter game mode\n\t1. 3x3\n\t2. 4x4\n\t3. 5x5\n\t4. 6x6\n\t5. 7x7\n\t6. 8x8\n\t7. 9x9\n\t8. '
                    'Exit\n\t')
        if validate_game_mode(val):
            return int(val)
        else:
            print('Enter valid game mode!!!')


def run_game():
    game_mode = get_game_mode()
    if game_mode == 4:
        return
    arr = init(game_mode + 2)
    print_matrix(arr)
    play(arr)


if __name__ == '__main__':
    run_game()
