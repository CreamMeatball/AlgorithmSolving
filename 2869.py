import sys

A, B, V = map(int, sys.stdin.readline().rstrip().split())

# 시간 초과 남
# day = 1
# while(V>A):
#     day += 1
#     V -= (A-B)

# 반복문 안 쓰고 구하기 (수학적으로 사고)
if (V-A) % (A-B) == 0:
    day = (V-A) // (A-B) + 1
else:
    day = (V-A) // (A-B) + 2

print(day)