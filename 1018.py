M, N = map(int, input().split())

# [[-1]*M]*N 으로 쓰게 되면 shallow copy가 돼서, 한 값을 바꾸면 다른 모든 값이 바뀜
board = [[-1 for _ in range(M)] for _ in range(N)]

# for i in range(N):
#     board_input = str(input())
#     for j in range(M):
#         board[i][j] = board_input[j]
        
# 이렇게 해도 한 글자씩으로 들어감. 여러개 글자 단위로 넣으려면 split() 이용해서 기준 잡아주기        
for i in range(N):
    board[i] = list(input())

# print(board)

def splitBoard(i, j):
    # i, j 는 시작점.
    split_board = [[-1 for _ in range(8)] for _ in range(8)]
    for k in range(8):
        for l in range(8):
            split_board[k][l] = board[i+k][j+l]
    return split_board

# i, j 를 나눠서 if/else 문 쓸 필요 없이, "i+j" 값이 일관된다는 규칙이 있음.
def countPaint(split_board):
    count = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                if split_board[i][j] == 'B':
                    count += 1
            else:
                if split_board[i][j] == 'W':
                    count += 1
    count2 = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                if split_board[i][j] == 'W':
                    count2 += 1
            else:
                if split_board[i][j] == 'B':
                    count2 += 1
    
    return min(count, count2)

minPaint = []

for i in range(N-7):
    for j in range(M-7):
        minPaint.append(countPaint(splitBoard(i, j)))
        
print(min(minPaint))
