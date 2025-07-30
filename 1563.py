N = int(input())
divisor = 10 ** 6

# 모든 경우의 수 combination으로 다 하기엔 너무 많고
# dp shape (3,3,3) 으로 하기에도 너무 많음 (최대 3 ** 1000)
# -> dp[day][late][absent]
# ex) dp[2][1][0] : 둘째 날에 지각한 경우
# ex) dp[2][0][2] : 둘째 날에 결석 해서 연속 두 번 결석 스택 쌓인 경우

dp = [[[0] * 3 for _ in range(2)] for _ in range(N + 1)]
dp[0][0][0] = 1

# 개근 실패:
# 1) 지각 두 번 이상
# 2) 결석 세 번 연속

for day in range(N):
    for late in range(2):
        for absence in range(3):
            current = dp[day][late][absence]
            if current == 0: # 없으면 건너뛰기
                continue

            # 출석
            # 전 날에 지각 한 경우와 안 한 경우(출석) 더하기
            dp[day+1][late][0] = (dp[day+1][late][0] + current) % divisor

            # 지각 (지각 0 -> 1만 허용)
            # 전 날에 지각을 안 한 경우만 더하기
            if late == 0:
                dp[day+1][1][0] = (dp[day+1][1][0] + current) % divisor

            # 결석 (연속 0,1 -> +1만 허용)
            # absence 스택이 0 혹은 1 인 경우만 더하기
            if absence < 2:
                dp[day+1][late][absence+1] = (dp[day+1][late][absence+1] + current) % divisor

answer = 0
for late in range(2):
    for absence in range(3):
        answer = (answer + dp[N][late][absence]) % divisor
print(answer)