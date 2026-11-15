def grundy(max_num, k):
    g = [0] * (max_num + 1)
    for m in range(2, max_num + 1):
        seen = set()
        for b in range((m + k) // (k + 1), (m - 1) // 2 + 1):
            seen.add(g[b] ^ g[m - b])
        mex = 0
        while mex in seen:
            mex += 1
        g[m] = mex
    return g

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    g = grundy(max(numbers), k)
    total = 0
    for m in numbers:
        total ^= g[m]
    count = 0
    for m in set(numbers):
        for b in range((m + k) // (k + 1), (m - 1) // 2 + 1):
            if (total ^ g[m] ^ g[b] ^ g[m - b]) == 0:
                count += 1
    if count > 0:
        print(f"Win {count}")
    else:
        print("Lose 0")