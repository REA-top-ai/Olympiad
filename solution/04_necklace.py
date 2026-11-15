def solve():
    n, k = map(int, input().split())
    seen = set()

    def dfs(p):
        if len(p) == n:
            mini = p
            for i in range(n):
                rot = p[i:] + p[:i]
                if rot < mini:
                    mini = rot
                rev = rot[::-1]
                if rev < mini:
                    mini = rev
            seen.add(mini)
        else:
            for c in range(k):
                ok = True
                if p and p[-1] == c:
                    ok = False
                if ok and len(p) == n - 1 and c == p[0]:
                    ok = False
                if ok:
                    dfs(p + (c,))

    dfs(())
    print(len(seen) % 1000000007)


if __name__ == "__main__":
    solve()
