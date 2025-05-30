import sys

input_ = sys.stdin.readline

# sudokuMap = [list(map(int, list(str(input_().rstrip())))) for _ in range(9)]
sudokuMap = [list(int(n) for n in str(input_().rstrip())) for _ in range(9)]

for i in range(9):
    for j in range(9):