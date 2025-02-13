import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())

testPrint = True

map_data = []
map_data.append([2] * (M + 2))
for _ in range(N):
    map_data.append([2] + list(map(int, input_data().split() + [2])))
map_data.append([2] * (M + 2))

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
breaking_chance = 1

visited = [[False] * (M + 2) for _ in range(N + 2)]
count = [[0] * (M + 2) for _ in range(N + 2)]

def showCurrentMove(current, visited, count):
    print(f"current: {current}")
    print(f"visited: ")
    for i in range(1, N + 1):
        row = [('o' if visited[i][v] else 'x') for v in range(1, M + 1)]
        print(' '.join(row))

def bfs(current, direction, breaking_chance):
    global visited
    current_x = current[0]
    current_y = current[1]
    queue = [(current_x, current_y)]
    visited[current_x][current_y] = True
    
    showCurrentMove(current, visited, count) if testPrint else None
    
    while queue:
        current = queue.pop(0)
        current_x = current[0]
        current_y = current[1]
        
        for dx, dy in direction:
            next_x = current_x + dx
            next_y = current_y + dy
            
            if map_data[next_x][next_y] == 0 and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                count[next_x][next_y] = count[current_x][current_y] + 1
                queue.append((next_x, next_y))
                
            elif map_data[next_x][next_y] == 1 and breaking_chance > 0:
                visited[next_x][next_y] = True
                count[next_x][next_y] = count[current_x][current_y] + 1
                queue.append((next_x, next_y))
                breaking_chance -= 1
                
            showCurrentMove(current, visited, count) if testPrint else None

bfs((1, 1), direction, breaking_chance)
print(count[N][M])
            
        