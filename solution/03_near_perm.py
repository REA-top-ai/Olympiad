from itertools import permutations

n, k = map(int, input().split())

count = 0
for p in permutations(range(1, n + 1)):
    ok = True
    for i in range(n):
        if abs(p[i] - (i + 1)) > k:
            ok = False
            break
    if ok:
        count += 1

print(count % 998244353)
