import sys
input = sys.stdin.readline

T = int(input().strip())
k = int(input().strip())

# '유한' 동전 DP 문제.
# 무한 동전일 때랑 좀 다름.

coins = [tuple(map(int, input().split())) for _ in range(k)]
# coins: [(p1, n1), (p2, n2), ..., (pk, nk)]

dp = [0] * (T + 1)
dp[0] = 1

for p, n in coins:
    # 같은 동전 종류를 여러 번 쓰더라도 '이전 상태'만을 참조하도록 j를 내림차순 순회
    for j in range(T, -1, -1):
        # 이 금액 j에서 이 동전을 최대 몇 개까지 쓸 수 있는지
        max_take = min(n, j // p)
        for t in range(1, max_take + 1):
            dp[j] += dp[j - t * p]

print(dp[T])