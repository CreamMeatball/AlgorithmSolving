from collections import deque

N, K = map(int, input().split())
coins = str(input().strip())

start_t = coins.count('T')
visited = [-1] * (N + 1)
visited[start_t] = 0

q = deque([start_t])

result = -1

# 각각의 동전을 개별적인 존재라고 보지 말고
# 그냥 앞면/뒷면의 '개수'로만 따져서 진행하면 됨. 그러면 더 효율적으로 할 수 있음.

# 어차피 구분이 안되는 동전들이며, 모두 다 뒤집기만 하면 되니,
# 동전끼리 구분을 안해도 됨. permutation 대신 combination으로 하는 느낌.

while q:
    curr_t = q.popleft() # 현재 뒷면의 개수
    
    if curr_t == N:
        result = visited[curr_t]
        break
        
    for i in range(K + 1):
        # i: 뒤집을 T의 개수
        # K - i: 뒤집을 H의 개수
        if i <= curr_t and (K - i) <= (N - curr_t):
            next_t = curr_t - i + (K - i) # 새 뒷면의 개수
            
            if visited[next_t] == -1:
                visited[next_t] = visited[curr_t] + 1
                q.append(next_t)

print(result)