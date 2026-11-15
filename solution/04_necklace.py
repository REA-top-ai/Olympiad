n, k = map(int, input().split())
seen = set()

def build(c):
    if len(c) == n:
        if c[0] != c[-1]:
            forms = []
            for s in range(n):
                r = c[s:] + c[:s]
                forms += [r, r[::-1]]
            seen.add(tuple(min(forms)))
        return
    for x in range(k):
        if not c or x != c[-1]:
            build(c + [x])
build([])
print(len(seen) % 1000000007)
