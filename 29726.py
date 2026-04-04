import sys

input = sys.stdin.readline

# 시그마 쭉 전개해보면
# "중간에 어떤 걸 삭제하든, 남긴 수열의 [A_마지막 - A_처음]이 된다"는 걸 알 수 있음

# 중간에 뭘 빼냐가 다른 데 영향을 줄까봐 종속적인 것처럼 보일 수 있어 머리 아파보이는데
# 사실 중간에 뭘 빼도 나머지는 독립적으로 있음.


# ==> 첫 index와 마지막 index만 생각해서 둘 간의 차이가 가장 커질 때를 찾으면 됨 (중간에 숫자가 뭐가 있든 상관 X)

N, M = map(int, input().split())
A = list(map(int, input().split()))

# --> 근데 첫 index와 마지막 index의 best pair를 찾으려면 일반적인 방법으로는 O(N^2)이니까
# 더 효율적인 방법 고려

d = N - 1 - M # distance. 최소한으로 벌어져야 하는 거리.
minv = A[0]
result = A[d] - minv

# 효율적 방법:
# 최저점(시작index)과 최고점(끝index)만 찾으면 되는 거임.
# 이를 위해, O(N)으로 한 번만 돌면서
# 역대 최저가, 와 역대 최고가. 이렇게 두 개를 찾음 (다만 distance 범위 안에서. 이게 좀 까다로움)

# j가 '끝index'라고 할 때
# 시작index는 '역대 최저가'이고 (그래서 이후 탐색을 통해 탐색 범위가 지나갔어도 역대 최저가가 유지될 수 있음)
# 'j - d'를 '임시 시작index'라고 한 뒤
# '끝index - 임시시작index' 해봄. 이 때 이게 역대 최고차이라면
# 그 때의 값을 지금까지의 정답이라고 함.

for j in range(d + 1, N):
    minv = min(minv, A[j - d]) # distance 접목 핵심. 이를 통해 minv는 j(끝index)로부터 최소한 distance만큼은 멀리 떨어져있는 값들 중에서만 minv가 갱신됨.
    endv = A[j]
    result = max(result, endv - minv)
    
# maxv 라는 변수 만들어놓고
# 역대 최저가 minv, 역대 최고가 maxv 탐색-갱신 해주면 되는 거 아니냐 할 수 있는데
# distance 때문에 안됨. 단순 역대 최저/고가 갱신 및 그 둘의 차이로 결과를 내면 distance가 고려되지 않은 오답임.

# or

# for i in range(0, N - d):
#     minv = min(minv, A[i]) # i: start
#     endv = A[i + d] # i + d: end
#     result = max(result, endv - minv)
# 구현 관점만 다르고 동치임.

print(result)