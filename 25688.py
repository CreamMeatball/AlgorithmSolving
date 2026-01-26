from collections import deque

board = [list(map(int, input().split())) for _ in range(5)]
sr, sc = map(int, input().split())

FULL = (True, True, True, True, True, True)

visited = [[set() for _ in range(5)] for _ in range(5)]

# 초기 방문 상태 (1~6)
start_state = (False, False, False, False, False, False)

q = deque()
q.append((sr, sc, start_state, 0))
visited[sr][sc].add(start_state)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = -1

while q:
    r, c, state, dist = q.popleft()

    if state == FULL:
        result = dist
        break

    for dr, dc in directions:
        nr, nc = r + dr, c + dc

        if 0 <= nr < 5 and 0 <= nc < 5:
            if board[nr][nc] == -1:
                continue

            new_state = list(state)
            if 1 <= board[nr][nc] <= 6:
                new_state[board[nr][nc] - 1] = True
            new_state = tuple(new_state)

            if new_state not in visited[nr][nc]:
                visited[nr][nc].add(new_state)
                q.append((nr, nc, new_state, dist + 1))

print(result)
