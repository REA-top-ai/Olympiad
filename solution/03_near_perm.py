from sys import stdin, stdout
from itertools import permutations

def solve(n, k):
    cnt = 0

    for perm in permutations(range(1, n + 1)):
        if all(abs(perm[i] - (i + 1)) <= k for i in range(n)):
            cnt += 1

    return cnt % 998244353


def main():
    n, k = map(int, stdin.readline().split())
    stdout.write(str(solve(n, k)) + '\n')

if __name__ == "__main__":
    main()