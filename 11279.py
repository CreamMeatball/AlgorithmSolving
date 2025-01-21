import sys
import heapq

input_data = sys.stdin.readline

N = int(input_data().rstrip())
que = list()
# heapq는 기존이랑 똑같은 list를 쓰되, 넣을 때랑 뺄 때를 알고리즘적으로 다르게 처리.

for _ in range(N):
    data = int(input_data().rstrip())
    if data == 0:
        if que:
            print(heapq.heappop(que)[1])
            # heappop() return in format (priority, data)
        else:
            print(0)
    else:
        heapq.heappush(que, (-data, data))
        # heappush(list, (priority, data))
        # priority에 data를 음수로 넣어서 최소힙을 최대힙처럼 사용.
        # priority 값이 낮을 수록 우선순위가 높은 거임.