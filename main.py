def validate_user_input(val):
    try:
        val = int(val)
        return 1 <= val <= 3
    except ValueError:
        return False


def print_user_menu():
    print('What do you choose?', '1. Draw a square', '2. Draw a tower upside down', '3. Stop', sep="\n\t")


def get_user_input():
    print_user_menu()
    return input()


def get_user_dimension():
    return input('Give a dimension for your construction : ')


def validate_user_dimension(dimension):
    try:
        dimension = int(dimension)
        return dimension > 0
    except ValueError:
        return False


def draw_square(dimension):
    for i in range(dimension):
        for j in range(dimension * 2):
            print(chr(9608), end='')
        print()


def draw_tower(dimension):
    last_size = dimension
    while last_size > 0:
        print((' ' * ((dimension - last_size) // 2)) + (chr(9608) * last_size))
        last_size -= 2


def run():
    while True:
        val = get_user_input()

        if not (validate_user_input(val)):
            print('Enter a valid choice : 1, 2 or 3!')
            continue

        val = int(val)

        if val == 3:
            print('Thanks for playing with us!')
            return

        while True:
            dimension = get_user_dimension()
            if validate_user_dimension(dimension):
                break
            else:
                print('Enter a valid dimension, must be > 0')
        dimension = int(dimension)
        if val == 1:
            draw_square(dimension)
        elif val == 2:
            draw_tower(dimension)


if __name__ == '__main__':
    run()
