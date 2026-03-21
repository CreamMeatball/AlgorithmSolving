import sys
input = sys.stdin.readline

N = int(input().rstrip())
points = []
x_counts = {}
y_counts = {}

for _ in range(N):
    x, y = map(int, input().rstrip().split())
    points.append((x, y))
    x_counts[x] = x_counts.get(x, 0) + 1
    y_counts[y] = y_counts.get(y, 0) + 1

answer = 0
for x, y in points:
    answer += (x_counts[x] - 1) * (y_counts[y] - 1)

print(answer)