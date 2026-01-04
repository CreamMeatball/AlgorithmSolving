from collections import deque

s, t = map(int, input().split())

if s == t:
    print(0)
    exit()

visited = set()
visited.add(s)

q = deque()
q.append((s, ""))

found = False

while q:
    curr_val, ops = q.popleft()
    
    if curr_val == t:
        print(ops)
        found = True
        break
    
    # 1. * 연산
    next_val = curr_val * curr_val
    if next_val <= 10**9 and next_val not in visited:
        visited.add(next_val)
        q.append((next_val, ops + "*"))
        
    # 2. + 연산
    next_val = curr_val + curr_val
    if next_val <= 10**9 and next_val not in visited:
        visited.add(next_val)
        q.append((next_val, ops + "+"))
        
    # 3. - 연산 (s - s = 0)
    next_val = curr_val - curr_val
    if next_val not in visited:
        visited.add(next_val)
        q.append((next_val, ops + "-"))
        
    # 4. / 연산 (s / s = 1)
    if curr_val != 0:
        next_val = curr_val // curr_val
        if next_val not in visited:
            visited.add(next_val)
            q.append((next_val, ops + "/"))

if not found:
    print(-1)