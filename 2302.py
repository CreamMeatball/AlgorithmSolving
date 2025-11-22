import sys

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
VIPs = list(map(int, [input().rstrip() for _ in range(M)]))

# print(VIPs)

# ~ N 번까지의 자리가 있다고 할 때
# N 번째의 자리에 누가 앉을 수 있는지 경우를 따져보면:

# 1) N 번째 사람이 앉는 경우
# => N 번째 자리까지 있을 때 ~ N 까지 자리에 앉는 방법의 총 경우의 수: 1 * (N - 1 번째 자리에 어떻게 앉게되는지 경우의 수)

# 2) N - 1 번쨰 사람이 앉는 경우 = N 번째 사람은 N - 1 번째 자리에 앉게 됨
# => N 번째 자리까지 있을 때 ~ N 까지 자리에 앉는 방법의 총 경우의 수: 1 * 1 * (N - 2 번째 자리에 어떻게 앉게되는지 경우의 수)

# 3) N + 1 번째 사람이 앉는 경우는 없음. N 까지만 상정했기에, N + 1 번째가 존재하지 않으므로.

# -> 점화식으로 풀면
# dp[N] = 1 * dp[N - 1] + 1 * dp[N - 2]
#       = dp[N - 1] + dp[N - 2]
# 가 됨.
# => 피보나치랑 똑같음.

# 결국,
# N 개의 자리가 있을 때, 앉는 총 경우의 수 dp[N] 은 = dp[N - 1] + dp[N - 2] 이다.


# 이 상황에서,
# VIP 자리라는 건, 자리를 고정한다는 뜻.
# 그리고 좌석이 옮겨지는 경우는, 바로 옆자리로만 이동이 가능함.
# 그렇기에 이게 뭘 뜻하느냐,
# -> VIP 자리를 제외하고 나머지 빈 자리를 각각 별도의 N 자리 문제라고 보는 거임.

# VIP가 4, 7이면
# 1 2 3 [4] 5 6 [7] 8 9
# 1) 좌석 1~3번 (3칸)을 배치하는 경우의 수
# 2) 좌석 5~6번 (2칸)을 배치하는 경우의 수
# 3) 좌석 8~9번 (2칸)을 배치하는 경우의 수
# 로 분리된다는 거임.

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    
# print(dp)
    
sectors = list()
VIPs = [0] + VIPs

for i in range(1, len(VIPs)):
    current = VIPs[i]
    before = VIPs[i - 1]
    sectors.append(int(current - before - 1))
sectors.append(int(N - VIPs[-1]))
    
# print(sectors)
    
result = 1
    
for sector in sectors:
    if sector > 0: result *= dp[sector]
        
print(result)