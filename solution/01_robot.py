class Robot:
    def __init__(self, program):
        self.program = program
        self.pos = 0

    def rotate(self, x, y, direction):
        for _ in range(direction):
            x, y = y, -x
        return x, y

    def read(self):
        x = y = direction = 0
        moves = {"F": (0, 1), "B": (0, -1), "R": (1, 0), "L": (-1, 0)}
        while self.pos < len(self.program):
            symbol = self.program[self.pos]
            self.pos += 1
            if symbol == "]":
                break
            if symbol == ")":
                direction = (direction + 1) % 4
            elif symbol == "(":
                direction = (direction - 1) % 4
            elif symbol in moves:
                dx, dy = moves[symbol]
                dx, dy = self.rotate(dx, dy, direction)
                x += dx
                y += dy
            else:
                count = int(symbol)
                while "0" <= self.program[self.pos] <= "9":
                    count = count * 10 + int(self.program[self.pos])
                    self.pos += 1
                self.pos += 1
                dx, dy, turn = self.read()
                if turn == 0:
                    dx, dy = self.rotate(dx, dy, direction)
                    x += dx * count
                    y += dy * count
                else:
                    for _ in range(count % 4):
                        a, b = self.rotate(dx, dy, direction)
                        x += a
                        y += b
                        direction = (direction + turn) % 4
        return x, y, direction


if __name__ == "__main__":
    robot = Robot(input())
    x, y, _ = robot.read()
    print(x, y)
