import itertools
MOD = 1000000007
n, k = map(int, input().split())
necklaces = set()

for a in itertools.product(range(k), repeat=n):
    good = True

    for i in range(n):
        if a[i] == a[(i + 1) % n]:
            good = False
            break

    if not good:
        continue

    forms = []

    for p in range(n):
        forms.append(a[p:] + a[:p])

    b = a[::-1]

    for p in range(n):
        forms.append(b[p:] + b[:p])

    canonical = min(forms)

    necklaces.add(canonical)

print(len(necklaces) % MOD)