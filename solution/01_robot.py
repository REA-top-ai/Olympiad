a = input()
x, y = 0, 0
direction = 0

def run(prog):
    i = 0
    global x, y, direction
    while i < len(prog):
        sim = prog[i]
        if sim == 'F':
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            else:
                x -= 1
        if sim == 'B':
            if direction == 0:
                y -= 1
            elif direction == 1:
                x -= 1
            elif direction == 2:
                y += 1
            else:
                x += 1
        if sim == 'L':
            if direction == 0:
                x -= 1
            elif direction == 1:
                y += 1
            elif direction == 2:
                x += 1
            else:
                y -= 1
        if sim == 'R':
            if direction == 0:
                x += 1
            elif direction == 1:
                y -= 1
            elif direction == 2:
                x -= 1
            else:
                y += 1
        if sim == ')':
            direction = (direction + 1) % 4
        elif sim == '(':
            direction = (direction - 1) % 4
        if sim.isdigit():
            number = 0
            while prog[i].isdigit():
                number = number * 10 + int(prog[i])
                i += 1
            start = i + 1
            d = 1
            i += 1
            while d != 0:
                if prog[i] == '[':
                    d += 1
                elif prog[i] == ']':
                    d -= 1
                i += 1
            body = prog[start:i - 1]
            for n in range(number):
                run(body)
            continue
        i += 1
    return x, y
print(run(a))