import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 문제에서 말하는 2차원 배열에서의 부분행렬이라는 건
# 꽉 찬 직사각형 형태의 부분행렬을 뜻하는 듯

# 카데인 알고리즘(부분최대합)을 2차원 행렬로 확장하기
# DP 개념으로 보아
# 행의 일부까지만 범위로 한정한다음, 그 범위에서의 최대를 구하고
# 행 범위를 확장시켜나가면서 최대값을 구함.

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().rstrip().split())))

prefix_sum = [[0] * M for _ in range(N + 1)]
for i in range(N):
    for j in range(M):
        prefix_sum[i+1][j] = prefix_sum[i][j] + matrix[i][j]

max_sum = -float('inf')

for i in range(N):
    for j in range(i + 1, N + 1):
        current_kadane = 0
        for k in range(M):
            col_sum = prefix_sum[j][k] - prefix_sum[i][k]
            current_kadane += col_sum
            if current_kadane > max_sum:
                max_sum = current_kadane
            if current_kadane < 0:
                current_kadane = 0

print(max_sum)