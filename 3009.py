point = [list(input().split()) for _ in range(3)]

for i in range(2):
    if point[0][i] == point[1][i]:
        print(point[2][i], end=' ')
    elif point[0][i] == point[2][i]:
        print(point[1][i], end=' ')
    else:
        print(point[0][i], end=' ')