import sys

input_data = sys.stdin.readline

T = int(input_data())

direction = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

def bfs(visited, current, destination, count, L):
    current_row, current_col = current
    destination_row, destination_col = destination
    visited[current_row][current_col] = True
    queue = [(current_row, current_col)]
    while queue:
        row, col = queue.pop(0)
        if row == destination_row and col == destination_col:
            return count[row][col]
        for i in range(8):
            next_row = row + direction[i][0]
            next_col = col + direction[i][1]
            # 원래 범위가 0 ~ L - 1인데, 시작점을 (2, 2)로 옮겼으므로 범위를 2 ~ L + 1로 변경. L + 2 아님 주의.
            if ((2 <= next_row) and (next_row <= L + 1) and (2 <= next_col) and (next_col <= L + 1)) \
                and \
                (not visited[next_row][next_col]):
                visited[next_row][next_col] = True
                count[next_row][next_col] = count[row][col] + 1
                queue.append((next_row, next_col))
            else:
                continue

for _ in range(T):
    L = int(input_data())
    current = list(map(int, input_data().split()))
    destination = list(map(int, input_data().split()))
    visited = [[False] * (L + 4) for _ in range(L + 4)]
    
    tailored_current = (current[0] + 2, current[1] + 2)
    tailored_destination = (destination[0] + 2, destination[1] + 2)
    
    count = [[0] * (L + 4) for _ in range(L + 4)]
    
    result = bfs(visited, tailored_current, tailored_destination, count, L)
    print(result)