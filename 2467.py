# from itertools import combinations

N = int(input())
liquids = list(map(int, input().split()))

# selected = list(combinations(liquids, 2))

# best = 1000000000
# a, b = 1000000000, 1000000000
# for s in selected:
#     if abs(sum(s) - 0) < abs(best - 0):
#         best = sum(s)
#         a, b = s[0], s[1]
# print(a, b)

# 메모리 초과 남

# 투 포인터 알고리즘
# 조합을 구하는 경우에 O(N)만 쓰고 모든 조합을 다 해 볼 수 있음

l, r = 0, N - 1
best = float('inf')
a, b = None, None

# 원래 오름차순으로 정렬해줘야 아래 알고리즘이 맞지만
# 입력에서 애초에 오름차순으로 주기 때문에 sort 안해줘도 됨
while l < r:
    sum_ = liquids[l] + liquids[r]
    if abs(sum_) < best:
        best = abs(sum_)
        a, b = liquids[l], liquids[r]
    if sum_ < 0: # 0에 가깝기 만드는 게 목적이기 때문에, 합이 0보다 작아졌다면 현재의 왼쪽값보다 더 큰 값으로 옮김
        l += 1
    else: # 0에 가깝기 만드는 게 목적이기 때문에, 합이 0보다 커졌다면 현재의 오른쪽값보다 더 작은 값으로 옮김
        r -= 1
        
print(a, b)