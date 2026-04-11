import sys

input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

# 우리가 구해야 하는 값은 각 k k에 대해 S k = ∑ j = 1 k ( k + 1 − j ) 2 a j S k ​ = j=1 ∑ k ​ (k+1−j) 2 a j ​ 입니다.
# 여기서 제곱을 전개하면 ( k + 1 − j ) 2 = ( k + 1 ) 2 − 2 ( k + 1 ) j + j 2 (k+1−j) 2 =(k+1) 2 −2(k+1)j+j 2 이므로,
# S k = ( k + 1 ) 2 ∑ j = 1 k a j − 2 ( k + 1 ) ∑ j = 1 k j a j + ∑ j = 1 k j 2 a j S k ​ =(k+1) 2 j=1 ∑ k ​ a j ​ −2(k+1) j=1 ∑ k ​ ja j ​ + j=1 ∑ k ​ j 2 a j ​ 가 됩니다. 
# 즉 매번 필요한 건 딱 3개 누적합입니다. 
# 1. P 1 ( k ) = ∑ j = 1 k a j P 1 ​ (k)=∑ j=1 k ​ a j ​ 
# 2. P 2 ( k ) = ∑ j = 1 k j a j P 2 ​ (k)=∑ j=1 k ​ ja j 
# 3.​ P 3 ( k ) = ∑ j = 1 k j 2 a j P 3 ​ (k)=∑ j=1 k ​ j 2 a j ​

# 예시
# 4
# 1 2 3 4

# 예시에서, 
# $a = (1, 2, 3, 4)$ 이므로, 
# $1^{2} \cdot a_{1} = 1$, 
# $2^{2} \cdot a_{1} + 1^2 \cdot a_{2} = 6$, 
# $3^{2} \cdot a_{1} + 2^{2} \cdot a_{2} + 1^{2} \cdot a_{3} = 20$, 그리고 
# $4^{2} \cdot a_{1} + 3^{2} \cdot a_{2} + 2^{2} \cdot a_{3} + 1^{2} \cdot a_{4} = 50$ 이다.


# 그냥 단순 방식으로 하면
# S1 은 1개 더함
# S2 는 2개 더함
# ...
# SN 은 N개 더함

# 이니까 1 + 2 + ... + N = N(N + 1)/2 --> O(N^2) 이 됨.

# 그래서 3개 누적합에 대해 사전 계산을 해놓으면
# O(N) 으로 풀 수 있음.

s1 = 0
s2 = 0
s3 = 0
result = []

for k in range(1, N + 1):
	x = a[k - 1]
	s1 += x
	s2 += k * x
	s3 += k * k * x
	kp1 = k + 1
	value = kp1 * kp1 * s1 - 2 * kp1 * s2 + s3
	result.append(str(value))

print(" ".join(result))