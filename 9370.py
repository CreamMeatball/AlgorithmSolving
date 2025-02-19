import sys
import heapq

input_data = sys.stdin.readline
max_size = 2000 * 2000 * 1000

T = int(input_data())

# 어디가 정답 도착지인지 모르니,
# 도착지를 정해놓지 않고 다익스트라를 시행해
# 일단 모든 node에 대한 최단 거리를 구함.
def dijkstra(start, n, graph):
    dist = [max_size] * (n + 1)
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cost, node = heapq.heappop(queue)
        if cost > dist[node]:
            continue
        for next_node, next_cost in graph[node]:
            new_cost = cost + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))
    return dist

for _ in range(T):
    n, m, t = map(int, input_data().split())
    s, g, h = map(int, input_data().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input_data().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
        
    candidates = [int(input_data()) for _ in range(t)]
    candidates.sort()
    
    # 세 출발지에서 다익스트라 실행
    dist_s = dijkstra(s, n, graph) # 출발점을 출발점으로 놓고 다익스트라 시행
    dist_g = dijkstra(g, n, graph) # g를 출발점으로 놓고 다익스트라 시행
    dist_h = dijkstra(h, n, graph) # h를 출발점으로 놓고 다익스트라 시행
    
    # g와 h 사이의 도로 길이 (문제에서 g-h 도로는 반드시 존재)
    for next_node, d in graph[g]:
        if next_node == h:
            dgh = d
            break
    
    answer = []
    for x in candidates:
        # s -> x의 최단 거리와,
        # (s -> g) + (g -> h) + (h -> x) 또는 (s -> h) + (h -> g) + (g -> x)
        # 가 일치하면 정답에 추가
        # dist_s[x] : s -> x(도착지 후보)의 최단 거리
        # dist_s[g] : s -> g의 최단 거리
        # dgh : g -> h의 거리
        if (dist_s[x] == dist_s[g] + dgh + dist_h[x]) or (dist_s[x] == dist_s[h] + dgh + dist_g[x]):
            answer.append(x)
    
    print(" ".join(map(str, answer)))