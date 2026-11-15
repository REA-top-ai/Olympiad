MOD = 1000000007


def mod_power(base, exponent):
    result = 1
    while exponent:
        if exponent % 2:
            result = result * base % MOD
        base = base * base % MOD
        exponent //= 2
    return result


def solve(n, k):
    factors = []
    remaining = n
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            power = 0
            while remaining % p == 0:
                remaining //= p
                power += 1
            factors.append((p, power))
        p += 1
    if remaining > 1:
        factors.append((remaining, 1))
    divisors = [(1, 1)]
    for p, power in factors:
        added = []
        part = 1
        phi = 1
        for exponent in range(1, power + 1):
            part *= p
            if exponent == 1:
                phi = p - 1
            else:
                phi *= p
            for d, value in divisors:
                added.append((d * part, value * phi))
        divisors += added
    total = 0
    for d, phi in divisors:
        length = n // d
        ways = mod_power(k - 1, length)
        if length % 2 == 0:
            ways += k - 1
        else:
            ways -= k - 1
        total = (total + phi * ways) % MOD
    if n % 2 == 0:
        total += (n // 2) * k * mod_power(k - 1, n // 2)
        total %= MOD
    return total * mod_power(2 * n, MOD - 2) % MOD


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(solve(n, k))
