import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
buckets = []

for _ in range(N):
    g, x = map(int, input().rstrip().split())
    buckets.append((x, g)) # (위치, 얼음 양)

buckets.sort()

# 슬라이딩 윈도우
# 그냥 매 반복마다 백곰 위치마다의 범위 내 양동이 값 일일이 계산해줘도 되는데
# 비효율적이라서 슬라이딩 윈도우 사용

left = 0
total_ice = 0
max_ice = 0

for right in range(N):
    total_ice += buckets[right][1] # 현재 양동이의 얼음 추가
    
    # 윈도우의 너비가 2*K를 초과하면 왼쪽 포인터 이동
    while left < right and buckets[right][0] - buckets[left][0] > 2*K:
        total_ice -= buckets[left][1] # 범위를 벗어난 양동이의 얼음 제거
        left += 1
    
    max_ice = max(max_ice, total_ice)

print(max_ice)