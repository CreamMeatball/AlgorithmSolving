N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
dp_list = [[x] for x in A]

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            dp_list[i] = dp_list[j] + [A[i]]

length = max(dp)
print(length)

index = dp.index(length)
print(*dp_list[index])