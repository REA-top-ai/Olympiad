t = int(input())

for test in range(t):
    n, k = map(int, input().split())
    piles = list(map(int, input().split()))

    memo = {}

    def win(state):
        if state in memo:
            return memo[state]

        result = False
        for i in range(len(state)):
            m = state[i]
            for b in range(1, m):
                a = m - b
                if a > b and a <= k * b:
                    new_state = list(state)
                    new_state.pop(i)
                    new_state.append(a)
                    new_state.append(b)
                    new_state.sort()
                    if not win(tuple(new_state)):
                        result = True

        memo[state] = result
        return result

    seen = []
    count = 0
    for i in range(len(piles)):
        m = piles[i]
        for b in range(1, m):
            a = m - b
            if a > b and a <= k * b:
                if (m, b) in seen:
                    continue
                seen.append((m, b))

                new_state = list(piles)
                new_state.pop(i)
                new_state.append(a)
                new_state.append(b)
                new_state.sort()
                if not win(tuple(new_state)):
                    count += 1

    if count > 0:
        print("Win", count)
    else:
        print("Lose 0")
