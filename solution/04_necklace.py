import sys

MOD = 1000000007
n, k = map(int, sys.stdin.readline().split())


def phi(x):
    result = x
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            result -= result // p
        p += 1
    if x > 1:
        result -= result // x
    return result


def divisors(x):
    result = []
    d = 1
    while d * d <= x:
        if x % d == 0:
            result.append(d)
            if d * d != x:
                result.append(x // d)
        d += 1
    return result


def cycle_colorings(length):
    if length == 1:
        return 0
    return (pow(k - 1, length, MOD) +
            (k - 1 if length % 2 == 0 else -(k - 1))) % MOD

rotation_sum = 0
for d in divisors(n):
    rotation_sum += phi(n // d) * cycle_colorings(d)
    rotation_sum %= MOD

reflection_sum = 0
if n % 2 == 0:
    reflection_sum = (n // 2) * k * pow(k - 1, n // 2, MOD)
    reflection_sum %= MOD

answer = (rotation_sum + reflection_sum) % MOD
answer = answer * pow(2 * n, MOD - 2, MOD) % MOD
print(answer)
