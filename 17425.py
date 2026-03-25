# PyPy3

import sys

input = sys.stdin.readline

T = int(input().rstrip())

# 1. f(x)를 미리 효율적으로 계산해놓고,
# 2. g(x)를 누적합으로 계산해놔야 됨.

MAX = 1000000

f = [0] * (MAX + 1)
g = [0] * (MAX + 1)

# f를 효율적으로 구하기 위해 아래와 같은 방법 사용.
# 에라토스테네스의 체의 원리를 응용해서 다른 목적으로 활용.

# 예를 들어 1은 모두의 약수이니
# 루프 돌면서 모든 x에 대해 f(x)에 1씩 추가해줌.

# 이렇게 하면 어떤 수 x의 약수가 무엇인지를 식별하는 과정이 빠져서 압도적으로 빠름.
# 시간 복잡도: O(N * sqrt(N)) vs O(N * logN)
# (약수 찾는 알고리즘 시간복잡도: O(sqrt(N)). 왜냐면 어떤 수 x의 약수를 찾을 때 sqrt(x)까지만 탐색해서 찾으면 그 이후로는 pair값이기 때문에)

for i in range(1, MAX + 1):
    for j in range(i, MAX + 1, i):
        f[j] += i

for i in range(1, MAX + 1):
    g[i] = g[i - 1] + f[i]

# for _ in range(T):
#     N = int(input().rstrip())
#     print(g[N])

# N이 최대 10만까지라서, print()를 매 번 찍는 것도 병목 걸린댄다. 합산 1초 정도.

answers = []
for _ in range(T):
    N = int(input().rstrip())
    answers.append(str(g[N]))

print('\n'.join(answers))
