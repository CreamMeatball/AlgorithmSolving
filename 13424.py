import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N, M = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    K = int(input())
    friends = list(map(int, input().split()))
    
    # 각 친구마다 모든 노드까지의 거리 다익스트라 전부 각각 계산
    
    # 모든 친구들의 각 방(1~N)까지의 거리 누적 총합 저장
    total_dist = [0] * (N + 1)

    def dijkstra(start):
        dist = [float('inf')] * (N + 1)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, curr = heapq.heappop(pq)
            if d > dist[curr]: continue
            for nxt, weight in graph[curr]:
                if dist[nxt] > d + weight:
                    dist[nxt] = d + weight
                    heapq.heappush(pq, (dist[nxt], nxt))
        return dist # 모든 방까지의 거리 전부 반환

    # 모든 친구의 위치에서 각각 다익스트라 수행
    for f_pos in friends:
        res = dijkstra(f_pos)
        for i in range(1, N + 1):
            total_dist[i] += res[i]

    # 최소 거리 합을 가진 방 번호 찾기 (거리가 같으면 번호가 작은 방 우선)
    min_val = float('inf')
    ans = 0
    for i in range(1, N + 1):
        if total_dist[i] < min_val:
            min_val = total_dist[i]
            ans = i
            
    print(ans)