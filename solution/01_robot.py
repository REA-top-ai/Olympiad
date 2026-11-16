def position(program):
    deg = 90 
    x, y = 0, 0
    stack = []
    i = 0

    while i < len(program):
        command = program[i]
        if command.isdigit():
            start = i
            while program[i].isdigit():
                i += 1
            count = int(program[start:i])
            stack.append((x, y, deg, count))
            x, y = 0, 0
            deg = 90
        elif command == "]":
            dx, dy = x, y
            turn = deg - 90
            x, y, deg, count = stack.pop()
            if turn == 0:
                dx *= count
                dy *= count
                count = 1
            else:
                count %= 4
            for _ in range(count):
                if deg == 90:
                    x += dx
                    y += dy
                elif deg == 0:
                    x += dy
                    y -= dx
                elif deg == 180:
                    x -= dy
                    y += dx
                else:
                    x -= dx
                    y -= dy
                deg = (deg + turn) % 360
        elif command == ")":
            deg = (deg - 90) % 360
        elif command == "(":
            deg = (deg + 90) % 360
        else:
            step_deg = deg
            if command == "B":
                step_deg = (deg + 180) % 360
            elif command == "R":
                step_deg = (deg - 90) % 360
            elif command == "L":
                step_deg = (deg + 90) % 360
            if step_deg == 90:
                y += 1
            elif step_deg == 180:
                x -= 1
            elif step_deg == 270:
                y -= 1
            else:
                x += 1
        i += 1
    return x, y

program = input()
print(*position(program))
