import sys

input = sys.stdin.readline

N, M = map(int, input().split())
P = list(map(int, input().split()))

# 2회 이상 멘션한 사람들의 총합과 인원수 계산 (평균 판별용)
sum_ge2 = 0
cnt_ge2 = 0
for x in P:
    if x >= 2:
        sum_ge2 += x
        cnt_ge2 += 1

# 메시지 발송 횟수 계산을 위한 빈도수 배열
# freq[i]: 평균 이하 그룹 중 멘션 횟수가 정확히 i번인 사람의 수
freq = [0] * (M + 1)
msg1_from_large = 0

for x in P:
    # 평균 이하인지 판별 (나눗셈 오차 방지를 위해 곱셈 비교)
    # 2회 이상 멘션자가 없으면 평균은 0이므로 모든 x는 평균 초과가 됨
    if cnt_ge2 > 0 and x * cnt_ge2 <= sum_ge2:
        # 평균 이하인데 멘션 횟수가 메시지 종류 M보다 많으면 중복 메시지 발생 (-1)
        if x > M:
            print("-1")
            sys.exit()
        freq[x] += 1
    else:
        # 평균 초과 그룹은 1번 메시지만 딱 1회 발송
        msg1_from_large += 1

# 누적합을 이용하여 메시지 번호별 총 발송 횟수 계산
# i번 메시지를 받는 사람은 '평균 이하 그룹 중 멘션 횟수가 i 이상인 사람'의 총합임
ans = [0] * (M + 1)
current_suffix_sum = 0
for i in range(M, 0, -1):
    current_suffix_sum += freq[i]
    ans[i] = current_suffix_sum

# 1번 메시지에는 평균 초과 그룹이 보낸 횟수를 합산
ans[1] += msg1_from_large

# 일반 방식:
# O(N * M)
# 누적합 방식:
# O(N + M)

print(*(ans[1:]))
