import sys
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

lamps = []
for _ in range(N):
    lamps.append(list(map(int, str(input().rstrip()))))
# print(lamps)
    
K = int(input().rstrip())

max_row = 0
zero_count_row = []

for row in range(N):
    counter = Counter(lamps[row])
    zeros = counter[0]
    zero_count_row.append(int(zeros))

visited = [False] * N

for row in range(N):
    zero_count = zero_count_row[row]
    count = 0
    if (zero_count <= K and (K - zero_count) % 2 == 0) and not visited[row]:
        for row2 in range(N):
            if not visited[row2]:
                if lamps[row] == lamps[row2]:
                    count += 1
                    visited[row2] = True
        # print(f"By Turn on the row: {row}, Total Turned On Row: {count}")
    max_row = max(max_row, count)

print(max_row)