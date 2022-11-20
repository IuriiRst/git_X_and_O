square = [[' '] * 3 for i in (range(3))]        # Игровое поле


def display():      # Вывод игрового поля на экран
    print(f'  0 1 2')
    print(f'0 {square[0][0]} {square[0][1]} {square[0][2]}')
    print(f'1 {square[1][0]} {square[1][1]} {square[1][2]}')
    print(f'2 {square[2][0]} {square[2][1]} {square[2][2]}')


def ask():      # Проверка ввода
    while True:
        _input = input('Сделайте ход --->  ').split()

        if len(_input) != 2:
            print('Введите две цифры координат...')
            continue

        x, y = _input

        if not (x.isdigit()) or not (y.isdigit()):
            print('Введены были не координаты...')
            continue

        x, y = int(x), int(y)

        if 0 < x > 2 or 0 < y > 2:
            print('Введите правильные координаты...')
            continue

        if square[x][y] != " ":
            print('Клетка занята...')
            continue

        return x, y


def wins():     # Определитель победителя
    win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
           ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)), ((0, 0), (1, 0), (2, 0)),
           ((2, 0), (1, 1), (0, 2)), ((0, 0), (1, 1), (2, 2)))

    for i in win:
        test_cells = []

        for f in i:
            test_cells.append(square[f[0]][f[1]])

            if test_cells == ['X', 'X', 'X']:
                print('Поздравляю тебя, X - ты выиграл!')
                return True
            if test_cells == ['0', '0', '0']:
                print('Поздравляю тебя, 0 - ты выиграл!')
                return True
    return False


print('Приветствую вас в нашей игре!!!')
print(' ----- Крестики и Нолики-----')
print('')


for i in range(1, 11):      # Игровой цикл

    display()

    if i > 9:
        print('Никто не выиграл...')
        break

    if i % 2 == 1:
        print('Ход "X" ')
    else:
        print('Ход "0" ')

    x, y = ask()

    if i % 2 == 1:
        square[x][y] = 'X'
    else:
        square[x][y] = '0'

    if wins():
        break









