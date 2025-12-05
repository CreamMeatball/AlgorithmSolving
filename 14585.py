import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

candies = []

max_x = 0
max_y = 0

for _ in range(N):
    x, y = map(int, input().rstrip().split())
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    candies.append((x, y))
    
candies_pos = [[False] * (max_y + 1) for _ in range(max_x + 1)]

for x, y in candies:
    candies_pos[x][y] = True
    
# for c in candies_pos:
#     print(c)

dp = [[0] * (max_y + 1) for _ in range(max_x + 1)] # x, y 좌표만큼 다 초기화.

directions = [(1, 0), (0, 1)]

for i in range(max_x + 1):
    for j in range(max_y + 1):
        for d1, d2 in directions:
            x, y = i + d1, j + d2
            if (x < 0) or (x > max_x) or (y < 0) or (y > max_y):
                continue
            candy = int(M - (x + y)) if candies_pos[x][y] else 0
            dp[x][y] = max(dp[x][y], dp[i][j] + candy)
     
# for d in dp:
#     print(d)

result = 0
for d in dp:
    result = max(result, max(d))
print(result)