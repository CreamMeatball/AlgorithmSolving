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

print(board)

