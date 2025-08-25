import sys

input = sys.stdin.readline

T, W = map(int, input().rstrip().split())

drops = [0] + [int(input().rstrip()) for _ in range(T)]

dp = [[0] * (W + 1) for _ in range(T + 1)]

# print(dp)

for t in range(1, T + 1):
    for w in range(W + 1):
        # 움직이지 않았을 때 (w=0) -> 이전 상태 그대로
        if w == 0:
            dp[t][w] = dp[t-1][w]
            if drops[t] == 1:  # 1번 나무에 있음
                dp[t][w] += 1
        else:
            # w번 움직였을 때
            dp[t][w] = max(dp[t-1][w-1], dp[t-1][w])
            current_pos = 1 if w % 2 == 0 else 2
            if drops[t] == current_pos:
                dp[t][w] += 1
        
# for d in dp[1:]:
#     print(d)
print(max(dp[T]))