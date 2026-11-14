from sys import stdin, stdout
from itertools import product

def solve(n, k):
    comb = set()
    for el in product(range(1, k + 1), repeat=n):
        lst = list(el)
        if all(lst[i] not in [lst[i - 1], lst[i + 1]] for i in range(n - 1)):
            variants = []
            for r in (lst, lst[::-1]):
                for s in range(n):
                    variants.append(tuple(r[s:] + r[:s]))
            comb.add(min(variants))

    return len(comb)


def main():
    n, k = map(int, stdin.readline().split())
    stdout.write(f"{solve(n, k)}\n")

if __name__ == "__main__":
    main()