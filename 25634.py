N = int(input())

As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

# 초기 상태의 밝기 합
total_brightness = sum(As[i] for i in range(N) if Bs[i] == 1)

dp = [0] * N # '변화량'에 대해서만 계산.
max_change = -float('inf')

for i in range(N):
    # 현재 전구를 뒤집었을 때의 변화량 (꺼져있으면 +As[i], 켜져있으면 -As[i])
    current_change = As[i] if Bs[i] == 0 else -As[i]

    if i == 0:
        dp[i] = current_change
    else:
        # 이전까지의 연속 합 + 이번까지 이어갔을 때의 값과, 현재 위치에서 새로 시작하는 것 중 큰 값 선택
        dp[i] = max(dp[i-1] + current_change, current_change)
    
    max_change = max(max_change, dp[i])

print(total_brightness + max_change)