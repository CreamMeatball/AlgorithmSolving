from collections import deque

N, K = map(int, input().split())

start = N
dq = deque([(N, 0)])

visited = [float('inf')] * (150001)
# 주어지는 점의 존재 위치는 100,000 까지지만, 순간이동을 통해서 더 넘어갈 수 있으므로 100,000 보다 더 크게 잡음.
# visited를 그냥 True/False 로 잡아버리면, 어떤 특정한 위치에 도달하는 데 다른 경로를 통해 이동했고, 이 경로도 동일하게 최소 시간이 걸렸지만,
# queue 상에서는 동일한 최소 시간을 갖는 다른 경로보다 늦게 도착할 수 있으므로
# visited를 True/False 로 잡는 대신, 소요 시간으로 잡아서, 다른 경로를 통해 queue 상에선 늦게 도착하더라도
# 도착까지 걸린 시간만 같으면 허용 가능하게끔 설정.

result = 0
min_time = float('inf')

while dq:
    c_pos, c_time = dq.popleft()
    
    if c_time > min_time: # 현재까지 걸린 시간이, 이미 먼저 목표 지점에 도착한 경로의 소요시간보다 길다면, 이미 실패이므로 날리기.
        continue
    
    if c_pos == K:
        if c_time <= min_time:
            result += 1
            min_time = c_time
    
    n_pos = [c_pos - 1, c_pos + 1, 2 * c_pos]
    
    for np in n_pos:
        if (0 <= np <= 150000) and (c_time <= visited[np]):
            dq.append((np, c_time + 1))
            if np != K:
                visited[np] = c_time
            
print(min_time)
print(result)

# 5 17 이면
# 1) 5 -> 4 -> 8 -> 16 -> 17 해서 4번만에 도착
# 2) 5 -> 10 -> 9 -> 18 -> 17 해서 4번만에 도착