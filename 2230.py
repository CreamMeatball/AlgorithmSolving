import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

As = [int(input().rstrip()) for _ in range(N)]

As.sort()

min_gap = float('inf')

left = 0
right = 1

# while left < right:
# 처음부터 gap이 M보다 크거나 같은 경우에, left +1 되어 left = right 가 되어 바로 중단되게 되는 문제가 있음.
while left < N and right < N: # l이랑 r이랑 겹쳐도 상관없음.
    current_gap = As[right] - As[left]
    # print(f"l: {left}({As[left]}), r: {right}({As[right]}). current_gap: {current_gap}")
    if current_gap < M:
        if (right + 1) < len(As):
            right += 1
        else:
            left += 1
    else: # M보다 크거나 같다
        min_gap = min(min_gap, current_gap)
        left += 1
    # print(f"min_gap: {min_gap}")
        
print(min_gap)