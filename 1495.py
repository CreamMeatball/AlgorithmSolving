N, S, M = map(int, input().split())
volumes = [-1] + list(map(int, input().split()))

# dp = [[0] * (2) for _ in range(N + 1)]
# # dp[i][0]: 불륨을 감소시켜야 할 때 최대값
# # dp[i][1]: 불륨을 증가시켜야 할 때 최대값

# 위 구조로 못 풀음

# dp의 열을 선택지 2개(볼륨 올림/내림)로 하지 말고
# dp의 열을 불륨 크기 0 ~ M 으로 한다는 아이디어.
# (가능한 유효볼륨)

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][S] = 1

for i in range(1, N + 1):
    for idx, volume in enumerate(dp[i - 1]):
        if volume == 1:
            dx = idx - volumes[i]
            dx2 = idx + volumes[i]
            if 0 <= dx <= M:
                dp[i][dx] = 1
            if 0 <= dx2 <= M:
                dp[i][dx2] = 1

try:
    # print(M - list(reversed(dp[N])).index(1))
    print(M - dp[N][::-1].index(1))
except: # 1이 존재하지 않으면 에러 뜸
    print(-1)
    
# 4 8 20
# 4 2 9 9
# -> 최대값 20