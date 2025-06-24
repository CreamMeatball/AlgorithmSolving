import sys

input_ = sys.stdin.readline

N, T = map(int, input_().rstrip().split())

chapters = {}
for i in range(1, N + 1):
    chapters[i] = list(map(int, input_().rstrip().split())) # 드는 시간, 점수
    
# 물건을 쪼갤 수 없는 배낭(KnapSack) 문제

dp = [[0] * (T + 1) for _ in range(N + 1)]
# 행: 물건 순번
# 열: 가방 무게 제한

for chapter in range(1, N + 1):
    for timelimit in range(1, T + 1):
        weight, value = chapters[chapter]
        if weight > timelimit: # 필요 시간이 현재 잔여 시간 안에 불가능할 때
            dp[chapter][timelimit] = dp[chapter - 1][timelimit]
        else: # 가능할 때
            dp[chapter][timelimit] = max( \
                dp[chapter - 1][timelimit], # 현재 단원 공부를 안 하고 넘어간다 (이전 단원까지 봤을 때 값 유지)
                dp[chapter - 1][timelimit - weight] + value # 현재 단원을 공부한다 (이전 걸 공부 안 하고 이번 걸 새로 공부했을 때 더 이득이다)
            ) # 중 더 이득인 걸 고른다
            
# 테스트
# for d in dp:
#     print(d)
    
# 3 20
# 3 40
# 7 70
# 13 150    
    
print(dp[N][T])