def solve(n:int ,k:int, a:list) -> str:
    max_n = max(a)

    for i in range()


import sys

input = sys.stdin.buffer.readline
write = sys.stdout.write

t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))

    print(solve(n,k,a))