# PyPy3 (to avoid time exceed)

import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().rstrip().split())

board = []

for _ in range(R):
    # data = str(input().rstrip())
    # board.append(list(str(d) for d in data))
    board.append(list(input().rstrip()))
    
# print(board)
    
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 어떠한 출발점 S에서 BFS를 통해 임의의 도착점에 대한 거리를 계산하고,
# 이를 모든 가능한 출발점 S에 대해 반복하는 방식일 때 (brute force)
# 시간 복잡도:
# 한 번 BFS: O(R*C)
# 임의의 출발점 개수: R*C
# 총 시간 복잡도: O((R*C)^2) = 2500^2 = 6,250,000
# 보통 시간 제한 1초에서 시간 복잡도 한계: O(1억)
# -> 가능할 것으로 예상됨.

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_overall_dist = 0

for r in range(R):
    for c in range(C):
        if board[r][c] == 'L':
            distance = [[-1] * C for _ in range(R)]
            dq = deque()

            dq.append((r, c))
            distance[r][c] = 0
            
            current_max_dist = 0
            current_max_pos = (r, c)

            while dq:
                current_r, current_c = dq.popleft()

                for dr, dc in directions:
                    nr, nc = current_r + dr, current_c + dc

                    if (0 <= nr < R) and (0 <= nc < C) and board[nr][nc] == 'L' and distance[nr][nc] == -1:
                        distance[nr][nc] = distance[current_r][current_c] + 1
                        current_max_dist = max(current_max_dist, distance[nr][nc])
                        dq.append((nr, nc))
            
            max_overall_dist = max(max_overall_dist, current_max_dist)

print(max_overall_dist)

# 주의점
# "출발점 A에서 가장 먼 지점이 B인 것을 찾았다면, B를 출발점으로 하는 탐색은 건너뛰어도 된다."
# "왜냐면 대칭적일 것이기 때문."
# 는 틀림. 따라서 이를 이용한 최적화 불가.
#
# 반례:
# (A B C D)
# (  E    )
# (  F    )
# (  G    )
#
# A에서 탐색 시, G가 가장 먼 곳이지만,
# G에서 탐색 시, D가 가장 먼 곳임.