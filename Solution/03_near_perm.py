n, k = map(int, input().split())
p = 998244353
if n <= 10:
    #Подзадача А
    dp = [0]*(1<<n)
    dp[0] = 1
    for znach in range(1<<n):
        i = bin(znach).count('1')+1
        for q in range(1, n+1):
            if not znach >> (q - 1) & 1 and abs(q-i) <= k:
                dp[znach | 1 << (q-1)] += dp[znach]
    print(dp[-1])
#Подзадача В
elif k >= n - 1:
    ans = 1
    for i in range(1, n + 1):
        ans = (ans * i) % p
    print(ans)
elif k == 0:
    print(1)
elif k == 1:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % p
    print(dp[n])
elif k == 2:
    dp = [0, 1, 2, 6, 14, 31] + [0] * (n - 5)
    for i in range(6, n + 1):
        dp[i] = (2 * dp[i - 1] + 2 * dp[i - 3] - dp[i - 5]) % p
    print(dp[n])