N = int(input())
tree = []
for _ in range(N):
    tree.append(int(input()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

interval = []

for i in range(N - 1):
    interval.append(tree[i+1] - tree[i])
    
# for i in range(len(interval) - 1):
#     for j in range(len(interval) - 1 - i):
#         interval[j] = gcd(interval[j], interval[j+1])

# 1번째간격과 2번째간격의 gcd, 1번째간격과 3번째간격의 gcd, ... , 2번째간격과 3번째간격의 gcd, ... 이렇게 다 해줄 필요 없이 (1*2*3*...*N번 연산)
# 1번째간격과 2번째간격의 gcd를 구하고, 그 값과 3번째간격의 gcd를 구하고..
# 이런 식으로 1번씩만 처리하면 됨 (N번 연산)

for i in range(len(interval) - 1):
    interval[i+1] = gcd(interval[i], interval[i+1])
    # 좌항 인덱스를 i+1 로 잡음으로써 방금의 연산 결과를 다음 순서의 대상으로 사용할 수 있음
    
# 또는
# g = interval[0]
# for i in range(1, len(interval)):
#     g = gcd(g, interval[i])
# 이런 방식으로도 가능
        
print((tree[-1] - tree[0]) // interval[-1] + 1 - N)

    

