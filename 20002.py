import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 2차원 누적합

pref = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        pref[i][j] = arr[i-1][j-1] + pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1]

answer = -float('inf')

for k in range(1, N + 1):
    for i in range(k, N + 1):
        for j in range(k, N + 1):
            current_sum = pref[i][j] - pref[i-k][j] - pref[i][j-k] + pref[i-k][j-k]
            if current_sum > answer:
                answer = current_sum

print(answer)
