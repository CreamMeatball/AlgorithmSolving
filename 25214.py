N = int(input())
numbers = [0] + list(map(int, input().split()))

dp = [-float('inf')] * (N + 1)
min_num = float('inf')

for i in range(1, N + 1):
    number = numbers[i]
    min_num = min(min_num, number)
    max_diff = dp[i - 1]
    diff = number - min_num
    max_diff = max(max_diff, diff)
    dp[i] = max_diff
    
print(*dp[1:])