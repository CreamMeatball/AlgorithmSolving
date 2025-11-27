import sys

input = sys.stdin.readline

S = str(input().strip())
N = int(input())
As = [str(input().strip()) for _ in range(N)]

S = '1' + S
lenS = len(S)

dp = [0] * lenS 
dp[0] = 1

for i in range(1, lenS):
    if dp[i - 1] == 1:
        for A in As:
            if (i + len(A) <= lenS) and (S[i:i+len(A)] == A):
                dp[i + len(A) - 1] = 1
                
# print(dp)
print(dp[lenS - 1])