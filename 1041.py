# 개별적인 작은 주사위가 보일 수 있는 면의 개수는 최대 3개임
# 꼭짓점 부분: 3면
# 모서리 부분: 2면
# 그 외의 면 부분: 1면

N = int(input())
numbers = list(map(int, input().split()))

def getadjacent(numbers: list, n: int):
    if n == 1:
        return numbers
    elif n == 2:
        return [
            sum([numbers[0], numbers[4]]),
            sum([numbers[0], numbers[3]]),
            sum([numbers[0], numbers[2]]),
            sum([numbers[0], numbers[1]]),
            sum([numbers[3], numbers[4]]),
            sum([numbers[2], numbers[4]]),
            sum([numbers[1], numbers[2]]),
            sum([numbers[1], numbers[3]]),
            sum([numbers[1], numbers[5]]),
            sum([numbers[2], numbers[5]]),
            sum([numbers[3], numbers[5]]),
            sum([numbers[4], numbers[5]]),
        ]
    elif n == 3:
        return [
            sum([numbers[0], numbers[1], numbers[2]]),
            sum([numbers[0], numbers[2], numbers[4]]),
            sum([numbers[0], numbers[3], numbers[4]]),
            sum([numbers[0], numbers[1], numbers[3]]),
            sum([numbers[5], numbers[2], numbers[4]]),
            sum([numbers[5], numbers[3], numbers[4]]),
            sum([numbers[5], numbers[1], numbers[3]]),
            sum([numbers[5], numbers[1], numbers[2]]),
        ]

minOfAdj3 = min(getadjacent(numbers, 3))
minOfAdj2 = min(getadjacent(numbers, 2))
minOfAdj1 = min(getadjacent(numbers, 1))

if N == 1:
    print(sum(numbers) - max(numbers))
elif N == 2: # 3면x4 + 2면x4
    print(minOfAdj3*4 + minOfAdj2*4)
else:
    # N = 3) 3면x4 + 2면x(4x1+3x2) + 1면x(1x5+1x4)
    # N = 4) 3면x4 + 2면x(4x2+3x3) + 1면x(4x5+2x4)
    # N = 5) 3면x4 + 2면x(4x3+3x4) + 1면x(9x5+3x4)
    # ...
    # 3면x4 + 2면x(4*(N-2)+4*(N-1)) + 1면x((N-2)**2*5+(N-2)*4)
    print(minOfAdj3*4 + minOfAdj2*(4*(N-2)+4*(N-1)) + minOfAdj1*(5*(N-2)**2+4*(N-2)))