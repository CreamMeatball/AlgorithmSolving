import sys
input = sys.stdin.readline

N, H = map(int, input().split())
prefix = [0] * (H + 2)
# 벽으로 인해 막히는 시작 위치를 1,
# 벽이 없어져서 뚫리는 시점 위치를 -1 로 표시.

# 그냥 장애물 있을 때마다 해당 위치에 +1 하는 게 직관적인 방식인데
# 그러면 반복문으로 해당 위치들에 다 +1 씩 해줘야해서
# 가로 * 세로 --> 200,000 * 500,000 해서 1000억번 연산해야됨.
# 그래서 효율적인 방식을 취하는 것.

# 어떠한 한 가로 위치에서,
# 위/아래 한 방향에서 시작한 종유석이 진행되다 멈춘 이후로는 다시 발생하지 않는다는 전제에서 취할 수 있는
# 아주 효율적이고 똑똑한 방식.

for i in range(N):
    h = int(input().rstrip())
    if i % 2 == 0:
        prefix[1] += 1
        prefix[h + 1] -= 1
    else:
        prefix[H - h + 1] += 1
        prefix[H + 1] -= 1

current = 0
min_obs = N
cnt = 0

for i in range(1, H + 1):
    current += prefix[i]
    if current < min_obs:
        min_obs = current
        cnt = 1
    elif current == min_obs:
        cnt += 1

print(min_obs, cnt)