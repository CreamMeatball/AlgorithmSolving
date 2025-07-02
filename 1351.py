import sys
sys.setrecursionlimit(10**6)  # 재귀 제한 증가

N, P, Q = map(int, input().split())

# 모든 A값이 다 필요하지가 않음.
# (실제로 N 크기의 A 배열 만들고 해봤는데 메모리 초과 남)

# Top-Down 재귀
# 집합과 맵 (dictionary)
# DP

# memoization
dp = {0: 1}

def find(n: int):
    if n in dp:
        return dp[n]
    
    dp[n] = find(n//P) + find(n//Q)
    return dp[n]
    
result = find(N)
print(result)

# print(dp)

# dp[3]이 없는 이유 (AI)
# Top-Down 방식의 다이내믹 프로그래밍을 사용하고 있어서, 필요한 값만 계산합니다. find(N)에서 시작해 필요한 값들만 재귀적으로 계산하는 구조입니다.

# N=256으로 시작할 때 재귀 호출의 흐름을 보면:

# find(256) → find(256//2) + find(256//4) = find(128) + find(64)
# find(128) → find(64) + find(32)
# find(64) → find(32) + find(16)
# ...
# 이런 식으로 계속 P=2와 Q=4로 나누어 내려갑니다. 이 과정에서 다음 숫자들만 등장합니다: 256, 128, 64, 32, 16, 8, 4, 2, 1, 0

# 그래서 i=6인 경우는 애초에 계산 과정에서 발생하지 않습니다. find(6)이 호출되지 않으므로 dp[6] = dp[3] + dp[1]과 같은 계산이 필요하지 않고, 따라서 dp[3]도 계산되지 않는 것입니다.