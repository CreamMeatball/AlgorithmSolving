import sys

input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

row_prefixsum = [[0] * (M + 1) for _ in range(N)]
for i in range(N):
    for j in range(M):
        row_prefixsum[i][j + 1] = row_prefixsum[i][j] + board[i][j]

col_prefixsum = [[0] * M for _ in range(N + 1)]
for j in range(M):
    for i in range(N):
        col_prefixsum[i + 1][j] = col_prefixsum[i][j] + board[i][j]

count = 0
need = 2 * K + 1

for i in range(K, N - K):
    for j in range(K, M - K):
        row_sum = row_prefixsum[i][j + K + 1] - row_prefixsum[i][j - K]
        col_sum = col_prefixsum[i + K + 1][j] - col_prefixsum[i - K][j]
        if row_sum == need and col_sum == need:
            count += 1

print(count)