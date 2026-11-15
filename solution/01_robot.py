program = input()

x = 0
y = 0
direction = 0

for command in program:
    if command == 'F':
        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        else:
            x -= 1

    elif command == 'B':
        if direction == 0:
            y -= 1
        elif direction == 1:
            x -= 1
        elif direction == 2:
            y += 1
        else:
            x += 1

    elif command == 'R':
        if direction == 0:
            x += 1
        elif direction == 1:
            y -= 1
        elif direction == 2:
            x -= 1
        else:
            y += 1

    elif command == 'L':
        if direction == 0:
            x -= 1
        elif direction == 1:
            y += 1
        elif direction == 2:
            x += 1
        else:
            y -= 1

    elif command == ')':
        direction = (direction + 1) % 4

    elif command == '(':
        direction = (direction - 1) % 4

print(x, y)