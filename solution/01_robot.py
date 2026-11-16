def solve():
    program = input().strip()
    x = 0
    y = 0
    direction = 0

    # функция для выполнения одной команды движения
    def get_move(command, direction):
        if command == 'F':  # вперёд
            if direction == 0:  # север
                return 0, 1
            elif direction == 1:  # восток
                return 1, 0
            elif direction == 2:  # юг
                return 0, -1
            else:  # запад
                return -1, 0
        elif command == 'B':  # назад
            if direction == 0:  # север
                return 0, -1
            elif direction == 1:  # восток
                return -1, 0
            elif direction == 2:  # юг
                return 0, 1
            else:  # запад
                return 1, 0
        elif command == 'R':  # вправо 
            right_dir = (direction + 1) % 4
            if right_dir == 0:  # север
                return 0, 1
            elif right_dir == 1:  # восток
                return 1, 0
            elif right_dir == 2:  # юг
                return 0, -1
            else:  # запад
                return -1, 0
        elif command == 'L':  # влево
            left_dir = (direction + 3) % 4
            if left_dir == 0:  # север
                return 0, 1
            elif left_dir == 1:  # восток
                return 1, 0
            elif left_dir == 2:  # юг
                return 0, -1
            else:  # запад
                return -1, 0
        return 0, 0

    # функция для поворота вектора по часовой стрелке
    def rotate_vector(dx, dy, direction):
        for i in range(direction):
            temp = dx
            dx = dy
            dy = -temp
        return dx, dy

    # функция для обработки блока программы
    def process_block(start_pos):
        pos = start_pos
        block_x = 0
        block_y = 0
        block_dir = 0 

        while pos < len(program):
            char = program[pos]

            if char == ']':
                break
            elif char == 'F' or char == 'B' or char == 'R' or char == 'L':
                dx, dy = get_move(char, block_dir)
                block_x += dx
                block_y += dy
                pos += 1
            elif char == ')':
                # поворот по часовой стрелке
                block_dir = (block_dir + 1) % 4
                pos += 1
            elif char == '(':
                # поворот против часовой стрелки
                block_dir = (block_dir + 3) % 4
                pos += 1
            elif char.isdigit():
                num_str = ""
                while pos < len(program) and program[pos].isdigit():
                    num_str += program[pos]
                    pos += 1
                n = int(num_str)

                if pos < len(program) and program[pos] == '[':
                    pos += 1

                pos, body_x, body_y, body_dir = process_block(pos)

                four_x = 0
                four_y = 0
                four_dir = 0

                for repeat in range(4):
                    dx, dy = rotate_vector(body_x, body_y, four_dir)
                    four_x += dx
                    four_y += dy
                    four_dir = (four_dir + body_dir) % 4

                full_cycles = n // 4
                remainder = n % 4
                block_x += full_cycles * four_x
                block_y += full_cycles * four_y

                for repeat in range(remainder):
                    dx, dy = rotate_vector(body_x, body_y, block_dir)
                    block_x += dx
                    block_y += dy
                    block_dir = (block_dir + body_dir) % 4

                if pos < len(program) and program[pos] == ']':
                    pos += 1
            else:
                pos += 1

        return pos, block_x, block_y, block_dir

    _, total_x, total_y, _ = process_block(0)
    print(total_x, total_y)
solve()
