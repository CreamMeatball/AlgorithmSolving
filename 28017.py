import sys

N, M = map(int, input().split())
times = []

for _ in range(N):
    times.append([int(x) for x in sys.stdin.readline().split()])
    
dp = [[0] * M for _ in range(N)]
dp[0] = times[0]

for i in range(1, N): # 게임 회차
    for j in range(M): # 각 무기를 선택했을 때
        prev = min(dp[i - 1][:j] + dp[i - 1][j + 1:]) # j 제외 (직전에 쓴 무기 안 써야하니)
        # 이게 반복문 돌려서 if j == ...: continue 하는 것보다 더 빠르다고 함.
        # 이론적 시간복잡도는 똑같은데 (반복문으로 M번 도나, index slicing된 리스트 내의 min을 찾기 위해 M번 순회하나)
        # 파이썬의 min() 이랑 index slicing의 동작이 C언어로 구현되어 있다고 함.
        # 그래서 반복문 돌면서 파이썬 코드 반복 실행하는 것보다 실제 동작 속도가 더 빠르다고 함.
        dp[i][j] = prev + times[i][j] # bottom to top
print(min(dp[N - 1]))