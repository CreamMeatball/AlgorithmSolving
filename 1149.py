# N = int(input())

# sum = 0
# RGB = [1, 1, 1]

# for i in range(N):
#     house = list(map(int, input().split()))
#     for i in range(3):
#         if RGB[i] == 0:
#             house[i] = 1001
#     min_house_index = house.index(min(house))
#     sum += house[min_house_index]
#     RGB = [1, 1, 1]
#     RGB[min_house_index] = 0

# print(sum)

from collections import deque

N = int(input())

house = deque()
for _ in range(N):
    house.append(list(map(int, input().split())))

# 풀이 방식의 핵심 개념은
# i 번째의 R, G, B 3개에 대해, 각각 i-1 번째의 최소값과 현재의 i 번째 값을 더한 값 중 최소값을 구하는 것이다.
# 예를 들어 i 번째 일 때, i-R + min((i-1)-G, (i-1)-B) 를 구하고, 이와 같은 방식을 i-G와 i-B 에 대해서도 진행한다는 것.
# 이렇게 되면, i-R은 i단계에서 R을 선택했을 때의 최소값, i-G는 i단계에서 G를 선택했을 때의 최소값, i-B는 i단계에서 B를 선택했을 때의 최소값이 된다.
# 맨 위 코드처럼 당장 최소값을 구하지 않고, 이런 방식을 사용하는 이유는
# 현재 단계의 최소값을 고른 뒤, 막상 다음 단계를 고를 때 더 최적의 값을 고르지 못하게 되어 최적의 최소값이 아니게 될 수도 있기 때문이다.
# 예를 들어
# 24 40 83
# 10 99 99
# 이럴 수도 있기 때문.
# 결국 이 방식을 사용하게 되면, 코드 상으론 i번째에서 i-1번째 값을 고려하는 것이지만,
# 개념적으론 i-1번째에서 다음 단계인 i번째 값까지 고려하여 여러 케이스를 계산해놓는 개념인 것이다.
# 그리고 구한 값을 dp에 덮어씌워서 누적시킨다.
# 값을 덮어씌워 이전까지의 최적의 최소값을 저장해나감으로써, 알고리즘 상 반복문 내에서 바로 한 단계 전의 값만 참조하면 되게끔 하는 것도 핵심.

dp = [[0] * 3 for _ in range(N)]

dp[0] = house[0]

for i in range(1, N):
    dp[i][0] = house[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = house[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = house[i][2] + min(dp[i-1][0], dp[i-1][1])
    
print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))

