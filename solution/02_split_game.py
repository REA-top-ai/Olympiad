#A/B
import sys
from functools import lru_cache
sys.setrecursionlimit(10000)
@lru_cache(maxsize = None)
def is_winning(piles, k):
    piles_list = list(piles)
    unique_piles = set(piles_list)
    for m in unique_piles:
        for b in range(1, m):
            a=m-b
            if a > b and a <= k*b:
                new_piles = piles_list.copy()
                new_piles.remove(m)
                new_piles.append(a)
                new_piles.append(b)
                new_piles.sort()
                if not is_winning(tuple(new_piles), k):
                    return True
    return False

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    piles = list(map(int, input().split()))
    piles.sort()
    if not is_winning(tuple(piles), k):
        print("Lose 0")
    else:
        winning_moves = set()
        unique_piles = set(piles)
        for m in unique_piles:
            for b in range(1, m):
                a = m - b
                if a > b and a <= k * b:
                    new_piles = piles.copy()
                    new_piles.remove(m)
                    new_piles.append(a)
                    new_piles.append(b)
                    new_piles.sort()
                    if not is_winning(tuple(new_piles), k):
                        winning_moves.add((m, b))
        print(f"Win {len(winning_moves)}")
