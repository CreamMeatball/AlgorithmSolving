N = int(input())
leftbig = list(map(int, input().split()))

# 4
# 2 1 1 0
# > 3 1 0 2

position = [0] * N

for i in range(N):
    for j in range(N):
        if leftbig[i] == 0 and position[j] == 0:
            position[j] = i + 1
            break
        elif position[j] == 0:
            leftbig[i] -= 1

print(' '.join(map(str, position)))