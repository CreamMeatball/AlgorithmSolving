import sys

input = sys.stdin.readline

N = int(input().rstrip())

# 구하고자 하는 건 엄청 단순한데
# N이 커서 시간 효율적으로 하기 위해 누적합 + 투 포인터 씀
# (단순 방식으로 하면 5만 * 5만 = 25억번 연산 필요)

# 누적합
pref = [0] * (N + 1)
for i in range(N):
    pref[i+1] = pref[i] + int(input().rstrip())

total = pref[-1]
half = total / 2 # 시계/반시계방향 중 짧은 거 쓴다라는 것 때문에, 총 거리의 절반을 투 포인터에서의 기준으로 사용
max_dist = 0

# 투 포인터
left = 0
right = 1

# 투 포인터는 모든 permutation case를 다 훑는 게 아님
# left를 중심점으로 잡고 right을 최대한 늘리면서
# 이득인 case들만 탐색하는 거.
while left < N and right <= N:
    dist = pref[right] - pref[left]
    min_dist = min(dist, total - dist) # total - dist 를 통해 반시계방향 거리 쉽게 계산 
    max_dist = max(max_dist, min_dist)
    
    if dist < half:
        right += 1
    elif dist > half:
        left += 1
    else:
        break

print(max_dist)
