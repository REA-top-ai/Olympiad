MOD = 998244353


def solve(n, k):
    if k >= n - 1:
        answer = 1
        for i in range(2, n + 1):
            answer = answer * i % MOD
        return answer
    if n <= 10:
        dp = [0] * (1 << n)
        bits = [0] * (1 << n)
        for mask in range(1, 1 << n):
            bits[mask] = bits[mask >> 1] + (mask & 1)
        dp[0] = 1
        for mask in range(1 << n):
            i = bits[mask]
            for j in range(max(0, i - k), min(n, i + k + 1)):
                if not mask & (1 << j):
                    nxt = mask | (1 << j)
                    dp[nxt] = (dp[nxt] + dp[mask]) % MOD
        return dp[-1]
    if k == 0:
        return 1
    width = 2 * k
    bits = [0] * (1 << width)
    for mask in range(1, 1 << width):
        bits[mask] = bits[mask >> 1] + (mask & 1)
    masks = [m for m in range(1 << width) if bits[m] == k]
    index = {m: i for i, m in enumerate(masks)}
    transitions = []
    for mask in masks:
        targets = []
        for j in range(width + 1):
            bit = 1 << j
            if mask & bit:
                continue
            filled = mask | bit
            if filled & 1:
                targets.append(index[filled >> 1])
        transitions.append(targets)
    start = index[(1 << k) - 1]
    dp = [0] * len(masks)
    dp[start] = 1
    for _ in range(n):
        nxt = [0] * len(masks)
        for i, targets in enumerate(transitions):
            value = dp[i]
            for j in targets:
                nxt[j] += value
        dp = [value % MOD for value in nxt]
    return dp[start]


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(solve(n, k))
