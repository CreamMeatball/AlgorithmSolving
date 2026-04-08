import sys

input = sys.stdin.readline

R, C, Q = map(int, input().split())
prefix = [[0] * (C + 1) for _ in range(R + 1)]

for i in range(1, R + 1):
	row = list(map(int, input().split()))
	row_sum = 0
	for j in range(1, C + 1):
		row_sum += row[j - 1]
		prefix[i][j] = prefix[i - 1][j] + row_sum

out = []
for _ in range(Q):
	r1, c1, r2, c2 = map(int, input().split())
	total = prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1]
	count = (r2 - r1 + 1) * (c2 - c1 + 1)
	out.append(str(total // count))

sys.stdout.write("\n".join(out))