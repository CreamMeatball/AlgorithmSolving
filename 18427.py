import sys

input_ = sys.stdin.readline

N, M, H = map(int, input_().rstrip().split())

blocks = [[0]]
for _ in range(N):
    # blocks.append(list(map(int, input_().rstrip().split())))
    blocks.append([0] + list(map(int, input_().rstrip().split())))
    # 블럭을 쌓지 않고 다음 사람으로 넘기는 경우를 생각해야하므로, '[0] +' 을 꼭 해줘야 됨.
    
dp = [[0] * (H + 1) for _ in range(N + 1)]

for i in range(N + 1):
    dp[i][0] = 1

def TestPrint(a, b, block):
    print()
    print(f"[till index[{a}][{b}]. current block: {block}]")
    for i in range(a):
        print(*dp[i])
    for i in range(b + 1):
        print(dp[a][i], end=' ')
    print()

for i in range(1, N + 1):
    for j in range(1, H + 1):
        for weight in blocks[i]:
            if weight <= j:
                # dp[i][j] += dp[i - 1][j - weight]
                dp[i][j] = (dp[i][j] + dp[i - 1][j - weight]) % 10007
            # else:
            #     dp[i][j] = dp[i - 1][j]
            # 위 else 구문이 있으면, 그 다음 가지고 있는 블럭이 앞의 블럭에서 count한 개수를 덮어써버림.
            # TestPrint(i, j, weight)
                
# for d in dp:
#     print(d)

print(dp[N][H])