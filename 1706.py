import sys

input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
grid = [str(input().rstrip()) for _ in range(R)]

words = []

# 가로 단어 추출
for row in grid:
    parts = row.split('#')
    for p in parts:
        if len(p) >= 2:
            words.append(p)

# 세로 단어 추출
for c in range(C):
    col = ''.join(grid[r][c] for r in range(R))
    parts = col.split('#')
    for p in parts:
        if len(p) >= 2:
            words.append(p)

# 사전순으로 가장 앞선 단어 출력.
# string type은 min() max() 같은 함수 사용 시 유니코드(아스키코드) 기준으로 계산함.
print(min(words))