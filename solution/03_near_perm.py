n, k = map(int, input().split())
MOD = 998244353

w = 2 * k + 1

trans = []
for mask in range(1 << w):
    result = []
    for j in range(w):
        if mask & (1 << j):
            continue
        new_mask = mask | (1 << j)
        if not (new_mask & 1):
            continue
        result.append(new_mask >> 1)
    trans.append(result)

start = (1 << k) - 1

dp = [0] * (1 << w)
dp[start] = 1

for i in range(n):
    new_dp = [0] * (1 << w)
    for mask in range(1 << w):
        ways = dp[mask]
        if ways == 0:
            continue
        for nm in trans[mask]:
            new_dp[nm] = (new_dp[nm] + ways) % MOD
    dp = new_dp

answer = 0
for mask in range(1 << k):
    answer = (answer + dp[mask]) % MOD

print(answer)
