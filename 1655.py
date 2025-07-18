import sys
import heapq

input = sys.stdin.readline

N = int(input())
left_heap = []  # 최대 힙 (리스트 왼쪽이 가장 큰 수임이 보장)
right_heap = [] # 최소 힙 (리스트 왼쪽이 가장 작은 수임이 보장)

for _ in range(N):
    num = int(input().rstrip())
    
    # 번갈아가며 힙에 추가: 왼쪽 힙의 개수가 같거나 더 많게 - '중간 위치'임을 확보하기 위해
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)
        
    # left_heap[0] 의 값이 항상 중간값(정답)이라고 할 수 있으려면
    # 무조건 left_heap[0] <= right_heap[0] 임이 보장돼야 됨.
    
    # 두 힙의 경계 조정 (left_heap의 최대값 <= right_heap의 최소값이 유지되게끔)
    # 위 구조에 의해 추가되다보면, left_heap[0]에 너무 큰 수가 들어가서, right_heap[0]의 값보다 커지는 경우가 생길 수 있음.
    if right_heap and -left_heap[0] > right_heap[0]:
        left_max = -heapq.heappop(left_heap)
        right_min = heapq.heappop(right_heap)
        
        heapq.heappush(left_heap, -right_min)
        heapq.heappush(right_heap, left_max)
    # left_heap[0] 값을 right_heap 으로 넘기면
    # 그 이전에는 left_heap[0] <= right_heap[0] 임이 보장돼있었으니까
    # 한 번만 넘겨주기만 하면 left_heap[0] <= right_heap[0] 임이 보장됨
    
    # ex)
    # 1 2 3 / 5 7 10
    # 이었을 때
    # 9 가 들어와서
    # 1 2 3 9 / 5 7 10
    # 이 됐으면, 여기서 right_heap 으로 넘겨주면
    # 1 2 3 / 5 7 10 9
    # 이런 식으로, 이전에 3 / 5 경계로 복구가 되니까
    
    # 중간값 출력 (항상 left_heap의 루트)
    print(-left_heap[0])