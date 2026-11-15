n, k = map(int, input().split())
mod = 998244353

free = tuple(range(1, min(n, k + 1) + 1))
dp = {free: 1}

for i in range(1, n + 1):
    next_dp = {}
    last_chance = i - k
    new_number = i + k + 1

    for free, count in dp.items():
        for j, number in enumerate(free):
            if last_chance in free and number != last_chance:
                continue

            rest = free[:j] + free[j + 1:]
            if new_number <= n:
                rest = rest + (new_number,)

            saved = next_dp.get(rest, 0)
            next_dp[rest] = (saved + count) % mod

    dp = next_dp

print(dp.get((), 0))