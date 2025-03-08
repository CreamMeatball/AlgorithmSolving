import sys

input_data = sys.stdin.readline

R, C, K = map(int, input_data().split())
roadMap = [list(0 for _ in range(C + 2))]
for _ in range(R):
    roadMap.append([0] + list(input_data().rstrip()) + [0])
roadMap.append(list(0 for _ in range(C + 2)))

visited = [[False for _ in range(C + 2)] for _ in range(R+2)]

count = 0
startPoint = (R, 1)
endPoint = (1, C)

distance = 1

def dfs(x, y):
    visited[x][y] = True
    global distance, count
    # # print(f"({x}, {y})")
    # for i in visited:
    #     print(i)
    if (x, y) == endPoint:
        if distance == K:
            count += 1
            # print(f"success. count: {count}")
        visited[x][y] = False  # 도착점에서도 backtracking 수행
        return
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 < nx <= R and 0 < ny <= C and not visited[nx][ny] and roadMap[nx][ny] != 'T':
            distance += 1
            # print(f"distance: {distance}")
            dfs(nx, ny)
            distance -= 1
    visited[x][y] = False
    
dfs(*startPoint)
print(count)
