import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

extended = A + A[: K - 1]

window_sum = sum(extended[:K])
max_sum = window_sum

for i in range(1, N):
	window_sum += extended[i + K - 1] - extended[i - 1]
	if window_sum > max_sum:
		max_sum = window_sum

print(max_sum)