import sys


def rot(v, r):
    x, y = v
    for _ in range(r % 4):
        x, y = y, -x
    return x, y


def compose(a, b):
    (ax, ay, ar), (bx, by, br) = a, b
    rx, ry = rot((bx, by), ar)
    return ax + rx, ay + ry, (ar + br) % 4


def power(t, n):
    res = (0, 0, 0)
    while n:
        if n & 1:
            res = compose(res, t)
        t = compose(t, t)
        n >>= 1
    return res


MOVES = {'F': (0, 1, 0), 'B': (0, -1, 0), 'R': (1, 0, 0), 'L': (-1, 0, 0),
         ')': (0, 0, 1), '(': (0, 0, 3)}


def main():
    s = sys.stdin.read().strip()
    stack = [[(0, 0, 0), 0]]
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        if c.isdigit():
            j = i
            while s[j].isdigit():
                j += 1
            stack.append([(0, 0, 0), int(s[i:j])])
            i = j + 1
            continue
        if c == ']':
            t, cnt = stack.pop()
            stack[-1][0] = compose(stack[-1][0], power(t, cnt))
        elif c in MOVES:
            stack[-1][0] = compose(stack[-1][0], MOVES[c])
        i += 1
    x, y, _ = stack[0][0]
    print(x, y)


main()
