N = int(input())
lines = []

for _ in range(N):
    lines.append(list(map(int, input().split())))
    
# 교차한다는 건 무엇이냐.
# 어떠한 A 줄과 B 줄이 있을 때
# A 줄의 시작 위치가 B 줄의 시작 위치보다 작은데
# A 줄의 도착 위치가 B 줄의 도착 위치가 큰 경우,
# 그리고 반대로 A 줄의 시작 위치가 B 줄의 시작 위치보다 큰데
# A 줄의 도착 위치가 B 줄의 도착 위치보다 작은 경우.
# 를 뜻한다.

sorted_lines = sorted(lines, key=lambda x: (x[0], x[1]))
# print(sorted_lines)

dp = [0] * N

for i in range(N):
    dp[i] = N - 1
    # N 이 아닌 N - 1인 이유 : 줄을 안 겹치게 할 때 최대로 많은 줄을 없애는 경우가 N - 1이기 때문.
    # 8개 줄이 있을 때 아무리 줄을 많이 없애도 7개까지 없애는 게 최대임.
    for j in range(i):
        # i 번째 순서에서, 이전까지 줄들을 순회하며 교차되지 않는 줄인지 판단.
        # 교차되지 않는 줄인 경우, 처음 초기화 된 값 N - 1(제거해야하는 줄 수)에서 1 차감.
        if sorted_lines[j][1] < sorted_lines[i][1]:
            dp[i] = min(dp[i], dp[j] - 1)
            
# print(dp)

print(min(dp))