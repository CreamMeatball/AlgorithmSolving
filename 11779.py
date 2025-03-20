import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

# 간선 weight(cost)가 있으니까 bfs 같은 거 말고 다익스트라(dijkstra)로 풀어야 함

# 출발 노드에서 도착 노드까지의 최저 비용 구하는 알고리즘.
# 약간 greedy 함.
# 1. 출발 노드를 설정
# 2. (출발점에서) 모든 노드까지의 필요 비용을 무한대로 설정 (dist)
# 3. 출발 노드를 현재 노드로 설정
# 4. 현재 노드에서 연결돼있는 인접 노드로 가는 데에 드는 비용을 확인 후 '이전 cost + 가야할 cost'가 기존 dist 보다 적을 경우 dist 갱신
# 5. 4. 에서 확인한 인접 노드 중 가장 비용이 적게 드는 노드를 현재 노드로 설정
# 6. 4. 5. 반복
# 7. 결국 출발 노드에서 도착 노드까지의 최저 비용이 dist 에 저장됨
# * 변경되는 현재 노드: 출발점에서 그 현재 노드를 경유해서 도착점까지 갔을 때의 경우가 되는 것

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

dist = [float('inf')] * (n + 1)
prev = [0] * (n + 1) # backtracking용
dist[start] = 0

heap = []
heapq.heappush(heap, (0, start))
while heap:
    cost, current = heapq.heappop(heap)
    if dist[current] < cost:
        continue
    for next, w in graph[current]:
        if cost + w < dist[next]:
            dist[next] = cost + w
            prev[next] = current
            heapq.heappush(heap, (dist[next], next))

print(dist[end])

path = []
current = end
while current:
    path.append(current)
    current = prev[current]

print(len(path))
print(*path[::-1])