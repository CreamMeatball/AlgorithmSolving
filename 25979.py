import sys

input = sys.stdin.readline

N = int(input().rstrip())
# 00:00:00 ~ 23:59:59는 총 86,400개의 1초 구간 (마지막 초 지점: 86,399)
MAX_T = 86400
diff = [0] * (MAX_T + 1)

A = []
for _ in range(N):
    A.append(input().split())


# 3가지 요소를 쓰는 문제
# 1. 누적합
# 2. 이모스 법
# 3. 슬라이딩 윈도우
    

# 유형 1 질의 처리: 차분 배열 업데이트

# Imos Method (이모스 법) - 이게 핵심
# "N개의 위치에 1을 더해라, 그리고 그걸 M번 수행하라. 이에 대한 prefix sum 배열 만들어라." 이런 경우에
# O(N * M)의 시간복잡도가 발생하는데
# 시작점과 끝점에만 표시해놓고
# 그 누적된 시작점,끝점 값들을 통해 prefix sum으로 만들면
# O(N + M)의 시간복잡도로 prefix sum 만들 수 있음

for i in range(N - 1):
    q = A[i]
    t1, t2 = q[1], q[2]
    
    # 시간 문자열을 초(second) 단위로 변환
    start = int(t1[:2]) * 3600 + int(t1[3:5]) * 60 + int(t1[6:])
    end = int(t2[:2]) * 3600 + int(t2[3:5]) * 60 + int(t2[6:])
    
    diff[start] += 1
    diff[end] -= 1

# 유형 2 질의 처리: 비교할 구간 길이 L 계산
t_len = A[-1][1]
L = int(t_len[:2]) * 3600 + int(t_len[3:5]) * 60 + int(t_len[6:])

# 차분 배열 복구하여 각 1초 구간의 실제 값 계산
curr = 0
for i in range(MAX_T):
    curr += diff[i]
    diff[i] = curr

# 구간 합을 빠르게 구하기 위한 누적합 배열 생성
prefix_sum = [0] * (MAX_T + 1)
for i in range(MAX_T):
    prefix_sum[i + 1] = prefix_sum[i] + diff[i]

# 슬라이딩 윈도우로 길이가 L인 구간 중 최대합 탐색
max_val = 0
for i in range(MAX_T - L + 1):
    curr_sum = prefix_sum[i + L] - prefix_sum[i]
    if curr_sum > max_val:
        max_val = curr_sum

print(max_val)
