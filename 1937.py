import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().rstrip())
forest = []
for _ in range(n):
    forest.append(list(map(int, input().rstrip().split())))
    
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dp = [[-1] * n for _ in range(n)] # 메모이제이션

def dfs(r, c):
    if dp[r][c] != -1:
        return dp[r][c]
    
    count = 1
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if (0 <= nr < n and 0 <= nc < n) and forest[r][c] < forest[nr][nc]:
            # count += dfs(nr, nc) # <- 모든 분기 경로의 합계
            count = max(count, 1 + dfs(nr, nc)) # <- 최장 길이를 타는 경우
            # 현재 dfs에서 탐색하는 방향이 네 방향인데, 거기서 가능한 방향 중,
            # 가장 길이 값이 높은 애로 결정하여, 현재 dfs의 좌표에서 그 방향을 선택한다고 보는 방식.
            
    dp[r][c] = count
    return count

max_count = 0

for i in range(n):
    for j in range(n):
        max_count = max(max_count, dfs(i, j))

# for d in dp:
#     print(d)

print(max_count)