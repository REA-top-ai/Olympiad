t = int(input())
answers = []
for _ in range(t):
    n, k = map(int, input().split())
    piles = list(map(int, input().split()))
                                                              
    grundy = [0] * (max(piles) + 1)
    for size in range(1, len(grundy)):
        possible = set()
        start = (size + k) // (k + 1)
        for small in range(start, (size - 1) // 2 + 1):
            possible.add(grundy[small] ^ grundy[size - small])
        g = 0
        while g in possible:
            g += 1
        grundy[size] = g
    total = 0
    for size in piles:
        total ^= grundy[size]
    if total == 0:
        answers.append('Lose 0')
    else:
        count = 0
                                                
        for size in set(piles):
            start = (size + k) // (k + 1)
            for small in range(start, (size - 1) // 2 + 1):
                if total ^ grundy[size] ^ grundy[small] ^ grundy[size - small] == 0:
                    count += 1
        answers.append('Win ' + str(count))
print('\n'.join(answers))
