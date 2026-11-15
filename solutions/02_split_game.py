t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    max_pile = max(a)
    grundy = [0] * (max_pile + 1)

    for m in range(1, max_pile + 1):
        low = (m + k) // (k + 1)
        high = (m - 1) // 2
        if low > high:
            continue

        moves = set()
        for b in range(low, high + 1):
            moves.add(grundy[b] ^ grundy[m - b])

        mex = 0
        while mex in moves:
            mex += 1
        grundy[m] = mex

    total = 0
    for x in a:
        total ^= grundy[x]

    if total == 0:
        print("Lose 0")
    else:
        ans = 0
        unique_piles = sorted(set(a))
        for m in unique_piles:
            low = (m + k) // (k + 1)
            high = (m - 1) // 2
            target = total ^ grundy[m]

            ans += sum(1 for b in range(low, high + 1) if (grundy[b] ^ grundy[m - b]) == target)

        print("Win", ans)
