def robot(program_str):
    while '[' in program_str and ']' in program_str:
        right_skob = program_str.find(']')
        left_skob = program_str.rfind('[', 0, right_skob)
        body = program_str[left_skob + 1: right_skob]

        i = left_skob - 1
        while i >= 0 and program_str[i].isdigit():
            i -= 1

        count = int(program_str[i + 1: left_skob])

        old_part = program_str[i + 1: right_skob + 1]
        new_part = body * count

        program_str = program_str.replace(old_part, new_part, 1)

    return program_str


def solve(program_str):
    full_command = robot(program_str)

    x, y = 0, 0
    view = 0  # север восток юг запад = 0 1 2 3

    for char in full_command:
        if char == 'F':
            if view == 0:
                y += 1
            elif view == 1:
                x += 1
            elif view == 2:
                y -= 1
            elif view == 3:
                x -= 1
        elif char == 'B':
            if view == 0:
                y -= 1
            elif view == 1:
                x -= 1
            elif view == 2:
                y += 1
            elif view == 3:
                x += 1
        elif char == 'R':
            if view == 0:
                x += 1
            elif view == 1:
                y -= 1
            elif view == 2:
                x -= 1
            elif view == 3:
                y += 1
        elif char == 'L':
            if view == 0:
                x -= 1
            elif view == 1:
                y += 1
            elif view == 2:
                x += 1
            elif view == 3:
                y -= 1
        elif char == ')':
            view = (view + 1) % 4
        elif char == '(':
            view = (view - 1) % 4

    return x, y, view


if __name__ == "__main__":
    program_str = input().strip()
    x, y, view = solve(program_str)
    print(x, y)
