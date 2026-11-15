import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    heaps = list(map(int, input().split()))
    limit = max(heaps)

    grundy = [0] * (limit + 1)

    for m in range(1, limit + 1):
        used = set()
        left = (m + k) // (k + 1)
        for b in range(max(1, left), (m - 1) // 2 + 1):
            a = m - b
            if a <= k * b:
                used.add(grundy[a] ^ grundy[b])

        g = 0
        while g in used:
            g += 1
        grundy[m] = g

    total = 0
    for x in heaps:
        total ^= grundy[x]

    if total == 0:
        print('Lose 0')
        continue

    winning = 0
    for m in set(heaps):
        for b in range(max(1, (m + k) // (k + 1)), (m - 1) // 2 + 1):
            a = m - b
            if a <= k * b:
                new_xor = total ^ grundy[m] ^ grundy[a] ^ grundy[b]
                if new_xor == 0:
                    winning += 1

    print('Win', winning)
