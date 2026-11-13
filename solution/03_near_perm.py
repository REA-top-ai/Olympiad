#A
import sys
sys.setrecursionlimit(2000)
def solve():
    n, k = map(int, input().split())
    MOD = 998244353

    used = [False] * (n+1)
    count = 0
    def find_permutations(pos):
        nonlocal count

        if pos > n:
            count+=1
            return

        start_num = max(1, pos-k)
        end_num = min(n, pos+k)

        for num in range(start_num, end_num + 1):
            if not used[num]:
                used[num] = True
                find_permutations(pos+1)
                used[num] = False

    find_permutations(1)
    print(count % MOD)
solve()