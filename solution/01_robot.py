import sys


def solve():
    s = sys.stdin.readline().strip()

    pos_x = 0
    pos_y = 0
    direction = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def execute(program, idx):
        nonlocal pos_x, pos_y, direction

        while idx < len(program):
            ch = program[idx]

            if ch == 'F':
                pos_x += dx[direction]
                pos_y += dy[direction]
                idx += 1
            elif ch == 'B':
                pos_x -= dx[direction]
                pos_y -= dy[direction]
                idx += 1
            elif ch == 'R':
                right_dir = (direction + 1) % 4
                pos_x += dx[right_dir]
                pos_y += dy[right_dir]
                idx += 1
            elif ch == 'L':
                left_dir = (direction - 1) % 4
                pos_x += dx[left_dir]
                pos_y += dy[left_dir]
                idx += 1
            elif ch == ')':
                direction = (direction + 1) % 4
                idx += 1
            elif ch == '(':
                direction = (direction - 1) % 4
                idx += 1
            elif ch.isdigit():
                num_str = ""
                while idx < len(program) and program[idx].isdigit():
                    num_str += program[idx]
                    idx += 1
                count = int(num_str)

                idx += 1

                start = idx
                balance = 1
                while balance > 0:
                    if program[idx] == '[':
                        balance += 1
                    elif program[idx] == ']':
                        balance -= 1
                    idx += 1

                body = program[start:idx - 1]

                for _ in range(count):
                    execute(body, 0)
            else:
                idx += 1

        return idx

    execute(s, 0)
    print(pos_x, pos_y)


if __name__ == '__main__':
    solve()