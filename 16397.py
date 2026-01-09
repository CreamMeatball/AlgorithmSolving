from collections import deque

N, T, G = map(int, input().split())

MAX = 100000
visited = [False] * MAX

def press_b(x):
    x *= 2
    if x >= MAX:
        return False  # 곱하는 순간 99999 초과면 실패
    s = str(x)
    # 가장 높은 자릿수 1 감소
    first = int(s[0]) - 1
    if first < 0:
        first = 0
    return int(str(first) + s[1:])

def bfs():
    dq = deque()
    dq.append((N, 0))
    visited[N] = True

    while dq:
        current, count = dq.popleft()

        if current == G:
            return count
        if count == T:
            continue

        # 버튼 A
        next = current + 1
        if next < MAX and not visited[next]:
            visited[next] = True
            dq.append((next, count + 1))

        # 버튼 B
        next = press_b(current)
        if next and not visited[next]:
            visited[next] = True
            dq.append((next, count + 1))

    return -1

result = bfs()
if result == -1:
    print("ANG") # ㅋㅋㅋㅋㅋ
else:
    print(result)
