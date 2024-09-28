# 1 : 1
# 2 : 2 3 4 5 6 7
# 3 : 8 9 10 11 12 13 14 15 16 17 18 19
# 4 : 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37
# 5 : 38 39 40 41 42 ~ 61

# 더해지는 양 : 6 12 18 24 ...

N = int(input())

if N == 1:
    print(1)
else:
    layer = 1
    rear_number = 1
    while rear_number < N:
        rear_number += 6*layer
        layer += 1
    print(layer)