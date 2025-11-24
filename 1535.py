import sys
input = sys.stdin.readline

N = int(input().rstrip())
L = [0] + list(map(int, input().rstrip().split()))
J = [0] + list(map(int, input().rstrip().split()))    

dp = [0] * 101

for i in range(1, N + 1):
    w, v = L[i], J[i]
    # 역순으로 순회하며 DP 테이블 갱신 (0/1 Knapsack)
    # 정순으로 구현하려면 2차원 DP 써야함.
    for j in range(100, w, -1): # 원래 방식은 w - 1 인데, 체력이 0 혹은 음수면 안된다는 조건이 있으므로 1 올려서 w 로.
        dp[j] = max(dp[j], dp[j - w] + v)

# print(dp)

print(dp[100])