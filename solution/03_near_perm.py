from itertools import permutations

n, k = map(int, input().split())
cnt = 0

for p in permutations(range(1, n+1)):
    right = True
    for i in range(n):
        if abs(p[i] - (i + 1)) > k:
            right = False
            break
    if right:
        cnt += 1

print(cnt % 998244353)
