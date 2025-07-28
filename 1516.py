import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input().rstrip())

prefix_detail = defaultdict(list)
postfix_detail = defaultdict(list)
indegree = [0] * (N + 1)
timecost = [0] * (N + 1)
for i in range(1, N + 1):
    data = list(map(int, input().rstrip().split()))
    timecost[i] = data[0]
    prefix_detail[i].extend(data[1:-1])
    indegree[i] += len(data[1:-1])
    for p in prefix_detail[i]:
        postfix_detail[p].append(i)
    
# print(prefix_detail)
# print(indegree)
# print(postfix_detail)

time_require = [0] * (N + 1)
dp = [0] * (N + 1)

dq = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        dq.append(i)
        
while dq:
    current = dq.popleft()
    max_require = 0
    for p in prefix_detail[current]:
        max_require = max(max_require, dp[p])
    dp[current] = max_require + timecost[current]
    for p in postfix_detail[current]:
        indegree[p] -= 1
        if indegree[p] == 0:
            dq.append(p)
            
for d in dp[1:]:
    print(d)