import sys
input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())
trees = []

for _ in range(N):
    line = list(map(int, input().split()))
    trees.append(line[1:])

# 다익스트라나 0-1 BFS로도 풀 수 있음
# 위 두 개 알고리즘이 DP랑 성향이 비슷해서, DP/다익스트라/0-1BFS 3가지로 풀 수 있는 문제가 많은 듯

dp = [[float('inf')] * 21 for _ in range(N)]

for h in trees[0]:
    dp[0][h] = 0 if h in (1, 2) else 1

for i in range(1, N):
    for curr_h in trees[i]:
        for prev_h in trees[i-1]:
            reachable = {prev_h, min(prev_h + 1, 20), min(prev_h * 2, 20), max(prev_h - 1, 1)}
            cost = 0 if curr_h in reachable else 1
            
            dp[i][curr_h] = min(dp[i][curr_h], dp[i-1][prev_h] + cost)

ans = min(dp[N-1])
if ans > K:
    print(-1)
else:
    print(ans)
