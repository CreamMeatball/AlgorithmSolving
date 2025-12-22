import sys

sys.setrecursionlimit(10**5)

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

X, Y = map(int, input().split())

# -1: 미방문, 0: 패배, 1: 승리
memo = [-1] * (Y + 1)

def can_win(curr):
    if memo[curr] != -1:
        return memo[curr]
    
    # 현재 상태에서 이길 수 있는 수가 하나라도 있으면 승리
    for next_val in range(curr + 1, Y + 1):
        if gcd(curr, next_val) == 1:
            # 상대방이 지는 선택지가 하나라도 있다면 나는 이길 수 있다
            if not can_win(next_val):
                memo[curr] = 1
                return True
                
    # 가능한 모든 수에 대해 상대방이 이긴다면 나는 진다
    memo[curr] = 0
    return False

if can_win(X):
    print("khj20006")
else:
    print("putdata")