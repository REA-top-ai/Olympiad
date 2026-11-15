MOD = 998244353
n, k = map(int, input().split())

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i % MOD
    return result

if k >= n - 1:
    print(factorial(n) % MOD)
else:
    w = 2 * k + 1
    size = 1 << w
    full = size - 1

    start = 0
    for j in range(w):
        x = -k + j
        if x < 0 or x >= n:
            start |= 1 << j

    dp = [0] * size
    dp[start] = 1

    for i in range(n):
        ndp = [0] * size

        for mask in range(size):
            if dp[mask] == 0:
                continue

            for j in range(w):
                x = i - k + j

                if x < 0 or x >= n:
                    continue

                bit = 1 << j

                if mask & bit:
                    continue

                new_mask = mask | bit

                if (new_mask & 1) == 0:
                    continue

                right_used = 1 if i + k + 1 >= n else 0
                next_mask = (new_mask >> 1) | (right_used << (w - 1))
                ndp[next_mask] = (ndp[next_mask] + dp[mask]) % MOD

        dp = ndp

    print(dp[full])