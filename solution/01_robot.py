command = input()


def movement(x, y, angle):
                                                              
    for i in range(angle):
        x, y = y, -x
    return x, y


def block(position):
    x, y = 0, 0
    angle = 0                                            

    while position < len(command) and command[position] != ']':
        symbol = command[position]

        if symbol.isdigit():
            count = 0
            while position < len(command) and command[position].isdigit():
                count = count * 10 + int(command[position])
                position += 1
            position += 1
            dx, dy, turn, position = block(position)
            position += 1

            if turn == 0:
                dx *= count
                dy *= count
            else:
                                                                    
                period = 2 if turn == 2 else 4
                new_x, new_y = 0, 0
                for i in range(count % period):
                    step_x, step_y = movement(dx, dy, i * turn % 4)
                    new_x += step_x
                    new_y += step_y
                dx, dy = new_x, new_y

            dx, dy = movement(dx, dy, angle)
            x += dx
            y += dy
            angle = (angle + count * turn) % 4
        elif symbol == ')' or symbol == '(':
            if symbol == ')':
                angle = (angle + 1) % 4
            else:
                angle = (angle - 1) % 4
            position += 1
        else:
            if symbol == 'F':
                dx, dy = 0, 1
            elif symbol == 'B':
                dx, dy = 0, -1
            elif symbol == 'R':
                dx, dy = 1, 0
            else:
                dx, dy = -1, 0
            dx, dy = movement(dx, dy, angle)
            x += dx
            y += dy
            position += 1

    return x, y, angle, position


x, y, angle, position = block(0)
print(x, y)
