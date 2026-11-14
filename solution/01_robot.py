program = input().strip()

while ']' in program:
    right = program.find(']')
    left = program.rfind('[', 0, right)

    start_num = left - 1
    while start_num > 0 and program[start_num - 1].isdigit():
        start_num -= 1

    k = int(program[start_num:left])
    body = program[left + 1: right]

    program = program[:start_num] + (body * k) + program[right + 1:]

x, y = 0, 0
dir_x, dir_y = 0, 1

for step in program:
    if step == ')':
        dir_x, dir_y = dir_y, -dir_x
    elif step == '(':
        dir_x, dir_y = -dir_y, dir_x
    elif step == 'F':
        x += dir_x
        y += dir_y
    elif step == 'B':
        x -= dir_x
        y -= dir_y
    elif step == 'R':
        x += dir_y
        y -= dir_x
    elif step == 'L':
        x -= dir_y
        y += dir_x

print(x, y)
