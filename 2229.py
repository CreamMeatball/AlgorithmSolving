N = int(input())
numbers = list(map(int, input().split()))

# dp[i]는 1번째부터 i번째 학생까지 있을 때 "잘 짜여진 정도"의 최댓값
dp = [0] * (N + 1)

# 이전까지의 모든 조 분리 경우의 수를 통틀어 최대값 + 이번 조의 값
# 근데 여기서 '이전'의 경계를 loop를 돌며 모든 경우 탐색.
# 이렇게 이분적으로 생각
for i in range(1, N + 1):
    current_max = numbers[i-1]
    current_min = numbers[i-1]

    for j in range(i, 0, -1): # 이전 조의 마지막이 j일 때:
        current_max = max(current_max, numbers[j-1])
        current_min = min(current_min, numbers[j-1])

        group_score = current_max - current_min
        total_score = dp[j-1] + group_score

        dp[i] = max(dp[i], total_score)

print(dp[N])

# 되게 영리하고 효율적인 방식 ㄷㄷ