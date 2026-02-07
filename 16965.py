import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
intervals = []

for _ in range(N):
    query = input().rstrip().split()
    cmd = int(query[0])
    op1 = int(query[1])
    op2 = int(query[2])

    if cmd == 1:
        intervals.append((op1, op2))
    else:
        start_idx = op1 - 1
        target_idx = op2 - 1
        
        q = deque([start_idx])
        visited = [False] * len(intervals)
        visited[start_idx] = True
        found = False
        
        while q:
            curr = q.popleft()
            
            if curr == target_idx:
                found = True
                break
            
            x1, y1 = intervals[curr]
            for i in range(len(intervals)):
                if not visited[i]:
                    x2, y2 = intervals[i]
                    # 이동 조건: x2 < x1 < y2 또는 x2 < y1 < y2
                    if (x2 < x1 < y2) or (x2 < y1 < y2):
                        visited[i] = True
                        q.append(i)
        
        if found:
            print(1)
        else:
            print(0)