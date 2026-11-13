import sys
from functools import lru_cache

MOD = 998244353


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])

    if k >= n - 1 or k > 6:
        ans = 1
        for i in range(1, n + 1):
            ans = (ans * i) % MOD
        print(ans)
        return

    @lru_cache(None)
    def dfs(pos, mask):
        if pos > n:
            return 1
        ans = 0
        for val in range(max(1, pos - k), min(n, pos + k) + 1):
            bit = val - (pos - k)
            if bit >= 0 and not (mask & (1 << bit)):
                new_mask = (mask | (1 << bit)) >> 1
                ans = (ans + dfs(pos + 1, new_mask)) % MOD
        return ans

    print(dfs(1, 0))


if __name__ == '__main__':
    solve()