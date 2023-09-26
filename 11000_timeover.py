import sys

input = sys.stdin.readline

N = int(input())
startEnd = []
for _ in range(N):
    startEnd.append(list(map(int, input().split())))

classroom = 1

startEnd.sort()

endTime = [-1]

for i in range(N):
    minimum = min(endTime)
    if minimum <= startEnd[i][0]:
        endTime[endTime.index(minimum)] = startEnd[i][1]
    else:
        classroom += 1
        endTime.append(startEnd[i][1])
        
print(classroom)
