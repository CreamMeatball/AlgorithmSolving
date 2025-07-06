import math

S, K = map(int, input().split())

max_ = 0

# 최대한 중앙쪽의 수로 곱해야지만 곱했을 때 곱이 크니까.
# ex)
# 10 을 2개로 나누면
# 1 9 로 나누는 것보다, 5 5 로 나눴을 때 그 곱이 제일 크니.

result = 1

if K <= 0: # 여기서 K는 0 혹은 음수일 떄를 고려해줬는데, 테스트 해보니 안해줘도 통과됨. 고려해줘야 되는 거 아닌가 해서 질문 올려놓음.
    result = 0
else:
    s = S
    k = K
    for _ in range(K):
        current = math.ceil(s / k)
        result *= current
        # print(temp)
        s -= current
        k -= 1
    max_ = max(max_, result)
    
print(result)