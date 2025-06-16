# 개별적인 작은 주사위가 보일 수 있는 면의 개수는 최대 3개임
# 꼭짓점 부분: 3면
# 모서리 부분: 2면
# 그 외의 면 부분: 1면

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

if N == 1:
    print(sum(numbers) - numbers[-1])
elif N == 2: # 모두 3면씩 보임
    print(sum(numbers[:3]) * 8)
else:
    # N = 3) 3x8 + 2x(4x3) + 1x6
    # N = 4) 3x8 + 2x(8x3) + 1x(4x6)
    # N = 5) 3x8 + 2x(12x3) + 1x(9x6)
    # ...
    # 3면x8 + 2면x(N-2)*4*3 + 1면x(N-2)**2
    print(
        sum(numbers[:3]) * 8 + \
        sum(numbers[:2]) * (N - 2) * 4 * 3 + \
        sum(numbers[:1]) * (N - 2) ** 2
    )