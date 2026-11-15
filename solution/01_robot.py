position = [0, 0, 0]


def movement(i):
    if i == 'F' and position[2] == 0:
        position[1] += 1
    if i == 'F' and position[2] == 1:
        position[0] += 1
    if i == 'F' and position[2] == 2:
        position[1] += -1
    if i == 'F' and position[2] == 3:
        position[0] += -1

    if i == 'B' and position[2] == 0:
        position[1] += -1
    if i == 'B' and position[2] == 1:
        position[0] += -1
    if i == 'B' and position[2] == 2:
        position[1] += 1
    if i == 'B' and position[2] == 3:
        position[0] += 1

    if i == 'R' and position[2] == 0:
        position[0] += 1
    if i == 'R' and position[2] == 1:
        position[1] += -1
    if i == 'R' and position[2] == 2:
        position[0] += -1
    if i == 'R' and position[2] == 3:
        position[1] += 1

    if i == 'L' and position[2] == 0:
        position[0] += -1
    if i == 'L' and position[2] == 1:
        position[1] += 1
    if i == 'L' and position[2] == 2:
        position[0] += 1
    if i == 'L' and position[2] == 3:
        position[1] += -1

    if i == ')':
        position[2] = (position[2] + 1) % 4
    if i == '(':
        position[2] = (position[2] - 1) % 4


def execute(inputdata):
    position = 0
    while position < len(inputdata):
        i = inputdata[position]

        if i in '0123456789':
            count = 0

            while position < len(inputdata) and inputdata[position] in '0123456789':
                count = count * 10 + int(inputdata[position])
                position += 1
            position += 1
            start = position
            come_count = 1

            while come_count > 0:
                if inputdata[position] == '[':
                    come_count += 1
                if inputdata[position] == ']':
                    come_count -= 1
                position += 1

            position1 = inputdata[start:position - 1]

            if position1:
                for j in range(count):
                    execute(position1)

        else:
            movement(i)
            position += 1


inputdata = input()
execute(inputdata)

print(position[0], position[1])