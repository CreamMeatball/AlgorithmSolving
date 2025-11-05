# PyPy3 for avoiding time exceed

N, M = map(int, input().split())
woks = list(map(int, input().split()))

# 한 번의 요리로 만들 수 있는 모든 경우의 수
cook_options = set()

# 웍 1개를 사용하는 경우
for w in woks:
    if w <= N: # N그릇을 초과하는 웍은 의미 없음
        cook_options.add(w)

# 웍 2개를 사용하는 경우
for i in range(M):
    for j in range(i + 1, M):
        total = woks[i] + woks[j]
        if total <= N: # N 그릇을 초과하는 조합은 의미 없음
            cook_options.add(total)
            
cook_list = list(cook_options)

dp = [float('inf')] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    for cook_amount in cook_list:
        if i >= cook_amount and dp[i - cook_amount] != float('inf'): # 문제의 특수성 때문에 꼭 dp[i - cook_amount] != float('inf') 체크해줘야 함.
            dp[i] = min(dp[i], dp[i - cook_amount] + 1)

# print(dp[1:])

if dp[N] == float('inf'): # 불가능한 경우
    print(-1)
else:
    print(dp[N])