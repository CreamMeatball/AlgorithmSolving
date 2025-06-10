import sys

input_ = sys.stdin.readline

N = int(input_().rstrip())
status = [-1] + list(map(int, input_().rstrip().split()))
M = int(input_().rstrip())
students = []
for _ in range(M):
    students.append((map(int, input_().rstrip().split())))


for i in range(M):
    sex, num = students[i]
    if sex == 1:
        for j in range(num, N + 1, num):
            status[j] = 1 if status[j] == 0 else 0
    elif sex == 2:
        idx1, idx2 = num, num
        while True:
            if (idx1 - 1) >= 1 and (idx2 + 1) <= N and status[idx1 - 1] == status[idx2 + 1]:
                idx1 -= 1
                idx2 += 1
            else:
                break
        for j in range(idx1, idx2 + 1):
            status[j] = 1 if status[j] == 0 else 0
            
for i in range(1, N + 1, 20):
    print(*status[i:i+20])