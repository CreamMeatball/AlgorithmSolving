import sys
sys.setrecursionlimit(10**7)
input_ = sys.stdin.readline

board = [list(map(int, input_().rstrip())) for _ in range(9)]

empties = [] # 빈 칸 좌표
# 행/열/3x3 에서 어떤 숫자가 이미 사용되었는지 기록용.
row_used   = [[False]*10 for _ in range(9)]
col_used   = [[False]*10 for _ in range(9)]
block_used = [[False]*10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        v = board[i][j]
        if v == 0:
            empties.append((i,j))
        else:
            row_used[i][v] = True
            col_used[j][v] = True
            b = (i // 3) * 3 + (j // 3)
            block_used[b][v] = True

def dfs(idx):
    if idx == len(empties):
        for row in board:
            print(''.join(map(str, row)))
        sys.exit(0)

    i, j = empties[idx]
    b = (i // 3) * 3 + (j // 3) # 넣어볼 숫자
    for k in range(1, 10):
        if (not row_used[i][k] # 넣어볼 숫자(b)가 행에서 아직 사용 안했을 경우
            and not col_used[j][k] # 넣어볼 숫자(b)가 열에서 아직 사용 안했을 경우
            and not block_used[b][k]): # 넣어볼 숫자(b)가 3x3에서 아직 사용 안했을 경우
            board[i][j] = k
            row_used[i][k] = col_used[j][k] = block_used[b][k] = True

            dfs(idx + 1)

            # 백트래킹 복귀
            board[i][j] = 0
            row_used[i][k] = col_used[j][k] = block_used[b][k] = False

dfs(0)