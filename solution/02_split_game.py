t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    mx = max(a)
    g = [0] * (mx + 1)
    used = [0] * (mx + 2)
    cur = 0

    for m in range(1, mx + 1):
        l = (m + k) // (k + 1)
        r = (m - 1) // 2
        if l > r:
            continue

        cur += 1
        for b in range(l, r + 1):
            v = g[b] ^ g[m - b]
            if v <= mx:
                used[v] = cur

        mex = 0
        while used[mex] == cur:
            mex += 1
        g[m] = mex

    x_sum = 0
    for val in a:
        x_sum ^= g[val]

    if x_sum == 0:
        print("Lose 0")
        continue

    ans = 0
    for m in set(a):
        l = (m + k) // (k + 1)
        r = (m - 1) // 2
        need = x_sum ^ g[m]

        for b in range(l, r + 1):
            if (g[b] ^ g[m - b]) == need:
                ans += 1

    print(f"Win {ans}")




