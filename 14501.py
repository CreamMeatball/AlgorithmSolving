import sys

input = sys.stdin.readline

N = int(input().rstrip())

counsels = [(0, 0)]

for _ in range(N):
    counsels.append(tuple(map(int, input().rstrip().split())))
    
# print(counsels)

dp = [0] * (N + 2)

for i in range(1, N + 1):
    # 더 좋은 일을 위해, 일을 안하고 쉬고 넘어간 경우: 지금까지 누적된 '최대' 금액을 값으로 가져야 함.
    # if dp[i] == 0: # 이 코드는 틀림. 비효율적인 루트를 통해 dp[i] > 0 이 됐을 경우, 이 경로를 타지 못함. 즉, 이전에 더 좋은 루트를 통해 돈을 벌고 i날까지 쭉 쉬는 게 더 좋은 경우일 때를 탐색하지 못함.
    #     dp[i] = dp[i - 1]
    dp[i] = max(dp[i], max(dp[:i]))
    t, p = counsels[i]
    if i + t <= N + 1:
        dp[i + t] = max(dp[i + t], dp[i] + p)
#         print(f"i: {i}, dp: {dp[1:]}")

# print("  ".join(str(i).zfill(2) for i in range(1, N + 1)))
# print("  ".join(str(d).zfill(2) for d in dp[1:]))
print(max(dp[1:]))