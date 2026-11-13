#A/B
def expand(st):
    stack = []
    current = ""
    i=0
    n=0
    while i<len(st):
        symb = st[i]

        if symb.isdigit():
            num_str = ""
            while i < len(st) and st[i].isdigit():
                num_str+=st[i]
                i+=1
            n = int(num_str)
        elif symb == '[':
            stack.append((current, n))
            current = ""
            i+=1
        elif symb == ']':
            prev, n = stack.pop()
            current = prev + n * current
            i += 1
        else:
            current += symb
            i += 1
    return current

x, y = 0, 0
fx, fy = 0, 1
st = input()
expanded = expand(st)
for symb in expanded:
    if symb == 'F':
        x+=fx
        y+=fy
    elif symb== 'B':
        x-=fx
        y-=fy
    elif symb == 'R':
        x+=fy
        y-=fx
    elif symb == 'L':
        x-=fy
        y+=fx
    elif symb == ')':
        fx, fy = fy, -fx
    elif symb == '(':
        fx, fy = -fy, fx

print(x,y)