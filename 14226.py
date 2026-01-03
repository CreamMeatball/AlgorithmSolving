from collections import deque

S = int(input())

visited = [[-1] * 2001 for _ in range(2001)]

q = deque()

q.append((1, 0)) # (화면상 이모티콘 1개, 클립보드 상 0개)
visited[1][0] = 0 # 시간으로 기입 (0초). queue 에 시간 변수 추가해서 넣어줘도 될 거 같은데, 이렇게 하는 게 더 효율적인 듯.

while q:
    s, c = q.popleft()
    
    if s == S:
        print(visited[s][c])
        break
    
    # 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
    if visited[s][s] == -1:
        visited[s][s] = visited[s][c] + 1
        q.append((s, s))
        
    # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
    if c > 0 and s + c <= 2000:
        if visited[s + c][c] == -1:
            visited[s + c][c] = visited[s][c] + 1
            q.append((s + c, c))
            
    # 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
    if s > 0:
        if visited[s - 1][c] == -1:
            visited[s - 1][c] = visited[s][c] + 1
            q.append((s - 1, c))