N, X = map(int, input().rstrip().split())

# [풀이 1]
# dp = [None] * (N + 1)
# dp[0] = 'P'
# for i in range(1, N + 1):
#     dp[i] = 'B' + dp[i - 1] + 'P' + dp[i - 1] + 'B'

# # for d in dp:
# #     print(d)

# result = 0
# for s in dp[N][:X+1]:
#     if s == 'P':
#         result += 1
        
# print(result)

# [풀이 2]
# a = 'P'
# b = 'BPPPB'

# for i in range(1, N + 1):
#     a = b
#     b = 'B' + a + 'P' + a + 'B'
#     b = b[:X+1]
    
# # print(a, b)
    
# result = 0 
# for s in b[:X+1]:
#     if s == 'P':
#         result += 1
        
# print(result)

# [풀이 3]
import sys

sys.setrecursionlimit(10**5)

burger = [0] * 51
patty = [0] * 51

burger[0] = 1 # 각 레벨의 전체 층 수
patty[0] = 1 # 각 레벨의 패티 존재 수

for i in range(1, N + 1):
    burger[i] = 1 + burger[i-1] + 1 + burger[i-1] + 1
    patty[i] = patty[i-1] + 1 + patty[i-1]

# 패턴 자체가
# 번1 + 버1 + 패 + 버2 + 번2
# 이니까
# 이 5단계에서 X가 어디 위치해있는지에 따라
# 수학적으로 패티가 몇 개인지 구할 수가 있음 (이렇게 안 하면 메모리 초과 / 시간 초과 남)

# 패턴을 이용해 수학적으로 효율 계산하자
# 재귀 사용하자 (DP)

def eat(n, x):
    if n == 0:
        return 1
    
    # 1) 번 단계
    if x == 1:
        return 0
    
    # 2) 버1 단계
    elif x <= 1 + burger[n-1]:
        return eat(n-1, x-1) # 재귀
    
    # 3) 패 단계
    elif x == 1 + burger[n-1] + 1:
        return patty[n-1] + 1
    
    # 4) 버2 단계
    elif x <= 1 + burger[n-1] + 1 + burger[n-1]:
        return patty[n-1] + 1 + eat(n-1, x - (1 + burger[n-1] + 1)) # 재귀
    
    # 5) 번2 단계
    else:
        return patty[n]

print(eat(N, X))