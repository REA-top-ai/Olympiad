def solve(piles, k):
    if k == 1:
        return "Lose 0"
    limit = max(piles)
    grundy = [0] * (limit + 1)
    for m in range(3, limit + 1):
        first = (m + k) // (k + 1)
        last = (m - 1) // 2
        values = set()
        for b in range(first, last + 1):
            values.add(grundy[b] ^ grundy[m - b])
        value = 0
        while value in values:
            value += 1
        grundy[m] = value
    total = 0
    for m in piles:
        total ^= grundy[m]
    if total == 0:
        return "Lose 0"
    answer = 0
    for m in set(piles):
        target = total ^ grundy[m]
        for b in range((m + k) // (k + 1), (m - 1) // 2 + 1):
            if grundy[b] ^ grundy[m - b] == target:
                answer += 1
    return f"Win {answer}"


def main():
    answers = []
    for _ in range(int(input())):
        n, k = map(int, input().split())
        piles = list(map(int, input().split()))
        answers.append(solve(piles, k))
    print("\n".join(answers))


if __name__ == "__main__":
    main()

# мне для этой задачи пришлось читать про теорию игр и чсило Гранди. не круто (ಥ_ಥ)