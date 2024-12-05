N = int(input())

dp = [0 for _ in range(N+1)]
dp[0] = N
count = 0

for i in range(1, N+1):
    if dp[i - 1] == 1:
        break
    
    if dp[i - 1] % 3 == 0:
        dp[i] = dp[i - 1] // 3
        count += 1
        # print("divide by 3")
        continue
    # 이번에 1을 빼서, 다음에 3으로 나눌 수 있을 경우.
    # 이 경우 때문에 그 다음 단계를 고려해야해서, dp로 풀게 됨.
    elif (dp[i - 1] - 1) % 3 == 0:
        dp[i] = dp[i - 1] - 1
        count += 1
        # print("subtract 1 for divide by 3 in next time")
        continue
    elif dp[i - 1] % 2 == 0:
        dp[i] = dp[i - 1] // 2
        count += 1
        # print("divide by 2")
        continue
    elif (dp[i - 1] - 1) % 2 == 0:
        dp[i] = dp[i - 1] - 1
        count += 1
        # print("subtract 1 for divide by 3 in next time")
        continue
    else:
        dp[i] = dp[i - 1] - 1
        count += 1
        # print("subtract 1")
        continue
    
# print(dp)
print(count)