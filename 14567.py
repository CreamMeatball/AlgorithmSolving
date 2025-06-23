# 2056 문제랑 굉장히 유사.

import sys
from collections import defaultdict, deque

input_ = sys.stdin.readline

N, M = map(int, input_().rstrip().split())
pre = defaultdict(list) # B: A
post = defaultdict(list) # A: B
prefix = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input_().rstrip().split())
    pre[B].append(A)
    post[A].append(B)

for b, a in pre.items():
    prefix[b] = len(a)
    
dp = [N + 1] * (N + 1) # i번째 과목이 걸리는 최소 총 학기 수

dq = deque()
for i in range(1, N + 1):
    if prefix[i] == 0:
        dq.append(i)
        dp[i] = 1

# print("pre_list: ")
# print(pre)
# print("post_list: ")
# print(post)
# print("prefix: ")
# print(prefix)
# print("dp: ")
# print(dp)

while dq:
    current = dq.popleft()
    for next in post[current]:
        prefix[next] -=1 
        if prefix[next] == 0: # 이번 완료된 작업을 선행 작업으로 포함하는 애들한테 물어보기. 혹시 이번 완료를 통해 모든 선행 작업이 완료됐니?
            dq.append(next)
            acc_time = 0
            for pr in pre[next]:
                acc_time = max(acc_time, dp[pr])
                # max인 이유: 모든 선행 작업이 다 종료됐다는 전제에서, 완료된 선행 작업들 중 가장 늦게 끝난 시점부터 새 작업을 이어나갸야하기 때문.
            dp[next] = acc_time + 1
            
print(*dp[1:])