N, L, R, X = map(int, input().split())
problems = list(map(int, input().split()))

answer = 0

# 각 problem의 사용 유무를 0/1로 계산
# ex) 0101 -> 0번째, 2번째 problem을 사용한다는 뜻

for bit in range(1, 1 << N): # 이것만으로 1개짜리 조합부터 N개짜리 조합까지 모든 조합을 탐색함. 비트 shift를 이용한 효율적 탐색.
    total_sum = 0
    count = 0
    min_diff = float('inf')
    max_diff = 0

    for i in range(N):
        if bit & (1 << i):
            count += 1
            total_sum += problems[i]
            min_diff = min(min_diff, problems[i])
            max_diff = max(max_diff, problems[i])
    
    if (count >= 2) and (L <= total_sum <= R) and ((max_diff - min_diff) >= X):
        answer += 1

print(answer)
