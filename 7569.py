import sys

input_data = sys.stdin.readline

testPrint = False

M, N, H = map(int, input_data().split())
# M : col, N : row, H : height

box = [[[-1] * (M + 2) for _ in range(N + 2)] for _ in range(H + 2)]
visited = [[[False] * (M + 2) for _ in range(N + 2)] for _ in range(H + 2)]

totalFreshTomatoes = 0

ripeTomatoesPositions = []

direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

for h in range(1, H+1):
    for n in range(1, N+1):
        tomato_data = list(map(int, input_data().split()))
        tomato_data = [-1] + tomato_data + [-1]
        for i, c in enumerate(tomato_data):
            if c == 1:
                ripeTomatoesPositions.append((h, n, i))
            elif c == 0:
                totalFreshTomatoes += 1
        box[h][n] = tomato_data

day = 0

for h in range(H + 2):
    print(box[h]) if testPrint else None
print(f"totalFreshTomatoes: {totalFreshTomatoes}") if testPrint else None
print(f"ripeTomatoesPositions: {ripeTomatoesPositions}") if testPrint else None
print(f"day: {day}") if testPrint else None

def bfs(ripeTomatoesPositions, box, visited, totalFreshTomatoes):
    global day
    queue = ripeTomatoesPositions
    while queue:
        next_queue = []
        for h, n, m in queue:
            for dh, dn, dm in direction:
                next_h, next_n, next_m = h + dh, n + dn, m + dm
                print(f"next_h: {next_h}, next_n: {next_n}, next_m: {next_m}") if testPrint else None
                if (1 <= next_h <= H) and (1 <= next_n <= N) and (1 <= next_m <= M) and \
                    (box[next_h][next_n][next_m] == 0 and not visited[next_h][next_n][next_m]):
                        
                    visited[next_h][next_n][next_m] = True
                    box[next_h][next_n][next_m] = 1
                    totalFreshTomatoes -= 1
                    next_queue.append((next_h, next_n, next_m))
        # queue를 다 돌면
        queue = next_queue # 이미 주변으로 전파한 토마토는 더 이상 전파되는 의미가 없으므로, 기존의 queue가 덮어씌워져도 됨
        if queue:
            day += 1
            print(f"day: {day}, totalFreshTomatoes: {totalFreshTomatoes}") if testPrint else None
        if totalFreshTomatoes < 1:
            return totalFreshTomatoes
        # queue에 없을 경우 = 익은 토마토가 더 전파될 수 없는 경우
        # 첫 줄인 while queue:로 돌아가고, queue가 비어있으므로 while문이 종료됨
        # 그리고 다음 return문으로 진행
    return totalFreshTomatoes

remainingFreshTomatoes = bfs(ripeTomatoesPositions, box, visited, totalFreshTomatoes)
if remainingFreshTomatoes > 0:
    print(-1)
else:
    print(day)
    
