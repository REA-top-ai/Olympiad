from itertools import permutations

def solve(n:int,k:int) -> int:
    answer = 0

    for p in permutations(range(1, n + 1)):
        if all(abs(value - i) <= k for i, value in enumerate(p, start=1)):
            answer += 1

    return answer % 998244353
    

n,k = map(int, input().split())
print(solve(n,k))