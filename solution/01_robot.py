import sys

def main():
    prog = sys.stdin.readline().strip()
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x = y = 0
    d = 0

    for c in prog:
        if c == 'F':
            k = d
        elif c == 'R':
            k = (d + 1) % 4
        elif c == 'B':
            k = (d + 2) % 4
        elif c == 'L':
            k = (d + 3) % 4
        elif c == ')':
            d = (d + 1) % 4
            continue
        elif c == '(':
            d = (d + 3) % 4
            continue
        else:
            continue
        x += dx[k]
        y += dy[k]
    print(x, y)

main()
