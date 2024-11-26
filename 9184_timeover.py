# def w(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#     if a > 20 or b > 20 or c > 20:
#         return w(20, 20, 20)
#     if a < b and b < c:
#         return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
#     return w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

def w_dynamic(a, b, c):
    dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
    if a > 20 or b > 20 or c > 20:
        a = b = c = 20
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    for i in range(21):
        for j in range(21):
            for k in range(21):
                if i <= 0 or j <= 0 or k <= 0:
                    dp[i][j][k] = 1
                    continue
                if i < j and j < k:
                    dp[i][j][k] = dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][k]
                    continue
                dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1]
                    
    return dp[a][b][c]


while(True):
    inputdata = list(map(int, input().split()))
    if inputdata == [-1, -1, -1]:
        break
    print(f"w({inputdata[0]}, {inputdata[1]}, {inputdata[2]}) = {w_dynamic(inputdata[0], inputdata[1], inputdata[2])}")
    