n, k = map(int, input().split())
mod = 998244353
if k >= n - 1:
    answer = 1
    for i in range(2, n + 1):
        answer = answer * i % mod
    print(answer)
elif k > 2:
    used = [False] * (n + 1)

    def count(row):
        if row > n:
            return 1
        result = 0
        for value in range(max(1, row - k), min(n, row + k) + 1):
            if not used[value]:
                used[value] = True
                result += count(row + 1)
                used[value] = False
        return result % mod

    print(count(1))
else:
    width = 2 * k + 1
    full = (1 << width) - 1
                                                                     
    initial = (1 << k) - 1
    dp = {initial: 1}
    for row in range(1, n + 1):
        next_dp = {}
        outside = (1 << (width - 1)) if row + k + 1 > n else 0
        for mask, ways in dp.items():
            free = full ^ mask
            while free:
                bit = free & -free
                free -= bit
                used = mask | bit
                if used & 1:
                    new_mask = (used >> 1) | outside
                    next_dp[new_mask] = (next_dp.get(new_mask, 0) + ways) % mod
        dp = next_dp
    print(dp.get(full, 0))
