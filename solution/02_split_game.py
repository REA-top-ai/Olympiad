def rules_checker(n, k):
    moves = []

    for x in range(1, n):
        y = n - x
        a = max(x, y)
        b = min(x, y)

        if a <= b or a > k*b:
            continue

        if (a, b) not in moves:
            moves.append((a, b))

    return moves


def check(ai, k, checked_combinations):
    ai = tuple(sorted(ai))

    if ai in checked_combinations:
        return checked_combinations[ai]

    sizes_checked = []

    for i in range(len(ai)):
        n = ai[i]

        if n in sizes_checked:
            continue

        sizes_checked.append(n)

        for a, b in rules_checker(n, k):
            new_ai = list(ai)
            new_ai.pop(i)
            new_ai.append(a)
            new_ai.append(b)

            if check(new_ai, k, checked_combinations) == False:
                checked_combinations[ai] = True
                return True

    checked_combinations[ai] = False
    return False


t = int(input())

for test in range(t):
    count, k = map(int, input().split())
    ai = list(map(int, input().split()))

    checked_combinations = {}
    checked = []
    counter = 0

    for i in range(len(ai)):
        n = ai[i]

        if n in checked:
            continue

        checked.append(n)

        for a, b in rules_checker(n, k):
            new_ai = ai.copy()
            new_ai.pop(i)
            new_ai.append(a)
            new_ai.append(b)

            if check(new_ai, k, checked_combinations) == False:
                counter += 1

    if counter > 0:
        print("Win", counter)
    else:
        print("Lose 0")