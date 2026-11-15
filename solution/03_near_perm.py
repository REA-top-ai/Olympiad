from itertools import permutations
from math import factorial

# |π(i) − i| ≤ k    для всех i = 1 … n


def is_valid(p: tuple) -> bool:
    for i in range(len(p)):
        if abs(p[i] - (i + 1)) > k:
            return False
    return True


def solve(n, k):
    if k == 0:
        return 1
    elif k >= (n - 1):
        return factorial(n)
    else:
        numbers = [num for num in range(1, n + 1)]
        all_perm = permutations(numbers)  # все перестановки

        count = 0
        for p in all_perm:
            if is_valid(p):
                count += 1
        return count


if __name__ == "__main__":

    n, k = list(map(int, input().split()))

    right_count = solve(n, k)
    print(right_count % 998244353)
