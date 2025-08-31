n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]

max_count = -1
leader = 0

for i in range(n):
    count = 0
    for j in range(n):
        if i == j:
            continue
        for k in range(5):
            if classes[i][k] == classes[j][k]:
                count += 1
                break  # 한 번이라도 같은 반이면 더 이상 비교할 필요 없음
    if count > max_count:
        max_count = count
        leader = i + 1

print(leader)