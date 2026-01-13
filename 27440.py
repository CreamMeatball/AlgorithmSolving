from collections import deque

N = int(input()) # N이 엄청 큼 (10^18)

visited = {N: 0} # value visited 방식. visited = True/False 말고 count값 넣어서 동시에 효율적 해결.
q = deque([N])

while q:
    current = q.popleft()
    
    if current == 1:
        print(visited[current])
        break
        
    cnt = visited[current]
    
    if current % 3 == 0 and current // 3 not in visited:
        visited[current // 3] = cnt + 1
        q.append(current // 3)
        
    if current % 2 == 0 and current // 2 not in visited:
        visited[current // 2] = cnt + 1
        q.append(current // 2)
        
    if current - 1 not in visited:
        visited[current - 1] = cnt + 1
        q.append(current - 1)