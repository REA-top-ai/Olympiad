import sys

MOD = 998244353


def main():
    n, k = map(int, sys.stdin.read().split())
    if k >= n - 1:
        f = 1
        for i in range(2, n + 1):
            f = f * i % MOD
        print(f)
        return


    w = 2 * k
    states = [m for m in range(1 << w) if bin(m).count('1') == k]
    idx = {m: j for j, m in enumerate(states)}
    trans = []
    for m in states:
        nxt = []
        for j in range(w + 1):
            if not (m >> j) & 1:
                nm = m | (1 << j)
                if nm & 1:
                    nxt.append(idx[nm >> 1])
        trans.append(nxt)
    s0 = idx[(1 << k) - 1]
    dp = [0] * len(states)
    dp[s0] = 1
    S = len(states)
    for _ in range(n):
        nd = [0] * S
        for s in range(S):
            v = dp[s]
            if v:
                for t in trans[s]:
                    nd[t] += v
        dp = [v % MOD for v in nd]
    print(dp[s0])


main()
