import sys
input = sys.stdin.readline

N = int(input())
blocks = input().strip()

dp = [float('inf')] * N
dp[0] = 0

for i in range(N):
    if dp[i] == float('inf'):
        continue
    
    target = ''
    if blocks[i] == 'B':
        target = 'O'
    elif blocks[i] == 'O':
        target = 'J'
    elif blocks[i] == 'J':
        target = 'B'
        
    for j in range(i + 1, N):
        if blocks[j] == target:
            cost = (j - i)**2
            if dp[j] > dp[i] + cost:
                dp[j] = dp[i] + cost

if dp[N-1] == float('inf'):
    print(-1)
else:
    print(dp[N-1])