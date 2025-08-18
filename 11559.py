from collections import deque

board = [list(map(str, input())) for _ in range(12)]

R, C = 12, 6
directions = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(r, c, visited):
    color = board[r][c]
    q = deque([(r, c)])
    group = [(r, c)]
    visited[r][c] = True

    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and board[nr][nc] == color:
                # 같은 색이면 그룹에 추가
                visited[nr][nc] = True
                q.append((nr, nc))
                group.append((nr, nc))
    return group

def apply_gravity():
    # 각 열마다 아래로 떨어뜨리기
    for c in range(C):
        write = R - 1
        for r in range(R - 1, -1, -1): # 아래쪽에 쌓여있을테니 아래쪽부터 탐색.
            if board[r][c] != '.':
                board[write][c] = board[r][c] # 가능한 최대의 아래로 내리기.
                write -= 1
        # 남은 위 칸들은 빈칸으로 채우기 (기존 뿌요 잔상 지우기)
        for r in range(write, -1, -1):
            board[r][c] = '.'

chain = 0

while True:
    # 매번 터질 거 있나 새로 찾기
    visited = [[False] * C for _ in range(R)]
    to_pop = []  # 터질 좌표들 모으기

    for r in range(R):
        for c in range(C):
            if board[r][c] != '.' and not visited[r][c]:
                group = bfs(r, c, visited)
                if len(group) >= 4:
                    to_pop.extend(group)

    if not to_pop:
        break  # 더 이상 터질 게 없으면 종료

    # 동시에 터뜨리기 (문제에서 여러 그룹이 한 번에 터지는 경우 한 번의 연쇄로 침)
    for r, c in to_pop:
        board[r][c] = '.'

    # 중력 적용
    apply_gravity()

    chain += 1

print(chain)