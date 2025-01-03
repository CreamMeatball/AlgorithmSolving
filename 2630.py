import sys

input_data = sys.stdin.readline

N = int(input_data().rstrip())
paper = [list(map(int, input_data().split())) for _ in range(N)]

white = 0
blue = 0

def isAllOneColor(start_x, start_y, n):
    global white
    global blue
    color = paper[start_x][start_y]
    if n > 1:
        for i in range(start_x, start_x + n):
            for j in range(start_y, start_y + n):
                if paper[i][j] != color:
                    isAllOneColor(start_x       , start_y       , n//2)
                    isAllOneColor(start_x + n//2, start_y       , n//2)
                    isAllOneColor(start_x       , start_y + n//2, n//2)
                    isAllOneColor(start_x + n//2, start_y + n//2, n//2)
                    return
    if color == 0:
        white += 1
    else:
        blue += 1
        
isAllOneColor(0, 0, N)

print(white)
print(blue)