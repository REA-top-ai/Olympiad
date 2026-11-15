from sys import stdin, stdout

NESW = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dictionary = {'F': 0, 'R': 1, 'B': 2, 'L': 3}

def turn(dx, dy, times):
    for _ in range(times % 4):
        dx, dy = dy, -dx
    return dx, dy

def programm(data):
    x, y, d = 0, 0, 0
    stack, count = [], ''
    for c in data:
        if c.isdigit():
            count = count + c

        elif c == '[':
            stack.append((x, y, d, int(count)))
            x, y, d, count = 0, 0, 0, ''

        elif c == ']':
            bx, by, br = x, y, d
            x, y, d, n = stack.pop()

            if br == 0:
                lx, ly = n * bx, n * by
            else:
                lx, ly = 0, 0
                for j in range(n % 4):
                    dx, dy = turn(bx, by, j * br % 4)
                    lx += dx
                    ly += dy

            dx, dy = turn(lx, ly, d)
            x += dx
            y += dy
            d = (d + n * br) % 4

        elif c in dictionary:
            dx, dy = NESW[(d + dictionary[c]) % 4]
            x += dx
            y += dy

        elif c == ')':
            d = (d + 1) % 4

        elif c == '(':
            d = (d - 1) % 4

    return x, y

def main():
    data = stdin.readline().strip()
    x, y = programm(data)
    stdout.write(f"{x} {y}\n")

if __name__ == "__main__":
    main()
