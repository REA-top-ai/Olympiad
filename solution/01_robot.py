program = input().strip()

stack = []
text = ""
number = ""

for c in program:
    if c.isdigit():
        number = number + c
    elif c == "[":
        stack.append((int(number), text))
        number = ""
        text = ""
    elif c == "]":
        times, before = stack.pop()
        text = before + text * times
    else:
        text = text + c

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x = 0
y = 0
d = 0

for c in text:
    if c == "F":
        x += dx[d]
        y += dy[d]
    elif c == "B":
        x += dx[(d + 2) % 4]
        y += dy[(d + 2) % 4]
    elif c == "R":
        x += dx[(d + 1) % 4]
        y += dy[(d + 1) % 4]
    elif c == "L":
        x += dx[(d + 3) % 4]
        y += dy[(d + 3) % 4]
    elif c == ")":
        d = (d + 1) % 4
    elif c == "(":
        d = (d + 3) % 4

print(x, y)
