import sys
from collections import deque

input_data = sys.stdin.readline

N, M = map(int, input_data().split())

testPrint = False

map_data = []
map_data.append([2] * (M + 2))
for _ in range(N):
    map_data.append([2] + list(map(int, input_data().strip())) + [2])
map_data.append([2] * (M + 2))

if testPrint:
    print("map_data:")
    for row in map_data:
        print(row)

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 기존의 visited와 count 옆에 값(벽 부수기 기회)을 더 붙여서,
# 벽을 부순 경우의 visited / 아닌 경우의 visited. 이렇게 두 가지 경우를 나누어서 존재하게 하는 게 핵심.
# 별도로 breaking_change 변수를 설정해서 사용하면, 후에 bfs 반복문에서 최적의 경로를 타지 않은 queue의 경우가 breaking_change를 덮어씌워서
# 이후의 최적의 경로를 타려는 queue의 breaking_change를 잘못 전달받아서 사용하는 경우가 발생함.
visited = [[[False, False] for _ in range(M + 2)] for _ in range(N + 2)]
count = [[[0, 0] for _ in range(M + 2)] for _ in range(N + 2)]

visited[1][1][1] = True
count[1][1][1] = 1

def showCurrentMove():
    global visited, count
    print("---")
    print("visited (형태: chance1/chance0):")
    for i in range(1, N + 1):
        row = []
        for j in range(1, M + 1):
            state = f"{'o' if visited[i][j][1] else 'x'}/{'o' if visited[i][j][0] else 'x'}"
            row.append(state)
        print(' '.join(row))
    print("count (형태: chance1/chance0):")
    for i in range(1, N + 1):
        row = []
        for j in range(1, M + 1):
            state = f"{count[i][j][1]}/{count[i][j][0]}"
            row.append(state)
        print(' '.join(row))
    print('---')

def bfs(current, direction):
    global visited, count
    current_row, current_col, current_chance = current
    # .pop() 이 O(n)의 시간복잡도를 가지므로, deque 및 .popleft()를 사용해서 O(1) 시간에 처리할 수 있도록 함.
    # 안 그러면 시간 초과 남.
    queue = deque()
    queue.append((current_row, current_col, current_chance))
    
    if testPrint:
        showCurrentMove()
    
    while queue:
        current_row, current_col, current_chance = queue.popleft()
        
        if current_row == N and current_col == M:
            print(count[current_row][current_col][current_chance])
            return
        
        for dx, dy in direction:
            next_row = current_row + dx
            next_col = current_col + dy
            
            if map_data[next_row][next_col] == 0:
                if not visited[next_row][next_col][current_chance]:
                    visited[next_row][next_col][current_chance] = True
                    count[next_row][next_col][current_chance] = count[current_row][current_col][current_chance] + 1
                    queue.append((next_row, next_col, current_chance))
                    
            elif map_data[next_row][next_col] == 1 and current_chance == 1:
                if not visited[next_row][next_col][0]:
                    visited[next_row][next_col][0] = True
                    count[next_row][next_col][0] = count[current_row][current_col][current_chance] + 1
                    queue.append((next_row, next_col, 0))
                    
            if testPrint:
                print(f"queue: {queue}")
                
        if testPrint:
            showCurrentMove()
    print(-1)

bfs((1, 1, 1), direction)