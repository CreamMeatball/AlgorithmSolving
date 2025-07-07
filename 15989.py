import sys

input_ = sys.stdin.readline

T = int(input_().rstrip())

ns = list()
for _ in range(T):
    ns.append(int(input_().rstrip()))
    
max_n = max(ns)
    
dp = [0] * (max_n + 1)
dp[0] = 1

for current_num in range(1, 4):
        for i in range(1, max_n + 1):
            if current_num <= i:
                dp[i] += dp[i - current_num]
                
# print(dp)

for n in ns:
    print(dp[n])