import sys

input = sys.stdin.readline

N = int(input().rstrip())
diff = [0] * 100005

# 변화 시작점과 변화 끝점만 기록해서 계산하는 효율적 방식
# 주로 Imos(이모스) Method 라고 많이 부른다고 함.
# 이모스 메소드는 '차이'를 기록하는 차분 배열 기법을 이용하여 구현.

for _ in range(N):
    start, end = input().split()
    sy, sm = map(int, start.split('-'))
    ey, em = map(int, end.split('-'))
    
    s_idx = (sy - 2000) * 12 + (sm - 1) # 년을 월 단위로 바꿔서 사용
    e_idx = (ey - 2000) * 12 + (em - 1) # 년을 월 단위로 바꿔서 사용
    
    diff[s_idx] += 1
    diff[e_idx + 1] -= 1

max_friends = -1
best_idx = 0
current_friends = 0

for i in range(100000):
    current_friends += diff[i]
    if current_friends > max_friends: # >= 가 아닌 > 로 함으로써 자연적으로 같은 max값이면 더 앞선 시기를 정답으로 하게끔 설정.
        max_friends = current_friends
        best_idx = i

ans_y = (best_idx // 12) + 2000
ans_m = (best_idx % 12) + 1

print(f"{ans_y:04d}-{ans_m:02d}")
