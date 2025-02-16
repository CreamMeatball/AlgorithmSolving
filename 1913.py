N = int(input())
find_number = int(input())

snail_map = [[0] * N for _ in range(N)]

r = c = N // 2
snail_map[r][c] = 1
find_r, find_c = r, c  
num = 2

# 방향: 위, 오른쪽, 아래, 왼쪽 (시계방향)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction = 0
step = 1  # 현재 방향으로 이동할 칸 수

while num <= N * N:
    for _ in range(2):
        for _ in range(step):
            if num > N * N:
                break
            r += directions[direction][0]
            c += directions[direction][1]
            snail_map[r][c] = num
            if num == find_number:
                find_r, find_c = r, c
            num += 1
        direction = (direction + 1) % 4
    step += 1

for row in snail_map:
    print(' '.join(map(str, row)))
print(find_r + 1, find_c + 1)