import sys
import math

def main_sem_pan():
    # 1. Читаем данные (n и k)
    line = sys.stdin.readline().strip()
    if not line:
        return
    n, k = map(int, line.split())
    
    MOD = 1000000007
    if k == 1:
        print(0)
        return
    total_s = 0
    for i in range(1, n + 1):
        d = math.gcd(i, n)
        term1 = pow(k - 1, d, MOD)
        
        if d % 2 == 0:
            term2 = (k - 1) % MOD
        else:
            term2 = -(k - 1) % MOD 
        p_d = (term1 +term2) %MOD
        total_s = (total_s + p_d) % MOD
        
    if n % 2 == 0:
        h_n = n // 2
        ref_sum= (h_n * k) % MOD
        ref_sum = (ref_sum * pow(k- 1, h_n, MOD)) % MOD
        
        total_s = (total_s +ref_sum)% MOD
        
    inv_2n = pow(2 * n, MOD - 2, MOD)
    ans = (total_s * inv_2n) % MOD
    return ans

if __name__ == '__main__':
    print(main_sem_pan())