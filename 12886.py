import sys
from collections import deque

a, b, c = map(int, input().split())

if (a + b + c) % 3 != 0:
    print(0)
    sys.exit()

def transfer(x, y, z): # x, y에 대해서만 돌 넘겨주기 연산
    if x == y:
        return x, y, z
    if x < y:
        return x + x, y - x, z
    else:
        return x - y, y + y, z
    
visited = set()

dq = deque([])
# if a != b: dq.append((a, b, c))
# if b != c: dq.append((b, c, a))
# if c != a: dq.append((c, a, b))
start = tuple(sorted((a, b, c))) # (3, 4, 5) 든 (3, 5, 4) 든 같은 경우임.
dq = deque([start])
visited.add(start)

result = 0

while dq:
    x, y, z = dq.popleft()

    if x == y == z:
        result = 1
        break

    # (x, y) 쌍을 골라 돌 넘겨주기 연산을 하는 경우
    if x != y:
        nx, ny, nz = transfer(x, y, z)
        state = tuple(sorted((nx, ny, nz))) # (3, 4, 5) 든 (3, 5, 4) 든 같은 경우임.
        if state not in visited:
            visited.add(state)
            dq.append(state)

    # (y, z) 쌍을 골라 돌 넘겨주기 연산을 하는 경우
    if y != z:
        ny, nz, nx = transfer(y, z, x)
        state = tuple(sorted((nx, ny, nz))) # (3, 4, 5) 든 (3, 5, 4) 든 같은 경우임.
        if state not in visited:
            visited.add(state)
            dq.append(state)

    # (x, z) 쌍을 골라 돌 넘겨주기 연산을 하는 경우
    if x != z:
        nx, nz, ny = transfer(x, z, y)
        state = tuple(sorted((nx, ny, nz))) # (3, 4, 5) 든 (3, 5, 4) 든 같은 경우임.
        if state not in visited:
            visited.add(state)
            dq.append(state)
    
print(result)