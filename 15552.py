import sys

T = int(sys.stdin.readline().rstrip())
# 개행문자(\n)가 같이 입력 받아지며, string 타입으로 받아진다고 함.
A = []
B = []
for _ in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    A.append(a)
    B.append(b)

# 행 단위로 넘어가는 for 문 사용하지 않고 list 내부값 반복해서 print 하기.
# zip() 함수는 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수.
print('\n'.join(str(a + b) for a, b in zip(A, B)))