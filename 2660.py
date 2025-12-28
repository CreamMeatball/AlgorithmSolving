import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input().rstrip())

friends = defaultdict(list)

while True:
    a, b = map(int, input().rstrip().split())
    if a == -1 and b == -1:
        break
    friends[a].append(b)
    friends[b].append(a)

def bfs(start):
    visited = [-1] * (N + 1)
    visited[start] = 0
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for neighbor in friends[current]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[current] + 1
                queue.append(neighbor)
                
    return max(visited) # 가장 먼 거리 반환

scores = []
for i in range(1, N + 1):
    scores.append(bfs(i)) # 탐색한 모든 거리 중 가장 먼 거리값이 그 회원의 점수가 됨.

min_score = min(scores)
candidates = [i + 1 for i, score in enumerate(scores) if score == min_score]

print(min_score, len(candidates))
print(*candidates)