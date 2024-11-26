def w_memo(a, b, c, memo):
    if (a, b, c) in memo:
        return memo[(a, b, c)]
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        result = w_memo(20, 20, 20, memo)
    elif a < b and b < c:
        result = w_memo(a, b, c - 1, memo) + w_memo(a, b - 1, c - 1, memo) - w_memo(a, b - 1, c, memo)
    else:
        result = (
            w_memo(a - 1, b, c, memo) + w_memo(a - 1, b - 1, c, memo) + w_memo(a - 1, b, c - 1, memo) - w_memo(a - 1, b - 1, c - 1, memo)
        )
    
    memo[(a, b, c)] = result
    return result

# 재귀는 유지하되,
# memoization 을 써서
# 이전 입력값을 통해 미리 계산했던 부분은 또 계산하지 않게끔
# ex) w(1, 1, 1) = 2 을 통해 1, 1, 1 을 계산했으면
# 그 다음 입력값들에서 w(1, 1, 1) 을 사용하는 경우 또 계산하지 않게끔
memo = {}
while True:
    inputdata = list(map(int, input().split()))
    if inputdata == [-1, -1, -1]:
        break
    a, b, c = inputdata
    print(f"w({a}, {b}, {c}) = {w_memo(a, b, c, memo)}")

