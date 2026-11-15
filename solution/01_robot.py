import sys

s = sys.stdin.readline().strip()
n = len(s)
pos = 0

DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]

def compose(a, b):
    result = []
    for d in range(4):
        x1, y1, r1 = a[d]
        x2, y2, r2 = b[r1]
        result.append((x1 + x2, y1 + y2, r2))
    return result

def power(a, count):
    result = [(0, 0, d) for d in range(4)]
    while count:
        if count % 2 != 0:
            result = compose(result, a)
        a = compose(a, a)
        count //= 2
    return result

def parse_program():
    global pos
    result = [(0, 0, d) for d in range(4)]

    while pos < n and s[pos] != ']':
        ch = s[pos]
        if ch.isdigit():
            count = 0
            while pos < n and s[pos].isdigit():
                count = count * 10 + int(s[pos])
                pos += 1
            pos += 1
            body = parse_program()
            pos += 1
            part = power(body, count)
        else:
            pos += 1
            part = []
            for d in range(4):
                if ch == 'F':
                    part.append((DX[d], DY[d], d))
                elif ch == 'B':
                    part.append((-DX[d], -DY[d], d))
                elif ch == 'R':
                    side = (d + 1) % 4
                    part.append((DX[side], DY[side], d))
                elif ch == 'L':
                    side = (d - 1) % 4
                    part.append((DX[side], DY[side], d))
                elif ch == ')':
                    part.append((0, 0, (d + 1) % 4))
                elif ch == '(':
                    part.append((0, 0, (d - 1) % 4))
        result = compose(result, part)

    return result

answer = parse_program()[0]
print(answer[0], answer[1])
