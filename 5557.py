N = int(input())
numbers = [0] + list(map(int, input().split()))
numbers, answer = numbers[:-1], numbers[-1]

# print(len(numbers))
# print(numbers)

dp = [[0] * 21 for _ in range(N)]
# dp[i][j]: i번째 숫자까지 고려했을 때, 합이 j가 되는 경우의 수
# dp[0][0] = 1 # 주어진 숫자 중 첫 숫자가 0일 경우, dp[1][0] = 2 가 되는 버그가 생김 (왜냐면 첫 숫자는 앞에 부호가 없어서, 이 경우에 경우의 수가 1개여야 함)
dp[1][numbers[1]] = 1

for i in range(2, N):
    number = numbers[i]
    for j in range(0, 21):
        if (j - number) >= 0: # number를 더했을 때 j가 되는 경우를 위해 조건 필터링
            dp[i][j] += dp[i - 1][j - number]
        if (j + number) <= 20: # number를 더했을 때 j가 되는 경우를 위해 조건 필터링
            dp[i][j] += dp[i - 1][j + number]
            
# for d in dp:
#     print(*d)
    
print(dp[N - 1][answer])