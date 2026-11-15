def mex(arr:list) -> int:
    s = set(arr)
    x = 0
    
    while x in s:
        x+=1
        
    return x

def calculate_grandi(h:int, k:int) -> dict:
    g = {1:0, 2:0}
    
    for i in range(3,h+1):
        arr = []
        for b in range((i + k) // (k + 1), (i + 1) // 2):
            arr.append(g[i-b] ^ g[b])
            
        g[i] = mex(arr)
        
    return g
        

def solve(n:int ,k:int, heaps:list) -> str:
    max_heap = max(heaps)
    g = calculate_grandi(max_heap, k)
    
    ans = 0
    for h in heaps:
        ans ^= g[h]
        
    if ans == 0: return "Lose 0"
    
    count = 0
    for h in set(heaps):
        for b in range((h + k) // (k + 1), (h + 1) // 2):
            after = ans ^ g[h] ^ g[h-b] ^ g[b]
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