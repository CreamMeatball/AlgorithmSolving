import sys
from collections import defaultdict, deque

input_ = sys.stdin.readline

N, M = map(int, input_().rstrip().split())

studentCompare = defaultdict(list)
indegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input_().rstrip().split())
    studentCompare[a].append(b)
    indegree[b] += 1

# print(studentCompare)
# print(indegree)

# 위상 정렬    
def topology_sort():
    idx = 0
    result = []
    dq = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            dq.append(i)
            
    while dq:
        current = dq.popleft()
        result.append(current)
        for next in studentCompare[current]:
            indegree[next] -= 1
            if indegree[next] == 0:
                dq.append(next)
                idx += 1
                    
    return result

result = topology_sort()
print(*result)