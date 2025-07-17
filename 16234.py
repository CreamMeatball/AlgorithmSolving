# PyPy3

import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().rstrip().split())
As = []
for _ in range(N):
    As.append(list(map(int, input().rstrip().split())))
    
# print(As)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

count = 0

while True:
    visited = [[False] * (N) for _ in range(N)]
    unions = []
    dq = deque()
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dq.append((i, j))
                c_union = []
                while dq:
                    cr, cc = dq.popleft()
                    if not visited[cr][cc]:
                        cn = As[cr][cc]
                        c_union.append((cr, cc))
                        visited[cr][cc] = True
                        for d in directions:
                            nr, nc = cr + d[0], cc + d[1]
                            if 0 <= nr < N and 0 <= nc < N:
                                nn = As[nr][nc]
                                if L <= abs(cn - nn) <= R:
                                    dq.append((nr, nc))
                if len(c_union) > 1:
                    unions.append(c_union)
    if unions:
        count += 1
        # print(f"[count: {count}]")
        # for u in unions:
        #     print(u)
        for union in unions:
            total_population = sum(As[r][c] for r, c in union)
            new_population = total_population // len(union)
            for r, c in union:
                As[r][c] = new_population
    else:
        break
            
print(count)