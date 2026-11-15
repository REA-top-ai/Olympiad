class State:
    def __init__(self, x=0, y=0, dir=0):
        self.x = x
        self.y = y
        self.dir = dir % 4

    def set_dir(self, d) -> State:

        match d % 4:
            case 1:
                self.x, self.y = self.y, -self.x
            case 2:
                self.x, self.y = -self.x, -self.y
            case 3:
                self.x, self.y = -self.y, self.x
        return self

    def __add__(self, other: State) -> State:
        next: State = State(other.x, other.y).set_dir(self.dir)

        new_x = self.x + next.x
        new_y = self.y + next.y
        new_dir = (self.dir + other.dir) % 4

        return State(new_x, new_y, new_dir)

    def __mul__(self, n) -> State:
        d = self.dir
        if d == 0:
            return State(self.x * n, self.y * n, 0)

        until_repeated = n % 2 if d == 2 else n % 4

        res = State()

        for i in range(0, until_repeated):
            res = res + self

        return res


def parse(expr: str, pos=0):
    res = State()
    out = False

    while pos < len(expr):
        ch = expr[pos]
        if ch == "F":
            res += State(0, 1)
            pos += 1
        elif ch == "B":
            res += State(0, -1)
            pos += 1
        elif ch == "R":
            res += State(1, 0)
            pos += 1
        elif ch == "L":
            res += State(-1, 0)
            pos += 1

        elif ch == ")":
            res += State(0, 0, 1)
            pos += 1
        elif ch == "(":
            res += State(0, 0, 3)
            pos += 1

        elif ch == "]":
            pos += 1
            return res, pos

        elif ch.isdigit():
            n = ""
            while ch.isdigit():
                n += ch
                pos += 1
                ch = expr[pos]

            pos += 1
            parsed, pos = parse(expr, pos)
            res += parsed * int(n)

    return res, pos


expr = input()
res, pos = parse(expr)
print(res.x, res.y)
