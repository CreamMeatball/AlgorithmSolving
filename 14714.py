from collections import deque

N, A, B, DA, DB = map(int, input().split())

# 1-based → 0-based
A -= 1
B -= 1

# visited[a][b][turn]
visited = [[[False]*2 for _ in range(N)] for __ in range(N)]

q = deque()
q.append((A, B, 0, 0))  # (A_pos, B_pos, turn, moves)
visited[A][B][0] = True

end = False
result = "Evil Galazy"

while q and not end:
    a, b, turn, moves = q.popleft()

    if turn == 0:  # A 차례
        for d in (-DA, DA):
            na = (a + d) % N
            # 종료 조건
            if na == b:
                result = moves + 1
                end = True
                break
            if not visited[na][b][1]:
                visited[na][b][1] = True
                q.append((na, b, 1, moves + 1))

    else:  # B 차례
        for d in (-DB, DB):
            nb = (b + d) % N
            # 종료 조건
            if nb == a:
                result = moves + 1
                end = True
                break
            if not visited[a][nb][0]:
                visited[a][nb][0] = True
                q.append((a, nb, 0, moves + 1))

print(result)
