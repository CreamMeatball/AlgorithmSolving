import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

input_ = sys.stdin.readline

N, M = map(int, input_().rstrip().split())

map_ = [[9] * (M + 2)]
init_virus_pos = []
init_safe_pos = []
init_safe_count = 0
max_safe_count = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(1, N + 1):
    line = [9] + list(map(int, input_().rstrip().split())) + [9]
    for j, l in enumerate(line):
        if l == 2:
            init_virus_pos.append((i, j))
        if l == 0:
            init_safe_pos.append((i, j))
            init_safe_count += 1
    map_.append(line)
    
map_.append([9] * (M + 2))

# print("init map")
# for m in map_:
#     print(*m)

new_wall = list(combinations(init_safe_pos, 3))
# print(new_wall)

for nw in new_wall:
    new_map = deepcopy(map_)
    virus_pos = deepcopy(init_virus_pos)
    safe_count = init_safe_count
    visited = [[False] * (M + 2) for _ in range(N + 2)]
    
    for w in nw:
        if new_map[w[0]][w[1]] == 0:
            new_map[w[0]][w[1]] = 1
            safe_count -= 1
        else:
            # print(f"impossible installing wall")
            break
    else:
        # print("show map after install wall")
        # for nm in new_map:
        #     print(*nm)
            
        dq = deque()
        dq.extend(virus_pos)
        # print("init virus pos:")
        # print(*dq)
        for vp in virus_pos:
            visited[vp[0]][vp[1]] = True
        
        while dq:
            current_row, current_col = dq.popleft()
            for d in directions:
                new_row = current_row + d[0]
                new_col = current_col + d[1]
                if new_map[new_row][new_col] == 0 and not visited[new_row][new_col]:
                    dq.append((new_row, new_col))
                    visited[new_row][new_col] = True
                    new_map[new_row][new_col] = 2
                    safe_count -= 1
        
        # print("show map after virus spreading out")
        # for nm in new_map:
        #     print(*nm)
        
        # print(f"safe count in this wall: {safe_count}")
        max_safe_count = max(max_safe_count, safe_count)
        
print(max_safe_count)