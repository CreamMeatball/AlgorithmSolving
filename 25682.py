# PyPy로 해야 시간초과 안 남.
# Python3로 컴파일 시 시간초과 남.

import sys
input_data = sys.stdin.readline

N, M, K = map(int, input_data().split())

arr = []
for _ in range(N):
    temp = input_data().rstrip()
    # B->0, W->1 로 저장
    temp = [0 if c == 'B' else 1 for c in temp]
    arr.append(temp)

# 일부분만 효율적으로 탐색해서 바꾸든, 어떻게 바꾸든
# 결국 모양은 흑백흑백 or 백흑백흑 형태의 판이 됨.
# 그렇기 때문에 지저분하게 다양한 조건부 식을 통해 변경해야하는 값인지 아닌지 판단할 필요 없이
# 그냥 단순하게 "짝수칸에 흑일 경우 옳고 아닐 경우 틀리다", 와 같은 방식으로 옳고 틀림을 판단하면 최적의 방식임.
# 단, 이 때 "짝수칸이 백일 경우" 도 함께 고려해서 2가지 형태로 고려해주면 됨.

# 두 가지 패턴에 대한 누적합 배열 계산
# black_prefix[y][x]: (0,0)이 'B'일 때 (y,x)까지 칠해야 하는 누적합
# white_prefix[y][x]: (0,0)이 'W'일 때 (y,x)까지 칠해야 하는 누적합
black_prefix = [[0]*(M+1) for _ in range(N+1)]
white_prefix = [[0]*(M+1) for _ in range(N+1)]

for r in range(N):
    for c in range(M):
        # (r+c) 짝수 칸은 'B'여야 하고, 홀수 칸은 'W'여야 함
        # arr[r][c] == 0 이면 B, 1이면 W
        # 'B'가 맞으면 cost_B=0, 틀리면 cost_B=1
        # 'W'가 맞으면 cost_W=0, 틀리면 cost_W=1
        correct_black = 0 if (r+c)%2==0 else 1
        correct_white = 1 if (r+c)%2==0 else 0
        cost_b = 1 if arr[r][c] != correct_black else 0
        cost_w = 1 if arr[r][c] != correct_white else 0

        black_prefix[r+1][c+1] = black_prefix[r][c+1] + black_prefix[r+1][c] - black_prefix[r][c] + cost_b
        white_prefix[r+1][c+1] = white_prefix[r][c+1] + white_prefix[r+1][c] - white_prefix[r][c] + cost_w

# K x K 부분에서 다시 칠해야 하는 칸의 최솟값 탐색
answer = float('inf')
for r in range(N-K+1):
    for c in range(M-K+1):
        # black_prefix, white_prefix 배열의 행과 열을 1개씩 늘려서 만들었기 때문에,
        # 누적합 - 부분합 계산 시 행==0 or 열==0 과 같은 경우를 따로 처리하지 않아도 됨.
        
        # 블랙 패턴 기준 다시 칠해야 할 갯수
        black_cost = black_prefix[r+K][c+K] - black_prefix[r][c+K] - black_prefix[r+K][c] + black_prefix[r][c]
        # 화이트 패턴 기준 다시 칠해야 할 갯수
        white_cost = white_prefix[r+K][c+K] - white_prefix[r][c+K] - white_prefix[r+K][c] + white_prefix[r][c]
        answer = min(answer, black_cost, white_cost)

print(answer)