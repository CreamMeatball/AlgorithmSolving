X, Y = map(int, input().split())

Z = Y * 100 // X
init_Z = Z

add_games = -1
# while Z == init_Z:
#     X += 1
#     Y += 1
#     add_games += 1
#     Z = Y * 100 // X
# X가 10억 이하라 너무 커서 시간 초과 남.

# 이진 탐색
start, end = 1, 1000000000
while start <= end:
    mid = (start + end) // 2
    if (Y + mid) * 100 // (X + mid) > init_Z:
        end = mid - 1
        add_games = mid
    else:
        start = mid + 1

print(add_games)