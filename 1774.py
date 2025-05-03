import sys
import math
import heapq

input_data = sys.stdin.readline

N, M = map(int, input_data().rstrip().split())

gods = [None] # 인덱스를 1부터 시작하기 위한 dummy.
for i in range(N):
    x, y = map(float, input_data().rstrip().split())
    gods.append((x, y))

connected = set()
for i in range(M):
    a, b = map(int, input_data().rstrip().split())
    # 작은 인덱스가 앞에 오게끔
    if a > b:
        a, b = b, a
    connected.add((a, b))

# 기존에 연결해놓은 통로가 있으므로
# Prim 알고리즘 사용하면 될 듯

# Prim MST 알고리즘
# 시작 정점에서부터 출발하여 신장트리 집합을 단계적으로 확장 해나가는 방법.
# 정점 선택을 기반으로 하는 알고리즘이다.
# 이전 단계에서 만들어진 신장 트리를 확장하는 방법이다.

# Prim 알고리즘 동작 절차 (우선순위큐 버전)
# 임의의 시작 정점 s를 선택, visited = {s}.
# pq(min-heap)에 s에서 나가는 모든 간선 (가중치, from, to) 삽입.
# pq가 빌 때까지
# 가장 가벼운 간선 (w,u,v) 꺼냄.
# v가 아직 visited에 없으면
# MST에 (u,v,w) 추가,
# v를 visited에 넣고 v에서 나가는 간선들을 pq에 삽입.
# 간선이 |V|-1 개 선택되면 완료.

def cal_dis(a, b):
    a_x, a_y = a
    b_x, b_y = b
    distance = math.sqrt(abs((a_x - b_x)) ** 2 + abs((a_y - b_y)) ** 2)
    return distance

def prim():
    total_distance = 0
    visited = [False] * (N + 1)
    
    # (거리, 정점)
    min_heap = [(0, 1)]  # 1번 정점부터 시작
    
    while min_heap:
        dist, node = heapq.heappop(min_heap)
        
        if visited[node]:
            continue
            
        visited[node] = True
        total_distance += dist
        
        for next_node in range(1, N + 1):
            if node != next_node and not visited[next_node]:
                edge = (node, next_node) if node < next_node else (next_node, node)
                
                if edge in connected:
                    heapq.heappush(min_heap, (0, next_node))
                else:
                    edge_dist = cal_dis(gods[node], gods[next_node])
                    heapq.heappush(min_heap, (edge_dist, next_node))
    
    return total_distance

result = prim()
print("{:.2f}".format(result))