import sys

input = sys.stdin.readline

N = int(input())
levels = list(map(int, input().split()))

# '실수하는 횟수'를 누적합으로 계산해놓음.

prefix = [0] * (N + 1)
for i in range(1, N):
	prefix[i] = prefix[i - 1] + (1 if levels[i - 1] > levels[i] else 0)

Q = int(input())
out = []

for _ in range(Q):
	x, y = map(int, input().split())
	out.append(str(prefix[y - 1] - prefix[x - 1]))

sys.stdout.write("\n".join(out))