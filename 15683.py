import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

room = []
cctv_list = []
wall_pos = []
total_zero = 0

for i in range(N):
    line = list(map(int, input().split()))
    room.append(line)
    for j, val in enumerate(line):
        if val == 0:
            total_zero += 1
        elif val == 6:
            wall_pos.append((i, j))
        else:
            cctv_list.append((val, (i, j)))

CCTV_DIRECTIONS = {
    1: [[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)]],
    2: [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]],
    3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)],
        [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
    4: [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)],
        [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
    5: [[(-1, 0), (1, 0), (0, -1), (0, 1)]]
}
def calculateSee(start, direction):
    """start 위치에서 direction 으로 진행하며 볼 수 있는 (0)칸 좌표 집합 반환"""
    r, c = start
    dr, dc = direction
    seen = set()
    while True:
        r += dr
        c += dc

        if not (0 <= r < N and 0 <= c < M) or room[r][c] == 6:
            break

        if 1 <= room[r][c] <= 5:
            continue

        seen.add((r, c))
    return seen

if not cctv_list:
    print(total_zero)
    sys.exit(0)

coverage_options = []

for typ, (r, c) in cctv_list:
    each = []
    for direction in CCTV_DIRECTIONS[typ]:
        watch = set()
        for d in direction:
            watch |= calculateSee((r, c), d) # union set | set
        each.append(watch)
    coverage_options.append(each)

min_blind = total_zero

def dfs(idx, watched):
    global min_blind
    
    if min_blind == 0:
        return

    if idx == len(cctv_list):
        blind = total_zero - len(watched)
        min_blind = min(min_blind, blind)
        return

    for cov in coverage_options[idx]:
        dfs(idx + 1, watched | cov) # 파라미터에다가 CCTV로 본 영역을 합치기
        # 일반적인 방식이면 재귀 호출 이후에 backtracking을 위한 별도 처리를 해줘야 되는데, 이렇게 하면 안 해도 됨. 파라미터 상에 그 때의 state가 저장돼있는 거라.

dfs(0, set()) # 확인한 영역들 합을 파라미터에다 저장함. 백트래킹 하기 용이.

print(min_blind)

# 일반적인 방식 ⬇
# # 1) 전역 감시 집합
# watched = set() # 현재까지 감시된 칸을 in-place(한 위치, 제자리에서)로 관리
# min_blind = total_zero

# def dfs(idx):
#     global min_blind

#     # 가지치기
#     if min_blind == 0:
#         return

#     # 모든 CCTV에 대해 방향을 고르면
#     if idx == len(cctv_list):
#         blind = total_zero - len(watched)
#         if blind < min_blind:
#             min_blind = blind
#         return

#     # 3) 이번 CCTV의 모든 회전 경우 시도
#     for cov in coverage_options[idx]:
#         # (1) 이번 회전으로 새로 추가된 칸만 기록
#         newly_added = []
#         for pos in cov:
#             if pos not in watched: # 이미 본 칸은 다시 넣을 필요 없음
#                 watched.add(pos)
#                 newly_added.append(pos) # 이번 탐색으로 인해 추가되는 애

#         dfs(idx + 1) # (2) 재귀 호출

#         # (3) 백트래킹 : 새로 넣었던 칸만 원상 복구
#         for pos in newly_added:
#             watched.remove(pos)

# # 4) 탐색 시작
# dfs(0)