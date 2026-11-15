from itertools import permutations

n, k = map(int, input().split())

c = 0
mass = []

while c < n:
    c += 1
    mass.append(c)

def replacement_check(mass: list, k: int):
    for i in range(len(mass)):
        if abs(mass[i] - (i + 1)) > k:
            return False
    return True
counter = 0
for replacement in permutations(mass):
    if replacement_check(replacement, k):
        counter += 1
print(counter % 998244353)