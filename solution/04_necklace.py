# пункт А

from itertools import product

n, k = map(int, input().split())
mod = 1000000007
seen = set()
answer = 0

for colors in product(range(1, k + 1), repeat=n):
    if colors in seen or colors[0] == colors[-1]:
        continue
    valid = True
    for i in range(n - 1):
        if colors[i] == colors[i + 1]:
            valid = False
            break
    if not valid:
        continue
    answer += 1
    flip = colors[::-1]
    for i in range(n):
        seen.add(colors[i:] + colors[:i])
        seen.add(flip[i:] + flip[:i])

print(answer % mod)