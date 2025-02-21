import sys
import heapq

input_data = sys.stdin.readline

n = int(input_data())
m = int(input_data())

# bus = [[] for _ in range(n + 1)]
# for _ in range(m):
#     a, b, c = map(int, input_data().split())
#     bus[a].append((b, c))
    
max_value = 100000 * 1000

# def dijkstra(start):
#     dist = [max_value] * (n + 1)
#     q = []
#     heapq.heappush(q, (0, start))
#     dist[start] = 0
#     while q:
#         cost, current = heapq.heappop(q)
#         for b in bus[current]:
#             next, next_cost = b
#             new_cost = cost + next_cost
#             if new_cost < dist[next]:
#                 dist[next] = new_cost
#                 heapq.heappush(q, (new_cost, next))
#     return dist

# for i in range(1, n + 1):
#     dist = dijkstra(i)
#     for j in range(1, n + 1):
#         if dist[j] == max_value:
#             print(0, end=' ')
#         else:
#             print(dist[j], end=' ')
#     print()
# 시간 초과 남

# '하나의 출발점에서 다른 모든 정점까지의 최단 거리'를 구하는 다익스트라 알고리즘은 O(mlogn)
# 이걸 n번 반복하니 O(nmlogn)이 되어 시간 초과가 난다.

# '모든 출발점에서 다른 모든 정점까지의 최단 거리'를 구하는 플로이드-워셜 알고리즘을 사용하면 O(n^3)


# 2차원 리스트 dist 초기화: 출발지와 도착지가 같으면 0, 나머지는 max_value
dist = [[max_value if i != j else 0 for j in range(n + 1)] for i in range(n + 1)]

# 버스 정보를 입력받아서, 출발 도시 a에서 도착 도시 b로 가는 최소 비용을 갱신
for _ in range(m):
    a, b, c = map(int, input_data().split())
    if c < dist[a][b]:
        dist[a][b] = c

# 플로이드-워셜 알고리즘 수행
# 출발지(i) -> 경유지(k) -> 도착지(j) 의 최단 거리를 구하는데
# 모든 i, j, k에 대해 다 진행함
for k in range(1, n + 1): # k: 중간에 거칠 node
    for i in range(1, n + 1): # i: 출발 node
        for j in range(1, n + 1): # j: 도착 node
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 결과 출력: 도달할 수 없는 경우 0 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(dist[i][j] if dist[i][j] != max_value else 0, end=' ')
    print()