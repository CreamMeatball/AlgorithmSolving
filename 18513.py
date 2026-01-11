from collections import deque

N, K = map(int, input().split())
sams = list(map(int, input().split()))

visited = set()
q = deque()

for sam in sams:
    q.append((sam, 1)) # (위치, 앞으로 탐색할 양옆 거리)
    visited.add(sam)
    
# 집들이 설치될 수 있는 여러 경우의 수를
# 탐색하면서 다 비교한 뒤
# 그 중 최적인 걸 찾자..
# 이렇게 처음 생각했는데

# 엄청 걍 간단한 방식이 있었음.    

# 모든 샘터에서, 양옆 위치에 집을 짓는다.
# 짓고나면, 한 칸 더 벌어진 위치에서 집을 짓는다 (이 때, 이미 집이 지어져있다면 스킵)
# 그래서 총 K개 지으면 멈춘다.
# K개 짓는 동안 누적된 거리(불행도)를 더한다.

# 왜냐면 무조건 그냥 샘터 가까이 지으면
# 그게 그냥 최소임.

result = 0
count = 0

while q:
    now, dist = q.popleft()
    
    for d in [-1, 1]:
        next_pos = now + d
        
        if next_pos not in visited:
            visited.add(next_pos)
            result += dist
            count += 1
            q.append((next_pos, dist + 1))
            
            if count == K:
                print(result)
                exit()