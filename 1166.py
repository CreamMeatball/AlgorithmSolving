N, L, W, H = map(int, input().split())

# N: 작은 상자 개수
# L: 큰 상자의 길이
# W: 큰 상자의 너비
# H: 큰 상자의 높이

# 이진 탐색을 통해 최대 A값 찾기
left = 0.0
right = min(L, W, H)
# epsilon = 1e-7 # 충분히 작은 값으로 종료 조건 설정. 너무 작게 하면 시간 초과 남.

# while right - left > epsilon: # float 연산이라서 left < right 조건으로 하면 무한루프에 빠질 수 있음
# epsilon = 1e-7 하면 틀리고, 1e-8 하면 시간 초과 나서
# 다른 방식으로 루프 제한 걸기

for _ in range(1000):
    mid = (left + right) / 2
    count = (L // mid) * (W // mid) * (H // mid)
    
    if count >= N:  # 필요한 N개 수 이상 들어가는 경우
        left = mid
    else:
        right = mid 

print(right)