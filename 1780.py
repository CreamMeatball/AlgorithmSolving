import sys

input_data = sys.stdin.readline

N = int(input_data().rstrip())
paper = [list(map(int, input_data().split())) for _ in range(N)]

paper_minus_one = 0
paper_zero = 0
paper_one = 0

def isAllOneColor(start_row, start_column, n):
    global paper_minus_one
    global paper_zero
    global paper_one
    color = paper[start_row][start_column]
    if n > 1:
        for i in range(start_row, start_row + n):
            for j in range(start_column, start_column + n):
                if paper[i][j] != color:
                    isAllOneColor(start_row       , start_column       , n//3)
                    isAllOneColor(start_row       , start_column + n//3, n//3)
                    isAllOneColor(start_row       , start_column + 2*n//3, n//3)
                    isAllOneColor(start_row + n//3, start_column       , n//3)
                    isAllOneColor(start_row + n//3, start_column + n//3, n//3)
                    isAllOneColor(start_row + n//3, start_column + 2*n//3, n//3)
                    isAllOneColor(start_row + 2*n//3, start_column       , n//3)
                    isAllOneColor(start_row + 2*n//3, start_column + n//3, n//3)
                    isAllOneColor(start_row + 2*n//3, start_column + 2*n//3, n//3)
                    return
    if color == -1:
        paper_minus_one += 1
    elif color == 0:
        paper_zero += 1
    else:
        paper_one += 1
        
isAllOneColor(0, 0, N)
        
print(paper_minus_one)
print(paper_zero)
print(paper_one)