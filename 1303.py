import sys
from collections import deque

input_data = sys.stdin.readline

N, M = map(int, input_data().rstrip().split())

soldiers = []
soldiers.append(["N"] * (N + 2))
for _ in range(M):
    soldiers.append(["N"] + list(input_data().rstrip()) + ["N"])
soldiers.append(["N"] * (N + 2))
    
visited = [[False] * (N + 2) for _ in range(M + 2)]

def bfs(soldiers, visited, start, team):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    count = 1
    
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    while queue:
        current_row, current_col = queue.popleft() # pop() 아님
        
        for d in directions:
            next_row, next_col = current_row + d[0], current_col + d[1]
            if (1 <= next_row <= M) and (1 <= next_col <= N) and not visited[next_row][next_col] and soldiers[next_row][next_col] == team:
                visited[next_row][next_col] = True
                count += 1
                queue.append((next_row, next_col))
                
    return count ** 2
        
powers = {"W": 0, "B": 0}
        
for row in range(1, M + 1):
    for col in range(1, N + 1):
        if not visited[row][col] and soldiers[row][col] in ["W", "B"]:
            team = soldiers[row][col]
            power = bfs(soldiers, visited, (row, col), team)
            powers[team] += power
            
print(powers["W"], powers["B"])