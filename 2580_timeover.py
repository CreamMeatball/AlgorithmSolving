def sudoku(depth, board):
    # depth가 81이면 모든 칸을 채운 것이므로 보드를 출력하고 프로그램을 종료합니다.
    if depth == 81:
        for row in board:
            print(" ".join(map(str, row)))
        exit()
    
    # 현재 위치의 행과 열을 계산합니다.
    # depth 라는 1 ~ 81의 숫자를 9로 나눈 몫이 행 번호, 나머지가 열 번호가 됩니다.
    y = depth // 9
    x = depth % 9
    
    # 현재 위치가 0이면 (빈 칸이면)
    if board[y][x] == 0:
        # 1부터 9까지의 숫자를 시도합니다.
        for i in range(1, 10):
            # 현재 위치에 숫자 i를 놓을 수 있는지 확인합니다.
            if check(y, x, i, board):
                # 숫자 i를 현재 위치에 놓습니다.
                board[y][x] = i
                # 다음 칸으로 이동합니다.
                sudoku(depth + 1, board)
                # 숫자 i를 다시 제거합니다 (백트래킹).
                # 숫자 넣은 게 성립되는 경우엔 계속 위 재귀를 타고 들어갈텐데
                # 그게 아니라면 이전 단계로 돌아가야 하므로 이전 단계의 숫자를 0으로 초기화
                board[y][x] = 0
    else:
        # 현재 위치가 빈 칸이 아니면 다음 칸으로 이동합니다.
        sudoku(depth + 1, board)
        
def check(y, x, num, board):
    # 아래의 세 가지 중 하나라도 해당되면 False를 반환합니다.
    # 같은 행에 숫자 num이 있는지 확인합니다.
    for i in range(9):
        if board[y][i] == num:
            return False
    # 같은 열에 숫자 num이 있는지 확인합니다.
    for i in range(9):
        if board[i][x] == num:
            return False
    # 3x3 박스에 숫자 num이 있는지 확인합니다.
    for i in range(3):
        for j in range(3):
            if board[(y // 3) * 3 + i][(x // 3) * 3 + j] == num:
                return False
    # 숫자 num을 놓을 수 있으면 True를 반환합니다.
    return True

# 9x9 보드를 입력받습니다.
board = [list(map(int, input().split())) for _ in range(9)]

# 스도쿠를 해결합니다.
sudoku(0, board)