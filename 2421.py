N = int(input())

# 에라토스테네스의 체
MAX_VAL = 10**6 # 최대: 999 + 999 해서 999,999
is_prime = [True] * MAX_VAL
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX_VAL**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX_VAL, i):
            is_prime[j] = False

dp = [[0] * (N + 1) for _ in range(N + 1)] # i: 첫째 저금통, j: 둘째 저금통

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == 1 and j == 1:
            continue
        
        current_num = int(str(i) + str(j))
        bonus = 1 if is_prime[current_num] else 0 # 두 수를 이었을 때 수가 소수가 되면 +1
        
        candidates = []
        if i > 1:
            candidates.append(dp[i-1][j])
        if j > 1:
            candidates.append(dp[i][j-1])
            
        if candidates:
            dp[i][j] = max(candidates) + bonus

print(dp[N][N])