import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())

ladder = {}
for _ in range(N):
    data = list(map(int, input_data().split()))
    ladder[data[0]] = data[1]
    
snake = {}
for _ in range(M):
    data = list(map(int, input_data().split()))
    snake[data[0]] = data[1]
    
roll = [0] * 101
visited = [False] * 101

def bfs(current):
    queue = [current]
    while queue:
        current = queue.pop(0)
        for i in range(1, 7):
            next = current + i
            if next > 100:
                continue
            if next in snake:
                next = snake[next]
                # continue
                # continue 하면 틀림. 뱀도 타줘야됨.
            if next in ladder:
                next = ladder[next]
            if not visited[next]:
                visited[next] = True
                roll[next] = roll[current] + 1
                queue.append(next)
    
bfs(1)
print(roll[100])