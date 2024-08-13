import sys

N = int(sys.stdin.readline().rstrip())
numbers = []

for i in range(N):
    numbers.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
# key=lambda x: (x[0], x[1])은 x[0]을 기준으로 오름차순 정렬하고, x[0]이 같은 경우 x[1]을 기준으로 오름차순 정렬한다는 뜻.
numbers.sort(key=lambda x: (x[0], x[1]))
# lambda 는 익명함수. (lambda x: x+1)(1) 은 2 라는 값이 반환됨.

for i in range(N):
    print(numbers[i][0], numbers[i][1])