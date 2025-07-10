from collections import deque

N = int(input())
scvs = list(map(int, input().split()))

attack_case1 = [(9)]
attack_case2 = [(9,3), (3,9)]
attack_case3 = [(9,3,1), (9,1,3), (3,9,1), (3,1,9), (1,9,3), (1,3,9)]


dq = deque([scvs + [0]])
if N == 1:
    visited = [False] * (scvs[0] + 1)
elif N == 2:
    visited = [[False] * (scvs[1] + 1) for _ in range(scvs[0] + 1)]
else:
    visited = [[[False] * (scvs[2] + 1) for _ in range(scvs[1] + 1)] for _ in range(scvs[0] + 1)]
    
while dq:
    *scv, count = dq.popleft()
    # print(f"{scv}, {count}")
    if N == 1:
        if visited[scv[0]]:
            continue
        visited[scv[0]] = True
    elif N == 2:
        if visited[scv[0]][scv[1]]:
            continue
        visited[scv[0]][scv[1]] = True
    else:
        if visited[scv[0]][scv[1]][scv[2]]:
            continue
        visited[scv[0]][scv[1]][scv[2]] = True

    dead_count = 0
    for sc in scv:
        if sc <= 0:
            dead_count += 1
    if dead_count == N:
        print(count)
        break
        
    if N == 1:
        dq.append([max(scv[0] - attack_case1[0], 0), count + 1])
    elif N == 2:
        for ac in attack_case2:
            dq.append([max(scv[0] - ac[0], 0), max(scv[1] - ac[1], 0), count + 1])
    else:
        for ac in attack_case3:
            dq.append([max(scv[0] - ac[0], 0), max(scv[1] - ac[1], 0), max(scv[2] - ac[2], 0), count + 1])
    