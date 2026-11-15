def base_command(point: list):
    # распаковка точки
    x, y, direction, command = point

    # список направлений для команд ")", "("
    directions = ['N', 'E', 'S', 'W']
    ind = directions.index(direction)

    # коэфицент и координаты относительно направления
    if direction == 'N':
        coordinats = [x, y]
        k = [1, 1]
    elif direction == 'S':
        coordinats = [x, y]
        k = [-1, -1]
    elif direction == 'E':
        coordinats = [y, x]
        k = [-1, 1]
    elif direction == 'W':
        coordinats = [y, x]
        k = [1, -1]

    # команды F, B, R, L
    if command == 'F':
        coordinats[1] += k[1]
    elif command == 'B':
        coordinats[1] -= k[1]
    elif command == 'R':
        coordinats[0] += k[0]
    elif command == 'L':
        coordinats[0] -= k[0]

    # распаковка координат
    if direction in 'NS':
        x, y = coordinats
    else:
        y, x = coordinats

    # определение нового направления
    if command == ')':
        if ind == 3:
            direction = 'N'
        else:
            direction = directions[ind + 1]
    elif command == '(':
        if ind == 0:
            direction = 'W'
        else:
            direction = directions[ind - 1]

    return [x, y, direction, command]


def povtor(n, body, point):
    if n == 0:
        return point
    for i in range(n):
        for c in body:
            point[3] = c
            point = base_command(point)
    return point


if __name__ == "__main__":

    commands = input()

    point = [0, 0, 'N', '']

    i = 0
    string_n = ''
    body = ''

    while i < len(commands):
        if commands[i] in 'FRLB)(':
            point[3] = commands[i]
            point = base_command(point)
            i += 1

        elif commands[i].isdigit():
            string_n += commands[i]
            i += 1

        else:
            n = int(string_n)
            string_n = ''

            i += 1
            while commands[i] != ']':
                body += commands[i]
                i += 1

            point = povtor(n, body, point)
            body = ''
            i += 1

    print(point[0], point[1])
