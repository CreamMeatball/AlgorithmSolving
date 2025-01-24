import sys

input_data = sys.stdin.readline

T = int(input_data().rstrip())

for _ in range(T):
    K = int(input_data().rstrip())
    file_sizes = [0] + list(map(int, input_data().split()))
    dp = [[0] * (K+1) for _ in range(K+1)]
    # dp[i][j]를 i번째 파일부터 j번째 파일을 합쳤을 때 최솟값이라고 두고 푸는 것이다.
    # dp[1][2], dp[2][3], dp[3][4], ... dp[i][i+1]은 연속된 두 개의 파일을 합치는 것으로 파일 i와 i+1의 크기를 단순히 합친 것과 같다.
    # dp[1][4]와 같은 경우 dp[1][1]+dp[2][4], dp[1][2]+dp[3][4], dp[1][3]+dp[4][4] 다음과 같은 경우의 수가 나온다.
    # 즉, 위의 경우 중 최소값을 찾은 뒤 sum을 이용해 1번부터 4번 파일까지의 크기를 합하면 dp[1][4]값을 구할 수 있다.
    # https://velog.io/@seung_min/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-11066%EB%B2%88-%ED%8C%8C%EC%9D%BC-%ED%95%A9%EC%B9%98%EA%B8%B0
    
    