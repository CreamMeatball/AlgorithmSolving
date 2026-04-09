import sys

input = sys.stdin.readline

N = int(input().rstrip())

As = list(map(int, input().split()))

Ps = [0] * (N + 1)

for i in range(1, N + 1):
    Ps[i] = Ps[i - 1] + As[i - 1]
    
# 각 숫자의 첫 번째 위치와 마지막 위치 기록하기 (효율화)
# 이 메소드 덕분에 이중 반복문 상에서 시간 초과 안 나게 할 수 있음 (N = 20만)
first_pos = {} # {숫자: 첫_인덱스}
last_pos = {}  # {숫자: 마지막_인덱스}

for idx, val in enumerate(As):
    if val not in first_pos:
        first_pos[val] = idx
    # 계속 갱신하면 결국 마지막 위치가 남음
    last_pos[val] = idx
    
# O(N) 시간 복잡도로
# 어떠한 한 숫자의 처음 출현지점과 마지막 출현지점을 기록해놓음.
# (숫자 종류 N' 개에 대한 시작점과 끝점을 기록)

# 이후 이것만 가지고 1중 반복문 돌려서
# 어떠한 한 숫자의 처음 출현지점과 마지막 출현지점까지의 누적합을 계산.
# (다른 출현 지점에 대해서도 계산해봐야하는 거 아닌가 할 수 있는데
# 1 <= a 인 조건 상에서 최대값만 따지는 것이기에, 더 길이가 긴 배열이 누적합이 더 크거나 최소한 같음.
# O(N') (N' < N) 만큼의 시간복잡도로 각 숫자별 최대 누적합 구할 수 있음.
    
# * 파이썬 라이브러리로 쉽게 누적합 리스트 구할 수 있다고 함.
# from itertools import accumulate
# Ps = list(accumulate(As, initial=0))

max_sum = -1
max_count = 0

for val in first_pos:
    start = first_pos[val]
    end = last_pos[val]
    
    # 구간 합 계산 (Ps[end+1] - Ps[start])
    current_sum = Ps[end + 1] - Ps[start]
    
    if current_sum > max_sum:
        max_sum = current_sum
        max_count = 1
    elif current_sum == max_sum:
        max_count += 1

print(max_sum, max_count)