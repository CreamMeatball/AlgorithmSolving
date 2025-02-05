import sys

input_data = sys.stdin.readline

testPrint = True

T = int(input_data().rstrip())

# visited = []
# count = 0
# 함수 안에서, 변수 선언보다 먼저 global 변수 선언을 하였지만
# 함수가 호출되는 scope가 변수 선언 이후이기 때문에,
# 위 visited 와 count 변수를 먼저 선언해놓지 않아도 오류가 나지 않음.
# 정확히 말하면 위 visited, count 를 적어봤자, 아래 함수 호출 직전 선언되는 변수에 의해 묻힘.

def searchNear(row, col, graph):
    global visited
    if (not visited[row][col]) and (graph[row][col] == 1):
        return True

def bfs(farm, current_node):
    global visited, count
    queue = [current_node]
    if (farm[current_node[0]][current_node[1]] == 1) and (visited[current_node[0]][current_node[1]] == False):
        visited[current_node[0]][current_node[1]] = True
    while queue:
        current_node = queue.pop(0)
        up = [current_node[0] - 1, current_node[1]]
        down = [current_node[0] + 1, current_node[1]]
        left = [current_node[0], current_node[1] - 1]
        right = [current_node[0], current_node[1] + 1]
        position = [up, right, down, left] # clockwise
        for p in position:
            if searchNear(p[0], p[1], farm):
                queue.append((p[0], p[1]))
                visited[p[0]][p[1]] = True
            else:
                continue
    count += 1
        
for _ in range(T):
    M, N, K = map(int, input_data().rstrip().split()) # M: 열(가로(), N: 행(세로), K: 배추의 개수

    farm = [[0] * (M + 2) for _ in range(N + 2)]
    
    visited = [[False] * (M + 2) for _ in range(N + 2)]
    count = 0

    for _ in range(K):
        X, Y = map(int, input_data().rstrip().split())
        farm[Y + 1][X + 1] = 1
        
    for i in range(1, N + 2):
        for j in range(1, M + 2):
            if (farm[i][j] == 1) and (not visited[i][j]):
                bfs(farm, [i, j])
    
    print(count)