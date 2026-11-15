def split_range(m, k):
    return range((m + k) // (k + 1), (m - 1) // 2 + 1)

def grundy_table(limit, k):
    g = [0] * (limit + 1)
    for m in range(3, limit + 1):
        opts = {g[m - b] ^ g[b] for b in split_range(m, k)}
        mex = 0
        while mex in opts:
            mex += 1
        g[m] = mex
    return g

tests = int(input())
cache = {}
out = []
for i in range(tests):
    n, k = map(int, input().split())
    piles = list(map(int, input().split()))

    if k == 1:
        out.append("Lose 0")
        continue

    k = min(k, 3000)
    limit = max(piles)
    if k not in cache or len(cache[k]) <= limit:
        cache[k] = grundy_table(limit, k)
    g = cache[k]

    total = 0
    for v in piles:
        total ^= g[v]
    if total == 0:
        out.append("Lose 0")
        continue

    cnt = 0
    for m in set(piles):
        need = total ^ g[m]
        cnt += sum(1 for b in split_range(m, k) if g[m - b] ^ g[b] == need)
    out.append(f"Win {cnt}")

print("\n".join(out))
