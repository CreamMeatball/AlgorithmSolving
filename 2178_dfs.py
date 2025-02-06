import sys
sys.setrecursionlimit(10**4) # 재귀 제한 늘리기. BOJ에서 기본값이 1000으로 되어있음.

testPrint = False

input_data = sys.stdin.readline
N, M = map(int, input_data().rstrip().split()) # N : 행, M : 열

maze = [[-1] * (M + 2) for _ in range(N + 2)]
for i in range(N):
    maze[i + 1][1:-1] = list(map(int, input_data().rstrip()))

def dfs(graph, current_node, visited, count = 0):
    global min_count
    current_node_row = current_node[0]
    current_node_col = current_node[1]
    visited[current_node_row][current_node_col] = True
    count += 1
    print(f"[start dfs] current_node_row: {current_node_row}, current_node_col: {current_node_col}, count: {count}") if testPrint else None
    
    if current_node_row == N and current_node_col == M:
        print(f"\n ★ reached the end. count: {count} \n") if testPrint else None
        print(f"current position row: {current_node_row}, col: {current_node_col}. \n current visited(after visit destination): ") if testPrint else None
        for row in visited:
            print(''.join(['v' if cell else '.' for cell in row])) if testPrint else None
        if count < min_count:
            print(f"\n ✪ min count update. count: {count} \n") if testPrint else None
            min_count = count
            visited[current_node_row][current_node_col] = False # 처리 무조건 해줘야됨
        return
    
    up = [current_node_row - 1, current_node_col]
    down = [current_node_row + 1, current_node_col]
    left = [current_node_row, current_node_col - 1]
    right = [current_node_row, current_node_col + 1]
    position = [up, right, down, left] # clockwise
    
    print(f"[start searching near] will search the position: {position}") if testPrint else None

    for p in position:
        print(f"p: {p}. position: {position}") if testPrint else None
        if (not visited[p[0]][p[1]]) and (graph[p[0]][p[1]] == 1):
            print(f"will visit the available near. {p}. current position row: {current_node_row}, col: {current_node_col}") if testPrint else None
            print(f"current position row: {current_node_row}, col: {current_node_col}. \n current visited(before visit available near): ") if testPrint else None
            for row in visited:
                print(''.join(['v' if cell else '.' for cell in row])) if testPrint else None
            dfs(graph, p, visited, count)
            print("back to the previous node") if testPrint else None
        else:
            continue
    visited[current_node_row][current_node_col] = False # 처리 무조건 해줘야됨

# !중요!
# 이전 재귀 단계로 되돌아갈 때,
# visited는 mutable 객체이므로 (mutable : list, set, dictionary ...)
# 이전 재귀 단계로 돌아갔음에도, visited 상태는 되돌아가지 않음.
# 반면에 count는 immutable 객체이므로 (immutable : int, float, str, tuple, bool ...)
# 이전 재귀 단계로 되돌아갔을 때, count 상태는 되돌아감.
# 그렇기 때문에 이전 재귀로 돌아갈 때 visited 상태도 되돌아가야 하는 상황이므로,
# visited[row][col] = False 처리를 별도로 해줘야 함.

visited = [[False] * (M + 2) for _ in range(N + 2)]
min_count = 10001

dfs(maze, [1, 1], visited, 0)
print(min_count)