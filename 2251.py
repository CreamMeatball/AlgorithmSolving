from collections import deque

A, B, C = map(int, input().split())

dq = deque([(0, 0, C)])
visited = [[[False] * (C + 1) for _ in range(B + 1)] for _ in range(A + 1)] # 물이 0일 때부터 꽉 차있을 때까지 체크해야하기 때문에 +1

result = set()

while dq:
    ca, cb, cc = dq.popleft()
    
    if visited[ca][cb][cc]:
        continue
    visited[ca][cb][cc] = True
    
    if ca == 0:
        result.add(cc)
    
    # 총 6가지 경우의 수가 있음.
    # A->B, A->C, B->A, B->C, C->A, C->B.
    
    # A->B
    water = min(ca, B - cb) # A에 있는 양, B에 남은 공간
    na, nb, nc = ca - water, cb + water, cc
    if not visited[na][nb][nc]:
        dq.append((na, nb, nc))
    
    # A->C
    water = min(ca, C - cc)
    na, nb, nc = ca - water, cb, cc + water
    if not visited[na][nb][nc]:
        dq.append((na, nb, nc))
    
    # B->A
    water = min(cb, A - ca)
    na, nb, nc = ca + water, cb - water, cc
    if not visited[na][nb][nc]:
        dq.append((na, nb, nc))
    
    # B->C
    water = min(cb, C - cc)
    na, nb, nc = ca, cb - water, cc + water
    if not visited[na][nb][nc]:
        dq.append((na, nb, nc))
    
    # C->A
    water = min(cc, A - ca)
    na, nb, nc = ca + water, cb, cc - water
    if not visited[na][nb][nc]:
        dq.append((na, nb, nc))
    
    # C->B
    water = min(cc, B - cb)
    na, nb, nc = ca, cb + water, cc - water
    if not visited[na][nb][nc]:
        dq.append((na, nb, nc))
    
print(*sorted(result))