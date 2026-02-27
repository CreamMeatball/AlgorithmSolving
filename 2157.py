import sys
from collections import defaultdict

input = sys.stdin.readline

n, m, k = map(int, input().split())
edges = defaultdict(list)

for _ in range(k):
    a, b, c = map(int, input().split())
    if a < b:
        edges[a].append((b, c))

# M개 이하여야한다는 제약을 dp[m] 까지로 설정하여 제약 적용 및 해결

dp = [[-1] * (n + 1) for _ in range(m + 1)]
dp[1][1] = 0

for i in range(1, m):
    for cur in range(1, n + 1):
        if dp[i][cur] == -1:
            continue
        for nxt, score in edges[cur]:
            if dp[i + 1][nxt] < dp[i][cur] + score:
                dp[i + 1][nxt] = dp[i][cur] + score

ans = 0
for i in range(1, m + 1):
    if dp[i][n] > ans:
        ans = dp[i][n]

print(ans)