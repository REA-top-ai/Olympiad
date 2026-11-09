from sys import stdin, stdout

NESW = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dictionary = {'F': 0, 'R': 1, 'B': 2, 'L': 3}


def turn(dx, dy, times):
    for _ in range(times % 4):
        dx, dy = dy, -dx
    return dx, dy

def programm(data, x, y, d):
    i = 0
    count = ''
    while i < len(data):
        if data[i].isdigit():
            count = count + data[i]
            i += 1

        elif data[i] == '[':
            n, count = int(count), ''
            cnt, i, alg = 1, i + 1, ''
            while cnt != 0:
                if data[i] == '[': cnt += 1
                elif data[i] == ']': cnt -= 1
                alg += data[i]
                i += 1
            alg = alg[:-1]

            bx, by, br = programm(alg, 0, 0, 0)

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

        elif data[i] in dictionary:
            dx, dy = NESW[(d + dictionary[data[i]]) % 4]
            x += dx
            y += dy
            i += 1

        elif data[i] == ')':
            d = (d + 1) % 4
            i += 1

        elif data[i] == '(':
            d = (d - 1) % 4
            i += 1

    return x, y, d

def main():
    data = stdin.readline().strip()
    x, y, d = programm(data, 0, 0, 0)
    stdout.write(f"{x} {y}\n")

if __name__ == "__main__":
    main()
