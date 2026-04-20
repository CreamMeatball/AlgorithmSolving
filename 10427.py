import sys

input = sys.stdin.readline

T = int(input().rstrip())

# 페널티 = (고른 M개의 숫자 중 최댓값 × M) - (고른 M개의 숫자의 합)
# 인데
# (고른 M개의 숫자의 합)이 최대한 클 수록 좋은 거니까
# 가장 best는, "어떠한 최대값을 골랐을 때, 그 최대값에 가깝게 가장 큰 숫자들로만 M-1 개를 뽑기"인 경우가 best임.
# --> '정렬'한 뒤에, '슬라이딩 윈도우' 써서 '연속된 M개'로 페널티 계산해서 가장 낮은 페널티가 되는 경우를 찾으면 됨.

for _ in range(T):
    data = list(map(int, input().split()))
    N = data[0]
    A = data[1:]
    
    # 정렬
    # M개의 빚을 고를 때, '가장 큰 값'을 기준으로 삼기 위해 오름차순 정렬.
    # 이렇게 하면 연속된 M개의 윈도우를 잡았을 때 맨 오른쪽 원소가 무조건 최댓값이 됨.
    A.sort()
    
    # 누적합
    P = [0] * (N + 1)
    for i in range(N):
        P[i + 1] = P[i] + A[i]
        
    answer = 0
    
    # 슬라이딩 윈도우
    # (M = 1일 때는 갚아야 할 추가 금액이 무조건 0이므로 탐색할 필요 없이 M = 2부터 시작)
    for M in range(2, N + 1):
        min_val = float('inf')
        
        # 배열에서 길이가 M인 윈도우를 슬라이딩하며 최소 추가 금액 탐색
        for k in range(M - 1, N):
            # k는 윈도우의 가장 오른쪽(최댓값) 인덱스
            # P[k + 1] - P[k - M + 1] 은 길이가 M인 윈도우 구간의 실제 합
            cost = A[k] * M - (P[k + 1] - P[k - M + 1])
            
            if cost < min_val:
                min_val = cost
                
        answer += min_val
        
    print(answer)
