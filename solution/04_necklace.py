import sys

MOD = 1000000007


def factorize(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def main():
    n, k = map(int, sys.stdin.read().split())
    km = (k - 1) % MOD

    def P(d):
        return (pow(km, d, MOD) + (km if d % 2 == 0 else -km)) % MOD


    divs = [(1, 1)]
    items = [(1, 1)]
    for p, e in factorize(n).items():
        new = []
        for d, ph in items:
            pk = 1
            for i in range(e + 1):
                new.append((d * pk, ph * (pk - pk // p if i else 1)))
                pk *= p
        items = new
    total = 0
    for q, phq in items:
        total += phq % MOD * P(n // q)
    if n % 2 == 0:
        total += (n // 2) % MOD * (k % MOD) % MOD * pow(km, n // 2, MOD)
    total %= MOD
    print(total * pow(2 * n, MOD - 2, MOD) % MOD)


main()
