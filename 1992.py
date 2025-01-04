import sys

input_data = sys.stdin.readline

N = int(input_data().rstrip())
screen = [list(map(int, list(input_data().rstrip()))) for _ in range(N)]

# print(screen)

def isAllOneColor(start_row, start_column, n):
    global white
    global black
    color = screen[start_row][start_column]
    if n > 1:
        for i in range(start_row, start_row + n):
            for j in range(start_column, start_column + n):
                if screen[i][j] != color:
                    print("(", end='')
                    isAllOneColor(start_row       , start_column       , n//2)
                    isAllOneColor(start_row       , start_column + n//2, n//2)
                    isAllOneColor(start_row + n//2, start_column       , n//2)
                    isAllOneColor(start_row + n//2, start_column + n//2, n//2)
                    print(")", end='')
                    return
    print(color, end='')
    return
        
isAllOneColor(0, 0, N)