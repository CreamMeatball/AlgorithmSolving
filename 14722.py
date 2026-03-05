import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 종류가 나눠져있는 DP 문제는 len(종류)만큼 DP를 만들자.
dp = [[[0] * 3 for _ in range(n + 1)] for _ in range(n + 1)]

# dp[i][j][0]: (i, j)에서 딸기로 끝냈을 때 최대 우유 섭취 개수
# dp[i][j][1]: (i, j)에서 초코로 끝냈을 때 최대 우유 섭취 개수
# dp[i][j][2]: (i, j)에서 바나나로 끝냈을 때 최대 우유 섭취 개수

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 현재 (i, j) 위치에서의 우유 가게에서 파는 우유 종류
        kind = board[i-1][j-1] # board는 0-index고 dp에 쓸 i, j 는 1-index라서 맞춰주기
        
        up = dp[i-1][j]
        left = dp[i][j-1]

        # (i, j) 에서의 현재 값을 이전 값으로 임시로 갱신시켜놓기
        dp[i][j][0] = max(up[0], left[0]) # 현재 위치 (i, j)에서 딸기로 끝냈을 때 최대 우유 섭취 개수 갱신해놓기 = 이전 위쪽/왼쪽 위치에서 딸기로 끝낸 경우 중 더 큰 값
        dp[i][j][1] = max(up[1], left[1]) # 현재 위치 (i, j)에서 초코로 끝냈을 때 최대 우유 섭취 개수 갱신해놓기 = 이전 위쪽/왼쪽 위치에서 초코로 끝낸 경우 중 더 큰 값
        dp[i][j][2] = max(up[2], left[2]) # 현재 위치 (i, j)에서 바나나로 끝냈을 때 최대 우유 섭취 개수 갱신해놓기 = 이전 위쪽/왼쪽 위치에서 바나나로 끝낸 경우 중 더 큰 값
        
        if kind == 0: # 딸기
            dp[i][j][0] = max(dp[i][j][0], dp[i][j][2] + 1) # 이전에 딸기로 끝낸 값 유지 (우유 이번에 안 먹기) vs 이전에 바나나 먹고 이번에 딸기로 먹었을 때
        elif kind == 1: # 초코
            if dp[i][j][1] < dp[i][j][0]:
                dp[i][j][1] = max(dp[i][j][1], dp[i][j][0] + 1) # 이전에 초코로 끝낸 값 유지 (우유 이번에 안 먹기) vs 이전에 딸기 먹고 이번에 초코로 먹었을 때
        elif kind == 2: # 바나나
            if dp[i][j][2] < dp[i][j][1]:
                dp[i][j][2] = max(dp[i][j][2], dp[i][j][1] + 1) # 이전에 바나나로 끝낸 값 유지 (우유 이번에 안 먹기) vs 이전에 초코 먹고 이번에 바나나로 먹었을 때

print(max(dp[n][n]))
