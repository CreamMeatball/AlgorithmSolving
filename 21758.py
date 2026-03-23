import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))

S = [0] * N # 누적합. 꿀의 양을 쭉 더해야하는건데, 매번 더하면 비효율적이니 미리 더해놓음(누적합)
S[0] = arr[0]
for i in range(1, N):
    S[i] = S[i-1] + arr[i]

ans = 0

for i in range(1, N - 1):
    # 벌통이 맨 오른쪽인 경우. 벌1(맨왼쪽) - 벌2(i) - 벌통(맨오른쪽).
    ans = max(ans, 2 * S[N-1] - arr[0] - arr[i] - S[i])
    # 벌통이 맨 왼쪽인 경우. 벌통(맨왼쪽) - 벌1(i) - 벌2(맨오른쪽).
    ans = max(ans, S[N-1] - arr[N-1] - arr[i] + S[i-1])
    # 벌통이 중간에 있는 경우. 벌1(맨왼쪽) - 벌통(i) - 벌2(맨오른쪽).
    ans = max(ans, S[i] - arr[0] + S[N-1] - S[i-1] - arr[N-1])
    
# 누적합 역방향은 고려할 필요 없음.
# 꿀 계산할 때는 어떠한 순서는 왼쪽-->오른쪽으로 계산하면 됨.

print(ans)