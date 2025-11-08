import sys

input = sys.stdin.readline

N = int(input().rstrip())

numbers = [0.0]

for _ in range(N):
    numbers.append(float(input().rstrip()))
    
dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = max(numbers[i], dp[i - 1] * numbers[i])
    
# print(dp[1:])
print(f"{max(dp[1:]):.3f}")