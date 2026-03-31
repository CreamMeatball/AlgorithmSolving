import sys

input = sys.stdin.readline

N, K, B = map(int, input().split())
broken = [0] * (N + 1)

for _ in range(B):
    broken[int(input().rstrip())] = 1

ps = [0] * (N + 1)
for i in range(1, N + 1):
    ps[i] = ps[i - 1] + broken[i]

answer = K
for s in range(1, N - K + 2):
    e = s + K - 1
    answer = min(answer, ps[e] - ps[s - 1])

print(answer)