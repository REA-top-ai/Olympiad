import sys
sys.setrecursionlimit(5000)

def PossibleSolutions(leap, k):
    solutions = []
    for b in range(1, leap//2 + 1):
        a = leap - b
        if a > b and a <= k * b:
            solutions.append((a, b))
    return solutions        

def Mex(mexlist):
    mex = 0
    while mex in mexlist:
        mex += 1
    return mex

def Grundy(leap, k, cache):
    key = (leap, k)
    if key in cache:
        return cache[key]
    elif leap == 1 or leap == 2:
        cache[key] = 0
        return cache[key]
    else:
        mexlist = []
        possible_solutions = PossibleSolutions(leap, k)
        for solution in possible_solutions:
            mexlist.append(Grundy(solution[0], k, cache) ^ Grundy(solution[1], k, cache))
        grundy_number = Mex(mexlist)
        
        cache[key] = grundy_number
        return grundy_number    
    
def Xor(grundy_numbers):
    total_xor = 0
    for number in grundy_numbers:
        total_xor ^= number
    return total_xor

def IsWinning(leaps, k, cache):
    grundy_numbers = []
    for leap in leaps:
        grundy_numbers.append(Grundy(leap, k, cache))
    total_xor = Xor(grundy_numbers)
    if total_xor == 0:
        return 0
    else:
        c = 0
        for leap in set(leaps):
            solutions = PossibleSolutions(leap, k)
            for solution in solutions:
                turnchecker = grundy_numbers.copy()
                turnchecker.remove(Grundy(leap, k, cache))
                turnchecker.append(Grundy(solution[0], k, cache))
                turnchecker.append(Grundy(solution[1], k, cache))
                sol_result = Xor(turnchecker)
                if sol_result == 0:
                    c += 1
        return c

def main():
    cache = {}
    tests = int(input())
    for i in range(tests):
        n, k = map(int, input().split())
        leaps = list(map(int, input().split()))
        c = IsWinning(leaps, k, cache)
        if c > 0:
            print("Win", c)
        else:
            print("Lose", c)
            
main()