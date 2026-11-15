
from itertools import product

MOD = 1000000007

n, k = map(int, input().split())

if k < 2:
    print(0)
else:
    unique_necklaces = set()
    for coloring in product(range(k), repeat=n):
        valid = True
        for i in range(n):
            if coloring[i] == coloring[(i + 1) % n]:
                valid = False
                break

        if not valid:
            continue


        variants = []
        for shift in range(n):
            rotated = coloring[shift:] + coloring[:shift]
            variants.append(rotated)


        reversed_coloring = coloring[::-1]
        for shift in range(n):
            rotated = (reversed_coloring[shift:]+ reversed_coloring[:shift])
            variants.append(rotated)

        canonical = min(variants)
        unique_necklaces.add(canonical)

    print(len(unique_necklaces) % MOD)
