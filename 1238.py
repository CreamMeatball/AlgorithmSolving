import sys
import heapq

input_data = sys.stdin.readline

N, M, X = map(int, input_data().rstrip().split())

# floyd warshall이 시간 초과 나서
# dijkstra * N * 2 번 반복해보기
# -> 와 이거 dijkstra 일일이 여러번 안해주고도 계산할 수 있는 방법이 있음: reverse dijkstra
# 단방향 경로를 반대로 설정하는 거임 ㄷㄷ;

graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input_data().rstrip().split())
    graph[u].append((v, w))        # u -> v 방향
    reverse_graph[v].append((u, w))  # v -> u 방향(역방향)

def dijkstra(start, graph):
    distance = [float('inf')] * (N + 1) # 어차피 여러번 다익스트라 해줘야하기 때문에, 호출될 때 dist 새로 초기화해서 사용하게끔
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        current_dist, current_pos = heapq.heappop(queue)
        
        # heapq이기 때문에 선입선출이 아니라서
        # 나중에 pop된 경우에 앞서 계산된 최적보다 어차피 dist가 클 경우에 스킵하게끔
        if current_dist > distance[current_pos]:
            continue
        
        for g in graph[current_pos]:
            next_pos, next_dist = g
            dist = current_dist + next_dist
            if dist < distance[next_pos]:
                distance[next_pos] = dist
                heapq.heappush(queue, (dist, next_pos))
                
    return distance

# X에서 모든 마을로의 최단거리
# 쓸데없이 여러번 안해주고, X를 출발점으로 잡음으로써 X로부터 다른 모든 노드까지의 최단거리 구함.
to_home = dijkstra(X, graph)

# 모든 마을에서 X로의 최단거리
# 와 이게 킥임 ㄷㄷ;;
# 각 노드에서 X까지 가는 걸, N번의 다익스트라 수행이 아닌
# 출발점을 반대로 X로 잡고, 경로를 역으로 설정한 reverse graph를 이용함으로써
# 한 번만에 모든 노드로부터 X로의 최단 거리를 구함.
to_party = dijkstra(X, reverse_graph)

# 각 학생별 왕복 시간 계산 및 최대값 찾기
max_time = 0
for i in range(1, N + 1):
    total_time = to_party[i] + to_home[i]
    max_time = max(max_time, total_time)

print(max_time)