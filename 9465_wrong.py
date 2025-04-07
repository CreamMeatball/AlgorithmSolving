import sys
from collections import deque

input_data = sys.stdin.readline

T = int(input_data().rstrip())

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

directions2 = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

def bfs(start, numberOfStickers, scoreList): # start: like (1, 1)
    score = 0
    selectedStickers = 0
    visited = [[False] * (numberOfStickers // 2 + 2) for _ in range(4)]
    print(visited)
    newScoreList = []
    newScoreList.append([0] * (numberOfStickers // 2 + 2))
    for row in scoreList:
        newScoreList.append([0] + row + [0])
    newScoreList.append([0] * (numberOfStickers // 2 + 2))
    scoreList = newScoreList
    print(scoreList)
    queue = deque()
    queue.append(start)
    
    while queue:
        print(f"rest queue: {queue}")
        current = queue.popleft()
        current_x, current_y = current
        print(f"current: {current}")
        if visited[current_x][current_y]:
            continue
        score += scoreList[current_x][current_y]
        print(f"score added. score: {score}")
        selectedStickers += 1
        if selectedStickers == numberOfStickers // 2:
            return score
        visited[current_x][current_y] = True
        # print(f"visited: {visited}")

        for d in directions:
            new_x = current[0] + d[0]
            new_y = current[1] + d[1]
            visited[new_x][new_y] = True
        # print(f"visited: {visited}")

        for d in directions2:
            new_x = current[0] + d[0]
            new_y = current[1] + d[1]
            if visited[new_x][new_y]:
                continue
            if 1 <= new_x <= 2 and 1 <= new_y <= len(scoreList[0]) - 2:
                queue.append((new_x, new_y))
        
for _ in range(T):
    n = int(input_data().rstrip())
    scoreList = []
    scoreList.append(list(map(int, input_data().rstrip().split())))
    scoreList.append(list(map(int, input_data().rstrip().split())))
    
    max_score = 0
    
    for row in range(1, 3):
        for startpoint in range(1, n+1):
            start = (row, startpoint)
            # print(f"n: {n}, start: {start}")
            score = bfs(start, 2 * n, scoreList)
            print(f"return score: {score}")
            if score > max_score:
                max_score = score
                
    print(max_score)