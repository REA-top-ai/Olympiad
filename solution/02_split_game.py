from sys import stdin, stdout

memo = {}
def can_split(m, b, k):
    a = m - b
    return a > b and a <= k * b

def win(piles, k):
    odd = []
    for p in set(piles):
        if piles.count(p) % 2 == 1:
            odd.append(p)
    piles = sorted(odd)

    key = (tuple(piles), k)
    if key in memo:
        return memo[key]

    result = False
    for i in range(len(piles)):
        m = piles[i]
        for b in range(1, m):
            if can_split(m, b, k):
                new_piles = piles[:i] + piles[i + 1:] + [m - b, b]
                if not(win(new_piles, k)):
                    result = True
                    break
        if result: break

    memo[key] = result
    return result


def solve(n, k, a):
    count = 0
    for m in set(a):
        rest = list(a)
        rest.remove(m)
        for b in range(1, m):
            if can_split(m, b, k):
                if not(win(rest + [m - b, b], k)):
                    count += 1

    return f'Win {count}' if count > 0 else 'Lose 0'
    
def main():
    t = int(stdin.readline())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        a = list(map(int, stdin.readline().split()))
        stdout.write(solve(n, k, a) + "\n")

if __name__ == "__main__":
    main()
