import sys

input_data = sys.stdin.readline
INF = 6000 * 10000  # 충분히 큰 값

N, M = map(int, input_data().split())
dist = [INF] * (N + 1)
edges = []
for _ in range(M):
    A, B, C = map(int, input_data().split())
    edges.append((A, B, C))

# 새로운 cost값이 기존 cost값보다 작은 경우에 append 하는 다익스트라로 풀 경우
# 음수 가중치가 있는 경우를 주의해야 함.
# 음수 가중치가 있다는 것 자체는 괜찮은데,
# 어떠한 사이클의 cost 총합이 음수가 되는 경우가 있을 경우
# cost가 무한히 낮아져서, 같은 사이클을 무한히 도는 문제가 발생함.

# 벨만-포드 알고리즘 사용
# 다익스트라보다 오래 걸리는 대신, 음수 사이클이 있는 경우를 판별 가능.
def bellman_ford(start):
    dist[start] = 0
    # N번의 라운드를 반복
    for i in range(1, N + 1):
        # 모든 간선을 확인하며 최단 거리 갱신
        for A, B, C in edges:
            if (dist[A] != INF) and (dist[A] + C < dist[B]):
                dist[B] = dist[A] + C
                # N번째 라운드에서도 값이 갱신된다면 음수 사이클 존재
                if i == N:
                    return True
    return False

if bellman_ford(1):
    print(-1)
else:
    for i in range(2, N + 1):
        print(-1 if dist[i] == INF else dist[i])