N = int(input())
numbers = list(map(int, input().split()))

if N == 1:
    print('A')
    exit()

if N == 2:
    if numbers[0] == numbers[1]:
        print(numbers[0])
    else:
        print('A')
    exit()

# N이 3 이상일 때, 연립 방정식을 통해 a와 b를 구하기
x0, x1, x2 = numbers[0], numbers[1], numbers[2]

# x1 = a * x0 + b
# x2 = a * x1 + b

# x2 과 x1 간의 간격과
# x2 와 x0 간의 간격 간의 규칙을 찾기

# x2 - x1 = (a*x1 + b) - (a*x0 + b)
# = a(x1 - x0)

# 즉,
# x_n = x_n-1 * a + b 관계에서
# x_n - x_n-1 = a(x_n-1 - x_n-2)
# 라는 관계가 나옴.
# -> a = (x2 - x1) // (x1 - x0)

if x1 - x0 == 0: # 분모가 0이라서, 나눔이 불가하여 위의 식의 나눔을 통해 a를 구할 수 없는 경우
    # (a = 0, b = 0) 인 경우와 (a = 2, b = x1 * (a - 1)) 같은 경우가 있음 (경우가 여러가지)
    # 하지만 (a, b) 쌍은 여러가지가 나올 수 있어도, ax + b 의 값은 하나로 특정되기 때문에 가능.
    # 그래서 모든 원소의 값이 같으면 하나로 특정되기에 답이 나오고,
    # 그렇지 않으면 'B' 출력.
    is_all_same = True
    for i in range(N):
        if numbers[i] != x0:
            is_all_same = False
            break
    
    if is_all_same:
        print(x0)
        exit()
    else:
        print('B')
        exit()

if (x2 - x1) % (x1 - x0) != 0: # 정수 비율이 아닌 경우 (예제 입력 7 같은 경우)
    print('B')
    # print(3)
    exit()
        
# 여기까지 필터링 한 뒤,
# a = a = (x2 - x1) // (x1 - x0) 를 통해 a와 b 특정.
# 변수 3개에서 위 식을 통해 a를 하나로 특정할 수 있음. 무한대 범위의 a에 대해 모두 탐색할 필요가 없음.

a = (x2 - x1) // (x1 - x0)
b = x1 - x0 * a

# print(f"a: {a}, b: {b}")

# N >= 4 경우의 모든 잔여 원소들에 대해 찾은 규칙이 성립하는지 확인.
for i in range(1, N):
    if numbers[i] != numbers[i-1] * a + b:
        print('B')
        # print(4)
        break
else:
    print(numbers[-1] * a + b)