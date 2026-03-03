import sys

input = sys.stdin.readline

dp = [[-1] * 16 for _ in range(16)]
dp[0][0] = 0

while True:
    line = input().split()
    if not line: # 개수 몇 개인지 안주어지고 중단점도 안주어져서 이런 식으로 처리.
        break
    
    w_stat, b_stat = map(int, line)

    for w in range(15, -1, -1): # 현재 고려 중인 플레이어 한 명을 백팀과 흑팀에 중복해서 넣는 실수를 방지하기 위해 뒤에서부터 계산 (공간 최적화된 배낭 문제와 같은 원리)
        for b in range(15, -1, -1):
            if dp[w][b] == -1:
                continue

            if w < 15:
                if dp[w+1][b] < dp[w][b] + w_stat: # 기존의 w+1 의 값보다, (w값 + w_stat) 이 더 클 경우, w+1 의 값을 (w값 + w_stat) 으로 갱신.
                    dp[w+1][b] = dp[w][b] + w_stat
            
            if b < 15:
                if dp[w][b+1] < dp[w][b] + b_stat:
                    dp[w][b+1] = dp[w][b] + b_stat

print(dp[15][15])
