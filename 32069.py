import sys
from collections import deque

input = sys.stdin.readline

L, N, K = map(int, input().split())
As = list(map(int, input().split()))

dq = deque()
visited = set()

# 문제 18513 랑 구조가 같고 보는 관점만 다름 (컨셉만 다름)

for a in As:
    dq.append((a, 0))
    visited.add(a)

ans = []
while len(ans) < K:
    current, d = dq.popleft()
    ans.append(d)

    if current - 1 >= 0 and (current - 1) not in visited:
        visited.add(current - 1)
        dq.append((current - 1, d + 1))
    
    if current + 1 <= L and (current + 1) not in visited:
        visited.add(current + 1)
        dq.append((current + 1, d + 1))

print(*ans, sep='\n')


# 18513: 샘터들이 있고, 집을 지어야 함. 집에서 가장 가까운 샘터까지의 거리가 그 집의 거리값. 거리값이 가장 짧게 되는 집들의 거리값들의 합을 구하라.

# 집들이 설치될 수 있는 여러 경우의 수를
# 탐색하면서 다 비교한 뒤
# 그 중 최적인 걸 찾자..
# 이렇게 처음 생각했는데

# 엄청 걍 간단한 방식이 있었음.    

# 모든 샘터에서, 양옆 위치에 집을 짓는다.
# 짓고나면, 한 칸 더 벌어진 위치에서 집을 짓는다 (이 때, 이미 집이 지어져있다면 스킵)
# 그래서 총 K개 지으면 멈춘다.
# K개 짓는 동안 누적된 거리(불행도)를 더한다.

# 왜냐면 무조건 그냥 샘터 가까이 지으면
# 그게 그냥 최소임.