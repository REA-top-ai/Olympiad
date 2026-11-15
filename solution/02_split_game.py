# пункт А

from functools import lru_cache

def count_winning_moves(piles, k):
    max_size = max(piles)
    splits = [[] for i in range(max_size + 1)]
    for size in range(1, max_size + 1):
        for b in range(1, (size - 1) // 2 + 1):
            a = size - b
            if a > k * b:
                continue
            new_piles = []
            if splits[a]:
                new_piles.append(a)
            if splits[b]:
                new_piles.append(b)
            splits[size].append(tuple(new_piles))

    def next_positions(position):
        positions = []
        previous_size = 0
        for i, size in enumerate(position):
            if size == previous_size:
                continue
            previous_size = size
            remaining = position[:i] + position[i + 1:]
            for parts in splits[size]:
                new_position = tuple(sorted(remaining + parts))
                positions.append(new_position)
        return positions

    @lru_cache(None)
    def can_win(position):
        for new_position in next_positions(position):
            if not can_win(new_position):
                return True
        return False

    position = tuple(sorted(size for size in piles if splits[size]))
    count = 0
    for new_position in next_positions(position):
        if not can_win(new_position):
            count += 1
    return count


t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    piles = list(map(int, input().split()))
    count = count_winning_moves(piles, k)
    if count > 0:
        print('Win', count)
    else:
        print('Lose 0')

