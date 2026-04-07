import sys

input = sys.stdin.readline

N, L = map(int, input().split())
a = list(map(int, input().split()))

current = 0
answer = 0

for i in range(N):
	current += a[i]
	if i >= L:
		current -= a[i - L]
	if 129 <= current <= 138:
		answer += 1

print(answer)