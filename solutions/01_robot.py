s = input().strip()
pos = 0

def add(a, b):
    x1, y1, r1 = a
    x2, y2, r2 = b
    for _ in range(r1):
        x2, y2 = y2, -x2
    return (x1 + x2, y1 + y2, (r1 + r2) % 4)

def repeat(block, count):
    four = (0, 0, 0)
    for _ in range(4):
        four = add(four, block)
    
    res = (four[0] * (count // 4), four[1] * (count // 4), 0)
    
    for _ in range(count % 4):
        res = add(res, block)
    return res

def parse():
    global pos
    res = (0, 0, 0)
    steps = {
        'F': (0, 1, 0), 'B': (0, -1, 0),
        'R': (1, 0, 0), 'L': (-1, 0, 0),
        ')': (0, 0, 1), '(': (0, 0, 3)
    }
    
    while pos < len(s) and s[pos] != ']':
        if s[pos] in steps:
            res = add(res, steps[s[pos]])
            pos += 1
        else:
            num = 0
            while s[pos].isdigit():
                num = num * 10 + int(s[pos])
                pos += 1
            pos += 1
            inner = parse()
            pos += 1
            res = add(res, repeat(inner, num))
    return res

x, y, _ = parse()
print(x, y)
