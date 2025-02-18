import heapq
import sys
input_data = sys.stdin.readline

N, K = map(int, input_data().split())

# visited = [False] * 100001
# 이진 visited로 하면 안 됨. 나중에 더 낮은 누적 시간으로 같은 노드에 도달할 수 있는 경우가 생길 수 있음.
max_cost = 100001 * 100
dist = [max_cost] * 100001
dist[N] = 0

def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, (0, start))
    dist[start] = 0

    while heap:
        current_time, current = heapq.heappop(heap)
        # if current_time > dist[current]:
        #     continue
        if current == end:
            return current_time
        
        for i, next_node in enumerate([current - 1, current + 1, current * 2]):
            if 0 <= next_node < 100001:
                add_time = 0 if i == 2 else 1
                new_time = current_time + add_time
                if new_time < dist[next_node]:
                    dist[next_node] = new_time
                    heapq.heappush(heap, (new_time, next_node))
    return -1

print(dijkstra(N, K))