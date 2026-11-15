def can_win(piles, k):
    for m in set(piles):
        for b in range(1, m // 2 + 1):
            a = m - b
            if a > b and a <= k * b:
                next_piles = list(piles)
                next_piles.remove(m)
                next_piles.append(a)
                next_piles.append(b)

                if not can_win(next_piles, k):
                    return True
    return False

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    piles = list(map(int, input().split()))

    winning_moves = 0

    for m in set(piles):
        for b in range(1, m // 2 + 1):
            a = m - b
            if a > b and a <= k * b:
                next_piles = list(piles)
                next_piles.remove(m)
                next_piles.append(a)
                next_piles.append(b)

                if not can_win(next_piles, k):
                    winning_moves += 1
    if winning_moves > 0:
        print("Win", winning_moves)
    else:
        print("Lose 0")