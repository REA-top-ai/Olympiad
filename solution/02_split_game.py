from functools import lru_cache


def get_moves(state, k):
    moves = []
    for m in set(state):
        for b in range(1, m):
            a = m-b
            if a > b and a <= k * b:
                new_state = list(state)
                new_state.remove(m)
                new_state.append(a)
                new_state.append(b)
                new_state.sort()
                moves.append(tuple(new_state))
    return moves


@lru_cache(None)

def winning(state, k):
    moves = get_moves(state, k)

    for new_state in moves:
        if not winning(new_state, k):
            return True

    return False


t = int(input())

for x in range(t):
    n, k = map(int, input().split())
    heaps = tuple(sorted(map(int, input().split())))

    winning_moves = 0

    for new_state in get_moves(heaps, k):
        if not winning(new_state, k):
            winning_moves += 1

    if winning_moves == 0:
        print("Lose 0")
    else:
        print("Win", winning_moves)