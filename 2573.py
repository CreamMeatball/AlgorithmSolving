import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(start_r, start_c, visited):
    dq = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    count = 0
    will_melt = []

    while dq:
        r, c = dq.popleft()
        count += 1

        water = 0
        # 주변 바다 개수 집계
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0:
                water += 1
        will_melt.append((r, c, water))

        # 인접 얼음 확장
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] != 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    dq.append((nr, nc))

    return count, will_melt

# 초기 얼음 좌표 수집
ice = [(i, j) for i in range(N) for j in range(M) if board[i][j] != 0]

year = 0

while True:
    # 전부 녹았으면 분리 없이 종료
    # 아래 조건 분기(두 덩어리 이상)에 끝날 때까지 안 걸렸다는 뜻이니까
    # 문제에서 제시한 것처럼 0으로 결과 출력
    if not ice:
        print(0)
        break

    visited = [[False] * M for _ in range(N)]

    # 현재 얼음이 한 덩어리인지 확인: ice[0]에서만 BFS
    sr, sc = ice[0]
    comp_count, will_melt = bfs(sr, sc, visited)

    # 분리되었으면 (한 해 시작 시점에 이미 2덩어리 이상) 종료
    # 빙산이 분리되었음을 판단하는 게, 굳이 bfs 여러번 돌려서 빙산들을 모두 파악한 뒤 덩어리 개수 count해서 판단할 필요가 없고
    # 그냥 한 위치에서 bfs 한 번 돌렸을 때, count 된 얼음 개수가 전체 얼음 개수랑 다르면, 덩어리가 여러개 있다는 뜻으로 판단하면 됨.
    if comp_count != len(ice):
        print(year)
        break

    # 한 덩어리라면 이번 해 녹임 적용
    removed = set()
    for r, c, w in will_melt:
        if board[r][c] > 0:
            new_h = board[r][c] - w
            if new_h <= 0:
                board[r][c] = 0
                removed.add((r, c))
            else:
                board[r][c] = new_h

    # ice 리스트 갱신 (사라진 칸만 제거)
    if removed:
        ice = [pos for pos in ice if pos not in removed]

    year += 1
