def mex(arr:list) -> int:
    s = set(arr)
    x = 0
    
    while x in s:
        x+=1
        
    return x

def g(h:int, k:int, memo) -> dict:
    if h in memo: return memo[h]
    
    arr = []
    for b in range((h + k) // (k + 1), (h + 1) // 2):
        arr.append(g(h-b,k, memo) ^ g(b,k, memo))
        
    memo[h] = mex(arr)
    return memo[h]


def solve(n:int ,k:int, heaps:list) -> str:
    memo = {1:0, 2:0}
    max_n = max(heaps)
    
    ans = 0
    for h in heaps:
        ans ^= g(h,k, memo)
        
    if ans == 0: return "Lose 0"
    
    count = 0
    for h in set(heaps):
        for b in range((h + k) // (k + 1), (h + 1) // 2):
            after = ans ^ g(h, k, memo) ^ g(b, k, memo) ^ g(h-b, k, memo)
            if after == 0:
                count += 1

    return f"Win {count}"

import sys

input = sys.stdin.buffer.readline
write = sys.stdout.write

t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    heaps = list(map(int, input().split()))

    print(solve(n,k,heaps))