from collections import deque

N = int(input())
bridge = [0] + list(map(int, input().split()))
a, b = map(int, input().split())

visited = [False] * (N + 1)
dq = deque([(a, 0)])
visited[a] = True

result = -1
while dq:
    current, current_count = dq.popleft()
    
    if current == b:
        result = current_count
        break
    
    jump = bridge[current]
    
    # 앞으로 이동
    for next_pos in range(current + jump, N + 1, jump):
        if not visited[next_pos]:
            visited[next_pos] = True
            dq.append((next_pos, current_count + 1))
    
    # 뒤로 이동(도 가능!)
    for next_pos in range(current - jump, 0, -jump):
        if not visited[next_pos]:
            visited[next_pos] = True
            dq.append((next_pos, current_count + 1))

print(result)