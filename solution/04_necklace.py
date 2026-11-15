from math import gcd

n, k = map(int, input().split())
mod = 1000000007
total = 0

for shift in range(n):
    length = gcd(n, shift)
    colors = pow(k - 1, length, mod)
    if length % 2 == 0:
        colors += k - 1
    else:
        colors -= k - 1
    total = (total + colors) % mod

if n % 2 == 0:
    reflection = k * pow(k - 1, n // 2, mod)
    total = (total + (n // 2) * reflection) % mod

print(total * pow(2 * n, mod - 2, mod) % mod)
