def cycle(length):
    r = pow(k - 1, length, MOD)
    if length % 2 == 0:
        r += k - 1
    else:
        r -= k - 1
    return r % MOD

MOD = 1000000007
n, k = map(int, input().split())
primes = []
x = n
p = 2
while p * p <= x:
    if x % p == 0:
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        primes.append((p, cnt))
    p += 1

if x > 1:
    primes.append((x, 1))
    
divs = [(1, 1)]
for p, cnt in primes:
    new = []
    for d, ph in divs:
        pk = 1
        for e in range(cnt + 1):
            if e == 0:
                new.append((d, ph))
            else:
                new.append((d * pk, ph * (pk - pk // p)))
            pk *= p
    divs = new

total = 0
for m, ph in divs:
    total += ph * cycle(n // m)
total %= MOD

if n % 2 == 0:
    total += n // 2 * k % MOD * pow(k - 1, n // 2, MOD)

print(total % MOD * pow(2 * n, MOD - 2, MOD) % MOD)
