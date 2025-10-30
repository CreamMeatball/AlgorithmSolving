N = int(input())

dp = [0] * (N + 1) # dp[i]: i번 눌렀을 때 A의 최대 개수

# 붙여넣기를 처음 하기 위해선, 총 3번의 입력이 필요하고
# 한 번 붙여넣기를 시작한 이후로는, A 한 개 입력하기를 할 이유가 없음.
# 그 때부터는 계속 붙여넣기만 하는 것.

for i in range(1, N + 1):
    insertA = dp[i - 1] + 1
    pasteA = 0
    if i >= 4:
        for j in range(1, i - 2):
            pasteA = max(pasteA, dp[j] + dp[j] * (i - (j + 2))) # (j+3) 번째 시점에, j일 때의 A 개수를 붙여넣기. 그리고 그걸 j+3번째부터 i번째까지 Ctrl+V만 반복.
            
    dp[i] = max(insertA, pasteA)
    
# print(*dp)
print(dp[N])