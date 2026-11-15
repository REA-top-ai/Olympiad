MOD = 998244353
n, k = map(int, input().split())

if k >= n - 1:
    ans = 1
    for i in range(2, n + 1):
        ans = ans * i % MOD
    print(ans)
else:
    w = 2 * k + 1
    start = (1 << k) - 1
    ids = {start: 0}
    states = [start]
    trans = []
    p = 0
    while p < len(states):
        mask = states[p]
        lst = []
        for j in range(w):
            if mask >> j & 1:
                continue
            nm = mask | 1 << j
            if not nm & 1:
                continue 
            nm >>= 1
            if nm not in ids:
                ids[nm] = len(states)
                states.append(nm)
            lst.append((j, ids[nm]))
        trans.append(lst)
        p += 1
    m = len(states)
    dp = [0] * m
    dp[0] = 1
    for i in range(1, n + 1):
        lim = n - i + k
        ndp = [0] * m
        for s in range(m):
            c = dp[s]
            if c == 0:
                continue
            for j, t in trans[s]:
                if j <= lim:
                    ndp[t] += c
        dp = [x % MOD for x in ndp]
    print(sum(dp) % MOD)
