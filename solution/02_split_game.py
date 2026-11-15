import sys


def grundy(maxm, k):
    g = [0] * (maxm + 1)
    for m in range(1, maxm + 1):
        lo = -(-m // (k + 1))
        hi = (m - 1) // 2
        seen = set()
        for b in range(max(lo, 1), hi + 1):
            seen.add(g[b] ^ g[m - b])
        v = 0
        while v in seen:
            v += 1
        g[m] = v
    return g


def main():
    data = sys.stdin.read().split()
    t = int(data[0]); p = 1
    out = []
    for _ in range(t):
        n, k = int(data[p]), int(data[p + 1]); p += 2
        a = list(map(int, data[p:p + n])); p += n
        g = grundy(max(a), min(k, max(a)))
        x = 0
        for v in a:
            x ^= g[v]
        if x == 0:
            out.append("Lose 0")
            continue
        cnt = 0
        for m in set(a):
            need = x ^ g[m]
            lo = -(-m // (k + 1))
            for b in range(max(lo, 1), (m - 1) // 2 + 1):
                if g[b] ^ g[m - b] == need:
                    cnt += 1
        out.append("Win %d" % cnt)
    print("\n".join(out))


main()
