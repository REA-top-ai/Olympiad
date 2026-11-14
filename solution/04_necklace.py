from itertools import product

n, k = map(int, input().split())
necklaces = set()

for colours in product(range(k), repeat=n):
    right = True

    for i in range(n):
        if colours[i] == colours[(i+1) % n]:
            right = False
            break
    if not right:
        continue

    reversed_colours = colours[::-1]
    variants = []

    for i in range(n):
        variants.append(colours[i:] + colours[:i])
        variants.append(reversed_colours[i:] + reversed_colours[:i])

    necklaces.add(min(variants))

print(len(necklaces) % 1000000007)
