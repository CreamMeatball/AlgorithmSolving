import sys
import heapq

input_data = sys.stdin.readline

N = int(input())
numbers = []

for _ in range(N):
    data = int(input_data().rstrip())
    if data == 0:
        if numbers:
            print(heapq.heappop(numbers))
        else:
            print(0)
    else:
        heapq.heappush(numbers, data)
        # heapq.heappush(numbers, (data, data))