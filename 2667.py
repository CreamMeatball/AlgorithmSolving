import sys

input_data = sys.stdin.readline

testPrint = False

N = int(input_data())
housemap = [[-1] * (N + 2) for _ in range(N + 2)]
for i in range(N):
    temp = list(str(input_data().rstrip()))
    housemap[i + 1][1:-1] = temp
    
for row in housemap:
    print("\t".join(map(str, row))) if testPrint else None
print(f"shape of housemap: {len(housemap)} x {len(housemap[0])}") if testPrint else None

apt_complex_list = []
apt_complex_count = 0
visited = [[False] * (N + 2) for _ in range(N + 2)]

def searchNear(row, col, graph):
    global visited
    print(f"receive index row: {row}, col: {col}") if testPrint else None
    if (not visited[row][col]) and (graph[row][col] == "1"):
        return True

def bfs(graph, current_node_row, current_node_col):
    global visited, apt_complex_list, apt_complex_count
    queue = [(current_node_row, current_node_col)]
    visited[current_node_row][current_node_col] = True
    apt_complex_count += 1
    while queue:
        print(f"current_node_row: {current_node_row}, current_node_col: {current_node_col}") if testPrint else None
        current_node_row, current_node_col = queue.pop(0)
        up = [current_node_row - 1, current_node_col]
        down = [current_node_row + 1, current_node_col]
        left = [current_node_row, current_node_col - 1]
        right = [current_node_row, current_node_col + 1]
        position = [up, right, down, left] # clockwise
        for p in position:
            if searchNear(p[0], p[1], housemap):
                queue.append((p[0], p[1]))
                print(f"found house nearby. current queue: {queue}") if testPrint else None
                visited[p[0]][p[1]] = True
                apt_complex_count += 1
            else:
                continue
    apt_complex_list.append(apt_complex_count)
    apt_complex_count = 0
    print(f"queue ended. move into the next apt_complex. apt_complex_list: {apt_complex_list}") if testPrint else None
            
for i in range(1, N + 2):
    for j in range(1, N + 2):
        if (not visited[i][j]) and (housemap[i][j] == "1"):
            bfs(housemap, i, j)

apt_complex_list.sort()
print(len(apt_complex_list))
print('\n'.join(map(str, apt_complex_list)))