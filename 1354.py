import sys

sys.setrecursionlimit(10**5)

n, p, q, x, y = map(int, input().split())

# memoization
memo = {0: 1}

def calculate(i):
    if i <= 0:
        return 1
    
    if i in memo:
        return memo[i]
    
    val = calculate(i // p - x) + calculate(i // q - y)
    
    memo[i] = val
    return val

print(calculate(n))