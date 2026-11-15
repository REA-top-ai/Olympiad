def solve():
    n, k = map(int, input().split())
    lim = 1 << (2 * k + 1)

    dp = [0] * lim
    dp[0] = 1

    for i in range(1, n + 1):
        ndp = [0] * lim
        for m in range(lim):
            if dp[m]:
                if not (i > k + 1 and not (m & 1)):
                    sm = m >> 1
                    for v in range(max(1, i - k), min(n, i + k) + 1):
                        idx = v - (i - k)
                        if not (sm & (1 << idx)):
                            nm = sm | (1 << idx)
                            ndp[nm] = (ndp[nm] + dp[m]) % 998244353
        dp = ndp

    print(sum(dp) % 998244353)


if __name__ == "__main__":
    solve()
