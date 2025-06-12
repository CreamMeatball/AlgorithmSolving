import sys
from collections import defaultdict, deque

input_ = sys.stdin.readline

N, M = map(int, input_().rstrip().split())

singers = defaultdict(list)
indegree = [0] * (N + 1) # indegree[2] = 1 -> 2번쨰 노드를 가기 위해 선행되어야 하는 노드가 1개라는 뜻

for _ in range(M):
    temp = list(map(int, input_().rstrip().split()))
    # for i in range(1, len(temp) - 1):
    #     for j in range(i + 1, len(temp)):
    #         singers[temp[i]].append(temp[j])
    #         indegree[temp[i]] += 1
    for i in range(1, len(temp) - 1):
        singers[temp[i]].append(temp[i + 1])
        # 자기 뒤쪽의 모든 노드 다 저장해놓을 필요 없이 바로 뒤 노드 하나와의 관계만 저장해주면 됨.
        indegree[temp[i + 1]] += 1
        
# print(singers)
# print(indegree)       

# 위상 정렬
def topology_sort():
    result = []
    dq = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            dq.append(i)
            
    while dq:
        current = dq.popleft()
        result.append(current)
        for next_singer in singers[current]:
            indegree[next_singer] -= 1
            if indegree[next_singer] == 0:
                dq.append(next_singer)
                
    return result

result = topology_sort()
if len(result) == N:
    for r in result:
        print(r)
else:
    print(0)