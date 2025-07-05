# PyPy3 because of time exceed

N, M = map(int, input().split())
S = set()
if M > 0:
    S = set(map(int, input().split()))

min_ = float('inf')

# limit = min(1001, N ** 3)
limit = 1002
# limit = min(1002, N ** 3) # 얘는 또 틀리네
# 아니 왜 1001 까지가 아니라 1002 까지 해야 맞음??
# ㄴ 만약 S = {1, 2, 3, ... , 1000} 으로 싹 다 포함할 경우,
#   최소값을 만드려면 1001 을 써야하기 때문. 그렇기 때문에 range(1, 1002) 까지 돌려야한다.

for i in range(1, limit):
    if i in S:
        continue
    for j in range(i, limit):
        if j in S:
            continue
        for w in range(j, limit):
            if w in S:
                continue
            min_ = min(min_, abs(N - i * j * w))
            
            if min_ == 0: # 최적화
                break
        if min_ == 0:
            break
    if min_ == 0:
        break
            
print(min_)