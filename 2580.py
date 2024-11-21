def sudoku(depth, board, rows, cols, boxes):
    if depth == 81:
        for row in board:
            print(" ".join(map(str, row)))
        exit()
    
    y = depth // 9
    x = depth % 9
    
    if board[y][x] == 0:
        for num in range(1, 10):
            if num not in rows[y] and num not in cols[x] and num not in boxes[(y // 3) * 3 + (x // 3)]:
                board[y][x] = num
                rows[y].add(num)
                cols[x].add(num)
                boxes[(y // 3) * 3 + (x // 3)].add(num)
                
                sudoku(depth + 1, board, rows, cols, boxes)
                
                board[y][x] = 0
                rows[y].remove(num)
                cols[x].remove(num)
                boxes[(y // 3) * 3 + (x // 3)].remove(num)
    else:
        sudoku(depth + 1, board, rows, cols, boxes)

def check(y, x, num, board):
    for i in range(9):
        if board[y][i] == num or board[i][x] == num:
            return False
    for i in range(3):
        for j in range(3):
            if board[(y // 3) * 3 + i][(x // 3) * 3 + j] == num:
                return False
    return True

# 9x9 보드를 입력받습니다.
board = [list(map(int, input().split())) for _ in range(9)]

# 행, 열, 박스에 있는 숫자를 추적합니다.
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]

# 초기 보드 상태를 기반으로 행, 열, 박스에 있는 숫자를 설정합니다.
for y in range(9):
    for x in range(9):
        if board[y][x] != 0:
            rows[y].add(board[y][x])
            cols[x].add(board[y][x])
            boxes[(y // 3) * 3 + (x // 3)].add(board[y][x])

# 스도쿠를 해결합니다.
sudoku(0, board, rows, cols, boxes)