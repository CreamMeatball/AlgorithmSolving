N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]

min = 100 * 20 ** 20

visited = [False] * N

def dfs(depth, idx, visited):
    global min
    if depth == N // 2:
        # print("visited : ", visited)
        team1 = 0
        team2 = 0
        for i in range(N):
            for j in range(N):
                if (i != j) and (visited[i] and visited[j]):
                    team1 += ability[i][j]
                elif(i != j) and (not visited[i] and not visited[j]):
                    team2 += ability[i][j]
        # print("team1 : ", team1)
        # print("team2 : ", team2)
        difference = abs(team1 - team2)
        # print("difference : ", difference)
        if difference < min:
            min = difference
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1, visited)
            visited[i] = False
            
dfs(0, 0, visited)
print(min)