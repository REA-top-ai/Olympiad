def rot(dx, dy, d):
    for k in range(d % 4):
        dx, dy = dy, -dx
    return dx, dy

def go(prog, i):
    x = y = d = 0
    N = 0
    while i < len(prog) and prog[i] != ']':
        c = prog[i]
        if c in moves:
            dx, dy = rot(*moves[c], d)
            x += dx
            y += dy
        elif c == ')':
            d = (d + 1) % 4
        elif c == '(':
            d = (d - 1) % 4
        elif c.isdigit():
            N = N * 10 + int(c)
        elif c == '[':
            bx, by, t, i = go(prog, i + 1)
            for j in range(min(N, 4)):
                cnt = N // 4 + (1 if j < N % 4 else 0)
                rx, ry = rot(bx, by, d + j * t)
                x += cnt * rx
                y += cnt * ry
            d = (d + N * t) % 4
            N = 0
        i += 1
    return x, y, d, i

moves = {'F': (0, 1), 'B': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
prog = input().strip()
print(prog)
x, y, d, i = go(prog, 0)
print(x, y)
