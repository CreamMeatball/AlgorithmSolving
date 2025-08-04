import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

room = []
cctv_pos = defaultdict(list)
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
            cctv_pos[val].append((i, j))

CCTV_DIRECTIONS = {
    1: [[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)]],
    2: [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]],
    3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)],
        [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
    4: [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)],
        [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
    5: [[(-1, 0), (1, 0), (0, -1), (0, 1)]]
}
def calculateSee(start: tuple[int, int], direction: tuple[int, int]) -> set[tuple[int, int]]:
    """start 위치에서 direction 으로 진행하며 볼 수 있는 (0)칸 좌표 집합 반환"""
    y, x = start
    dy, dx = direction
    seen = set()
    while True:
        y += dy
        x += dx
        # 경계 또는 벽(6) 만나면 종료
        if not (0 <= y < N and 0 <= x < M) or room[y][x] == 6:
            break
        # CCTV는 통과만 하고 시야에 포함시키지 않는다
        if 1 <= room[y][x] <= 5:
            continue
        # 빈 칸이면 시야에 포함
        seen.add((y, x))
    return seen

cctv_list = []
for typ in range(1, 6):
    cctv_list.extend([(typ, pos) for pos in cctv_pos[typ]])

if not cctv_list:
    print(total_zero)
    sys.exit(0)

coverage_options = []

for typ, (y, x) in cctv_list:
    each = []
    for dirs in CCTV_DIRECTIONS[typ]:
        watch = set()
        for d in dirs:
            watch |= calculateSee((y, x), d) 
        each.append(watch)
    coverage_options.append(each)

min_blind = total_zero

def dfs(idx: int, watched: set[tuple[int, int]]):
    global min_blind
    
    if min_blind == 0:
        return

    if idx == len(cctv_list):
        blind = total_zero - len(watched)
        if blind < min_blind:
            min_blind = blind
        return

    for cov in coverage_options[idx]:

        dfs(idx + 1, watched | cov)

dfs(0, set())

print(min_blind)
