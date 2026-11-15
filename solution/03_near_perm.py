
MOD = 998244353

n, k = map(int, input().split())

if k == 0:
    print(1)

elif k >= n - 1:
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i % MOD
    print(ans)

else:
    size = 1 << (2 * k)

    dp = [0] * size

    dp[(1 << k) - 1] = 1

    for i in range(1, n + 1):
        ndp = [0] * size

        max_d = min(2 * k, n - i + k)

        for mask in range(size):

            if dp[mask] == 0:
                continue

            val = dp[mask]

            if mask & 1:

                for d in range(1, max_d + 1):

                    if (mask & (1 << d)) == 0:

                        new_mask = (mask | (1 << d)) >> 1

                        ndp[new_mask] += val

                        if ndp[new_mask] >= MOD:
                            ndp[new_mask] -= MOD

            else:

                new_mask = mask >> 1

                ndp[new_mask] += val

                if ndp[new_mask] >= MOD:
                    ndp[new_mask] -= MOD

        dp = ndp

    need = (1 << k) - 1

    ans = 0

    for mask in range(size):
        if (mask & need) == need:
            ans += dp[mask]
            ans %= MOD

    print(ans)
