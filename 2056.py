import sys
from collections import defaultdict, deque

input_ = sys.stdin.readline

N = int(input_().rstrip())

postfix = defaultdict(list) # i: [postfix]
prefix = defaultdict(list) # i: [prefix]
prefix_count = [0] * (N + 1)
time = [0] * (N + 1)

for i in range(1, N + 1):
    data = list(map(int, input_().rstrip().split()))
    time[i] = data[0]
    prefix_count[i] = data[1]
    if data[1] > 0:
        for pre in data[2:]:
            postfix[pre].append(i)
        prefix[i].extend(data[2:])
    
# print(postfix)
# print(prefix_count)

complete = 0
dp = [9999] * (N + 1) # i번쨰 작업이 수행 완료되는 최소 시간

dq = deque()
for i in range(1, N + 1):
    if prefix_count[i] == 0:
        dq.append(i)
        dp[i] = time[i]
        
while dq:
    current = dq.popleft()
    for next in postfix[current]:
        prefix_count[next] -= 1
        if prefix_count[next] == 0: # 이번 완료된 작업을 선행 작업으로 포함하는 애들한테 물어보기. 혹시 이번 완료를 통해 모든 선행 작업이 완료됐니?
            dq.append(next)
            acc_time = 0
            for pre in prefix[next]:
                # acc_time += dp[pre]
                acc_time = max(acc_time, dp[pre])
                # max인 이유: 모든 선행 작업이 다 종료됐다는 전제에서, 완료된 선행 작업들 중 가장 늦게 끝난 시점부터 새 작업을 이어나갸야하기 때문.
                # 그래야지 필요한 선행 작업들이 모두 완료된 시점이니까.
            # dp[next] = min(dp[next], acc_time)
            dp[next] = acc_time + time[next]
            
# print(dp)
print(max(dp[1:]))