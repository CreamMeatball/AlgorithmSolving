N = int(input())
testPrint = False

count = 0
procedure = []

dp = [float("inf")] * (N + 1)
dp_which = [-1] * (N + 1)
dp[N] = 0

for n in range(N, 0, -1):
    if n % 3 == 0:
        if dp[n] + 1 < dp[n//3]:
            dp[n//3] = dp[n] + 1
            dp_which[n//3] = 3
    if n % 2 == 0:
        if dp[n] + 1 < dp[n//2]:
            dp[n//2] = dp[n] + 1
            dp_which[n//2] = 2
    if dp[n] + 1 < dp[n-1]:
        dp[n-1] = dp[n] + 1
        dp_which[n-1] = 1
    
print(f"dp: {dp}") if testPrint else None
    
print(dp[1])
i = 1
while i <= N:
    procedure.append(i)
    if dp_which[i] == 3:
        i *= 3
    elif dp_which[i] == 2:
        i *= 2
    else:
        i += 1

print(*procedure[dp[1]::-1])