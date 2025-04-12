import sys

input_data = sys.stdin.readline

TC = int(input_data().rstrip())

# floyd-warshall 쓰니까 오답임.
# floyd-warshall이 음수 가중치가 있는 경우도 다룰 수 있는 건 맞는데
# 음수 사이클이 발생하는 경우엔 정확한 결과를 보장하지 않는다고 함.

# 생각해보면, 출발지로 돌아왔을 때 시간이 마이너스가 된다는 건,
# 지났던 경로들 내의 양수 가중치들의 총합보다, 음수 가중치들의 총합이 더 크다는 건데,
# 이건 곧 '음수 사이클'이 발생한다는 거랑 같은 의미임.
# 어딘가를 찍고 다시 출발지로 돌아왔을 때 가중치 총합이 음수라면
# 그건 곧 또 어딘가로 계속해서 경로를 더 확장할 수 있다는 의미이고
# 이는 곧 '음수 사이클'의 정의랑 똑같음.
# * 음수 사이클: 사이클 내에 있는 간선의 가중치 합이 음수인 사이클.
# 그래서 임의의 출발지부터 임의의 도착지까지의 총 시간을 구하고
# 다시 도착지로부터 출발지까지의 총 시간을 또 구해서 더해줄 필요가 없음
# 그냥 음수 사이클이 발생하는지 아닌지만 판별하면 됨.
# * 음수 가중치 경로가 단방향이어도 성립.

def bellman_ford(n, graph):
    # bellman_ford가 dijkstra와 다른 점은
    # heapq를 사용하지 않아 가능한 모든 경로에 대해 다 탐색한다는 거임.
    # 그래서 당장 이후의 경로가 가중치가 더 클 경우 스킵해버리는 dijkstra와 달리
    # 음수 가중치가 있는 경우도 다룰 수 있음.
    # 음수 사이클이 있는 경우도 판별 가능.
    distance = [0] * (n + 1)
    
    for i in range(n):
        for start, end, time in graph:
            if distance[end] > distance[start] + time:
                distance[end] = distance[start] + time
                # 음수 사이클 판별
                if i == n - 1:
                    return True
    return False

for _ in range(TC):
    N, M, W = map(int, input_data().rstrip().split())
    
    graph = []
    for _ in range(M):
        S, E, T = map(int, input_data().rstrip().split())
        graph.append((S, E, T))
        graph.append((E, S, T))
    
    for _ in range(W):
        S, E, T = map(int, input_data().rstrip().split())
        graph.append((S, E, -T))
    
    # 음수 사이클이 있으면 YES, 없으면 NO
    if bellman_ford(N, graph):
        print("YES")
    else:
        print("NO")