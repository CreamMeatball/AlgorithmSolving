T = int(input())

for _ in range(T):
    iterableNumber, S = map(str, input().split())
    for a in S:
        print(int(iterableNumber) * a, end='')
    print()