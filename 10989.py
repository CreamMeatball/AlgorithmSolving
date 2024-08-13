import sys

N = int(sys.stdin.readline().rstrip())

numbers = [0 for _ in range(10001)]

for _ in range(N):
    numbers[int(sys.stdin.readline().rstrip())] += 1

for i in range(1, len(numbers)):
    # print(f'{i}\n' * numbers[i], end='') if numbers[i] != 0 else None
    # 위 코드가 오히려 메모리를 약간 더 쓰나 봄.
    if numbers[i] != 0:
        for _ in range(numbers[i]):
            print(i)