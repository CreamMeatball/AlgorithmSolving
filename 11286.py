import sys
import heapq

input_data = sys.stdin.readline

N = int(input_data().rstrip())

numbers = []
for _ in range(N):
    data = int(input_data().rstrip())
    if data == 0:
        # heappush 할 때 heapq.heappush(numbers, (abs(data), data)) 와 같은 형태로 우선순위를 따로 설정해줬을 경우엔
        # (우선순위값, 실제값) 형태로 list에 push 되고, 고로 pop 할 때도 (우선순위값, 실제값) 형태로 pop 되므로
        # print(heapq.heappop(numbers)[1]) 이런식으로 실제값을 출력해줘야함.
        print(heapq.heappop(numbers)[1]) if numbers else print(0)
        # heapq가 원래 우선순위 값이 같은 경우엔 실제 값이 더 작은 값을 더 높은 우선순위로 해주나봄.
        # 그래서 문제의 조건을 알아서 충족함.
    else:
        heapq.heappush(numbers, (abs(data), data))