A = input()
B = input()

lenA = len(A)
lenB = len(B)

dp = []
for i in range(lenA):
    dp.append([0] * (lenB))
    
# A의 각 문자에 대해 B 전체를 다 순회하며 A의 문자와 같은 게 있는 경우 숫자를 누적
# 그리고 그 누적된 숫자를 dp에 저장
# 왜냐면 A의 각 문자를 B에서 매칭할 때, 언제 대응될지를 모름. A의 첫 문자를 B의 거의 끝에서 대응시킬 수도 있음.
# 이후 다음 A의 문자에 대해 같은 과정을 반복하는데,
# 이전에 순회하며 저장한 이전 순서의 dp의 값을 이용함.

# 2차원 (n x n) dp인 것.

for i in range(lenA):
    for j in range(lenB):
        if A[i] == B[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            if i == 0 and j == 0:
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = dp[i][j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                # 줄을 순회할 때 이전의 dp행의 값이 큰 지, 이번 dp행의 바로 전 값이 더 큰 지 비교.
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
# print(dp)
print(dp[lenA - 1][lenB - 1])