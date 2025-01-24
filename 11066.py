import sys

input = sys.stdin.readline

T = int(input().rstrip())  # 테스트 케이스 수

for _ in range(T):
    K = int(input().rstrip())  # 장(파일) 개수
    files = list(map(int, input().split()))
    
    # 1) 누적 합(prefix sum) 배열 계산
    prefix_sum = [0] * (K+1)
    for i in range(1, K+1):
        prefix_sum[i] = prefix_sum[i-1] + files[i-1]
    
    # 2) dp 배열 초기화
    # dp[i][j] = i~j까지 합치는 최소 비용
    dp = [[0]*(K+1) for _ in range(K+1)]
    
    # 3) 구간의 길이 L에 대해 반복 (L=2부터 K까지)
    for L in range(2, K+1):  # 부분 파일의 길이
        for i in range(1, K-L+2):  # 구간 시작 인덱스
            j = i + L - 1  # 구간 끝 인덱스
            
            # dp[i][j]를 초기값으로 큰 수로 설정
            dp[i][j] = float('inf')
            
            # i~j 구간을 k를 기준으로 나누어 최소 비용 탐색
            for k in range(i, j):
                # 점화식
                # dp[i][j] = min(dp[i][k]+dp[k+1][j]+(파일크기의합(i∼j)))
                cost = dp[i][k] + dp[k+1][j] + (prefix_sum[j] - prefix_sum[i-1])
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    # 4) 최종 결과 출력 (1번부터 K번까지 합친 최소 비용)
    print(dp[1][K])

# 점화식 설계
# 모든 파일의 크기를 빠르게 합산하기 위해 누적 합(prefix sum) 배열을 사용한다.

# sum[i] = 1번 파일부터 i번 파일까지의 크기 합.
# 구간 (i, j)의 파일 총 크기 = sum[j] - sum[i-1] (단, sum[0] = 0으로 가정)
# 구간 i부터 j까지 합치는 방법은 구간을 나누는 기준점 k를 사이에 두고,
# (i ~ k) 구간과 (k+1 ~ j) 구간을 먼저 각각 합친 뒤, 최종적으로 두 결과물을 합치는 방식이다.

# 따라서 dp[i][j]를 구하기 위한 점화식은 아래와 같다.

# dp[i][j] = min(dp[i][k]+dp[k+1][j]+(파일크기의합(i∼j)))

# dp[i][k]: i~k 구간을 하나의 파일로 합치는데 필요한 최소비용
# dp[k+1][j]: k+1~j 구간을 하나의 파일로 합치는데 필요한 최소비용
# 파일크기의 합(i~j): 최종적으로 합쳐질 두 구간을 실제로 한 덩어리로 합치는 비용
# 이는 (sum[j] - sum[i-1])로 계산

# 초기값
# dp[i][i] = 0 (구간의 길이가 1이면 이미 단일 파일이므로 합칠 필요가 없어서 비용이 0)
# 계산 순서
# 구간의 길이(merge할 파일 수)가 짧은 것부터 점차 길게 확장하면서 dp[i][j]를 계산한다.
# 즉, 구간 길이 L = 2부터 K까지 순회하며, 각 구간 시작점 i와 j = i+L-1을 잡아 점화식에 따라 dp[i][j]를 갱신한다.