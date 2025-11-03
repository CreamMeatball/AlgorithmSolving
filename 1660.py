N = int(input())

# 2229 문제랑 풀이 방식 유사

tetra = [] # 사면체 필요 개수들
triangular = 0 # 층별 대포알 개수들
k = 1
while True:
    triangular += k # 현재 층의 삼각수 계산 (1, 1+2, 1+2+3, ...)
    tetra_num = (tetra[-1] if tetra else 0) + triangular # 사면체 수 누적 (1, 1+3, 1+3+6, ...)
    
    if tetra_num > N:
        break
    
    tetra.append(tetra_num)
    k += 1

dp = [float('inf')] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    for coin in tetra:
        if i >= coin:
            dp[i] = min(dp[i], dp[i - coin] + 1)
        else:
            break

# print(dp[1:])
print(dp[N])