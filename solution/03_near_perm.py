from sys import stdin, stdout

def solve(n, k):
    ways = {frozenset(): 1}
    for i in range(1, n + 1):
        new_ways = dict()
        for used, w in ways.items():
            for value in range(max(1, i - k), min(n, i + k) + 1):
                if value in used or (i - k >= 1 and i - k not in used and value != i - k):
                    continue
                new = (used | {value}) - {i - k}
                new_ways[new] = (new_ways.get(new, 0) + w) % 998244353
        ways = new_ways

    return sum(ways.values()) % 998244353

def main():
    n, k = map(int, stdin.readline().split())
    stdout.write(str(solve(n, k)) + '\n')

if __name__ == "__main__":
    main()