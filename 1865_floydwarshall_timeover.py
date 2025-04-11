import sys

input_data = sys.stdin.readline
TC = int(input_data().rstrip())

# 벨만-포드 알고리즘 말고
# 플로이드 워셜에서도 음수 사이클이 존재하는지 확인만 한다면
# 문제가 풀리지 않을까 하여 시도.

# PyPy3 로 제출했는데
# 실제로 답은 맞는 것 같으나
# 67% 정도까지 진행되다 시간 초과 남.

def floyd_warshall_negative_cycle(n, graph):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] != float('inf') and graph[k][j] != float('inf'):
                    if graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
                        # 음수 사이클 판별
                        # 만약 i와 j가 같은데(자기 자신으로 돌아오는 경로) 비용이 음수라면
                        # 음수 사이클이 존재
                        if i == j and graph[i][j] < 0:
                            return True
    
    return False

for _ in range(TC):
    N, M, W = map(int, input_data().rstrip().split())
    INF = float('inf')
    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        graph[i][i] = 0
    
    for _ in range(M):
        S, E, T = map(int, input_data().rstrip().split())
        graph[S][E] = min(graph[S][E], T)
        graph[E][S] = min(graph[E][S], T)
    
    for _ in range(W):
        S, E, T = map(int, input_data().rstrip().split())
        graph[S][E] = min(graph[S][E], -T)
    
    # 음수 사이클 판별
    if floyd_warshall_negative_cycle(N, graph):
        print("YES")
    else:
        print("NO")