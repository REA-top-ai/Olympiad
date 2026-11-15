s = input().strip()


def merge(a, b):
    x1, y1, d1 = a
    x2, y2, d2 = b
    if d1 == 1:
        x2, y2 = y2, -x2
    elif d1 == 2:
        x2, y2 = -x2, -y2
    elif d1 == 3:
        x2, y2 = -y2, x2
    return (x1 + x2, y1 + y2, (d1 + d2) & 3)


def power(st, k):
    res = (0, 0, 0)
    while k:
        if k & 1:
            res = merge(res, st)
        st = merge(st, st)
        k >>= 1
    return res


cmds = {
    'F': (0, 1, 0),
    'B': (0, -1, 0),
    'R': (1, 0, 0),
    'L': (-1, 0, 0),
    ')': (0, 0, 1),
    '(': (0, 0, 3),
}

stack = [(1, (0, 0, 0))]
i = 0
n = len(s)

while i < n:
    if s[i] in cmds:
        cnt, cur = stack[-1]
        stack[-1] = (cnt, merge(cur, cmds[s[i]]))
        i += 1
    elif s[i].isdigit():
        j = i
        while j < n and s[j].isdigit():
            j += 1
        k = int(s[i:j])
        stack.append((k, (0, 0, 0)))
        i = j + 1
    elif s[i] == ']':
        k, body = stack.pop()
        cnt, prev = stack[-1]
        stack[-1] = (cnt, merge(prev, power(body, k)))
        i += 1

ans_x, ans_y, _ = stack[0][1]
print(ans_x, ans_y)

