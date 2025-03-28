import sys

input_data = sys.stdin.readline

N = []
count = 0

for _ in range(8):
    N.append(input_data().rstrip())
for i in range(8):
    for j in range(8):
        if i % 2 == 1 and j % 2 == 1 and N[i][j] == "F":
            count += 1
        if i % 2 == 0 and j % 2 == 0 and N[i][j] == "F":
            count += 1
print(count)
