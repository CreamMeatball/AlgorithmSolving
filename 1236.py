import sys

input_ = sys.stdin.readline

N, M = map(int, input_().rstrip().split())
castle = [input_().rstrip() for _ in range(N)]

# 경비원이 없는 행 개수
missing_rows = sum(1 for row in castle if 'X' not in row)

# 경비원이 없는 열 개수
missing_cols = sum(1 for col in zip(*castle) if 'X' not in col)

# 둘 중 더 큰 값이 필요한 최소 추가 인원
print(max(missing_rows, missing_cols))
