def get_new_piles(piles: list, k: int) -> list:
    result = []
    for m in set(piles):  # берем уникальные значения тк одинаковые кучки неразличимы
        # b строго меньше a
        for b in range(1, (m - 1) // 2 + 1):
            a = m - b
            # проверка условия с k
            if a <= k * b:
                new_piles = list(piles)
                # удаляем старую кучку и добавляем 2 новые на которые разделили исходную
                new_piles.remove(m)
                new_piles.append(a)
                new_piles.append(b)
                result.append(new_piles)
    return result


def can_win(piles: list, k: int, memo: dict) -> bool:
    # убираем кучки 1 и 2 (они не влияют на игру) и сортируем для словаря
    state = tuple(sorted(x for x in piles if x > 2))
    if state in memo:
        return memo[state]

    for new in get_new_piles(list(state), k):
        if not can_win(new, k, memo):
            memo[state] = True
            return True

    memo[state] = False
    return False


if __name__ == "__main__":
    # ввод
    t = int(input())  # количество тестов

    results = []
    for _ in range(t):
        n, k = list(map(int, input().split()))   # количество куч и коэфицент для условия
        piles = list(map(int, input().split()))  # кучи

        if k == 1:
            print('Lose 0')
            break

        memo = dict()

        win_moves = 0
        for new in get_new_piles(piles, k):
            if not can_win(new, k, memo):
                win_moves += 1
        results.append(win_moves)

    # вывод
    for _ in results:
        if _ > 0:
            print(f"Win {_}")
        else:
            print("Lose 0")
