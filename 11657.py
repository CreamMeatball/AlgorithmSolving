import sys

input_data = sys.stdin.readline
INF = 6000 * 10000  # 충분히 큰 값

N, M = map(int, input_data().split())
dist = [INF] * (N + 1)
edges = []
for _ in range(M):
    A, B, C = map(int, input_data().split())
    edges.append((A, B, C))
    # graph[u] = v 처럼 더하는 방식이 아님.

# 새로운 cost값이 기존 cost값보다 작은 경우에 append 하는 다익스트라로 풀 경우
# 음수 가중치가 있는 경우를 주의해야 함.
# 어떠한 사이클의 cost 총합이 음수가 되는 경우가 있을 경우
# cost가 무한히 낮아져서, 같은 사이클을 무한히 도는 문제가 발생함.

# 벨만-포드 알고리즘 사용
# 다익스트라보다 오래 걸리는 대신, 음수 사이클이 있는 경우를 판별 가능.
# 다익스트라는 새 가중치가 기존 가중치보다 클 경우, 계산하지 않고 생략하는데
# 벨만-포드는 무조건 모든 노드의 모든 간선에 대해 다 탐색함.
# 그렇기에 음의 가중치로 인한 음수 사이클이 있어도 판별 가능.
def bellman_ford(start):
    dist[start] = 0 # dist[node]: node까지가는 최소의 거리.
    # N번의 라운드를 반복
    for i in range(1, N + 1): # 모든 간선에 대해 전체 순환을 N번 반복(이중반복문). node에 대해가 아니라 간선에 대해.
        # 순환 순서는 처음에 간선을 입력받은 대로.
        for A, B, C in edges: # 모든 간선에 대해 순환
            if (dist[A] < INF) and (dist[A] + C < dist[B]):
                # dist[A]: 간선의 출발점인 node까지 도달에 걸리는 최소 거리. dist[B]: 간선의 도착점인 node까지 도달에 걸리는 최소 거리.
                # 즉, 조건문의 뜻은 "A를 거쳐서 B로 가는 길이, 기존에 B로 가는 길보다 짧다면"
                # (dist[A] < INF): 출발점이 INF라면(가장 처음 출발점에서부터 아직 한 번도 도달하지 못했거나, 가는 길이 없어 도달할 수 없는 곳) 어차피 갱신시킬 수 없기 때문에 제외하는 것.
                # 이 때문에, 처음에는 길을 안뚫어놔서 출발점이 INF라 탐색하지 못하고 스킵한 경우들이 생김. 그렇기에 최대 N-1번까지 해봐야 가능한 모든 경우를 다 해 볼 수 있음.
                dist[B] = dist[A] + C
                # N번째 라운드에서도 값이 갱신된다면 음수 사이클이 존재한다는 것.
                # 모든 간선에 대해 순환(N회)을 N번째 또 반복할 때도 값이 '갱신'되는 경우가 있다면 음수 사이클이 존재한다는 것.
                # 왜 N번이냐: 어떠한 한 간선에 대해, 그 간선에 인접해 존재할 수 있는 간선은 N-1개이기 때문.
                # 어떠한 한 간선이 있을 때, 이 간선에 인접하여 존재할 수 있는 간선의 최대 개수(N-1)을 넘어서, 또 이 간선에 대해 값이 '갱신'된다면 음수 사이클이 존재한다는 것.
                if i == N:
                    return True
    return False

if bellman_ford(1):
    print(-1)
else:
    for i in range(2, N + 1):
        print(-1 if dist[i] == INF else dist[i])