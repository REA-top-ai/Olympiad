from itertools import product

n, k = map(int, input().split())

found = set()

for coloring in product(range(k), repeat=n):
    ok = True
    for i in range(n):
        if coloring[i] == coloring[(i + 1) % n]:
            ok = False
            break
    if not ok:
        continue

    variants = []
    reversed_coloring = coloring[::-1]
    for i in range(n):
        variants.append(coloring[i:] + coloring[:i])
        variants.append(reversed_coloring[i:] + reversed_coloring[:i])

    found.add(min(variants))

print(len(found) % 1000000007)
