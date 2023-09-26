import sys
import heapq

input = sys.stdin.readline

N = int(input())
startEnd = []
for _ in range(N):
    startEnd.append(list(map(int, input().split())))

classroom = 1

startEnd.sort()

endTime = []

heapq.heappush(endTime, startEnd[0][1])

for i in range(1, N):
    if startEnd[i][0] < endTime[0]:
        heapq.heappush(endTime, startEnd[i][1])
        classroom += 1
    else:
        heapq.heappop(endTime)
        heapq.heappush(endTime, startEnd[i][1])
        
print(classroom)