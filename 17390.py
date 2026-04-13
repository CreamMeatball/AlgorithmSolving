import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

B = sorted(A)
prefix = [0] * (N + 1)
for i in range(1, N + 1):
	prefix[i] = prefix[i - 1] + B[i - 1]

result = []
for _ in range(Q):
	L, R = map(int, input().split())
	result.append(str(prefix[R] - prefix[L - 1]))

print("\n".join(result))