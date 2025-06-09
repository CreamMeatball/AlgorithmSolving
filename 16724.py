import sys
from collections import deque

input_ = sys.stdin.readline

N, M = map(int, input_().rstrip().split())

map_ = []
for _ in range(N):
    map_.append(list(str(input_().rstrip())))
    
# 사이클이 발생하면 +1개
# 로 하면 될 듯.
# dfs로 해서 사이클이 발생할 경우 +1개로 하면
# 위치는 정확히 똑같진 않지만, 개수는 맞을 듯.

# !!!정확히 말하면!!!
# '현재'의 dfs 내에서 사이클이 발생할 경우 +1개
# 이전에 탐색했던 dfs 경로를 부딪칠 경우엔 +1개를 하지 않고 탐색 종료.
# = 이전에 탐색했던 루트에 종속됨(사이클 X)
    
visited = [[0] * M for _ in range(N)]
directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)} # 행, 열
cycle = 0
    
def dfs(map_, start_point):
    cycle = 0
    dq = deque()
    route = [] # 현재 dfs에서의 경로 기록용
    dq.append(start_point)
    
    while dq:
        current_row, current_col = dq.pop()
        if visited[current_row][current_col] == 0:
            route.append((current_row, current_col))
            direct = directions[map_[current_row][current_col]]
            next_row, next_col = current_row + direct[0], current_col + direct[1]
            dq.append((next_row, next_col))
            visited[current_row][current_col] = 1
            # print("current visited")
            # for v in visited:
            #     print(v)
        elif visited[current_row][current_col] == 1:
            cycle += 1
        elif visited[current_row][current_col] == 2:
            break
            
    for row, col in route:
        visited[row][col] = 2
        
    # print("total visited")
    # for v in visited:
    #     print(v)
            
    return cycle
        
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            # print(f"new dfs[{i}][{j}]")
            start_point = (i, j)
            cycle += dfs(map_, start_point)

print(cycle)