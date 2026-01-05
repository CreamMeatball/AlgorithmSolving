import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# 플로이드-워셜 (모든 노드로부터 모든 노드까지에 대한 모든 거리 계산)
# N = 100이라 O(N^3)이지만 시간 초과 안 날 듯
INF = float('inf')
dist = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dist[i][i] = 0

for _ in range(M):
    A, B = map(int, input().rstrip().split())
    dist[A][B] = 1
    dist[B][A] = 1

# 플로이드-워셜 (모든 노드로부터 모든 노드에 대한 거리 계산)
for k in range(1, N + 1): # k: 경유지
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

min_sum = INF
ans_node1 = 0
ans_node2 = 0

# 2개의 건물을 선택하는 모든 조합 탐색
for i in range(1, N): # 첫 가게
    for j in range(i + 1, N + 1): # 두 번째 가게
        current_sum = 0
        # 모든 건물에서의 접근성 합 계산
        for k in range(1, N + 1): # 모든 가게 외 노드에 대해, 가까운 가게까지의 거리를 누적 합.
            # k번 건물에서 i번 혹은 j번 건물 중 더 가까운 곳으로 왕복
            current_sum += min(dist[k][i], dist[k][j]) * 2
        
        if current_sum < min_sum:
            min_sum = current_sum
            ans_node1 = i
            ans_node2 = j

print(ans_node1, ans_node2, min_sum)

# 두 가게 위치를 구할 때,
# 개별적으로 가장 좋은 곳 찾는 Greedy한 방식으로
# 다른 모든 노드로부터 거리 총합이 가장 낮은 두 위치를 지점으로 삼으면 되는 거 아님?
# -> 안됨.

# because (by AI)
# 상상해 보세요. 도시가 크게 강남과 강북 두 덩어리로 나뉘어 있고, 그 사이를 잇는 다리가 하나뿐이라고 가정해 봅시다.

# 개별적으로 가장 좋은 곳 찾기 (제안하신 방식)
# 1등: 도시 전체의 정중앙(다리 근처)이 모든 사람에게 평균적으로 가장 가깝습니다.
# 2등: 1등 바로 옆 건물이 두 번째로 가깝습니다.
# 결과: 두 건물을 다리 근처에 나란히 짓게 됩니다. 강남 깊숙한 곳이나 강북 깊숙한 곳에 사는 사람들은 여전히 멉니다.

# 조합으로 가장 좋은 곳 찾기 (현재 코드 방식)
# 하나는 강남의 중심, 다른 하나는 강북의 중심에 짓습니다.
# 강남 사람은 강남 가게로, 강북 사람은 강북 가게로 갑니다.
# 결과: 전체 이동 거리가 획기적으로 줄어듭니다.