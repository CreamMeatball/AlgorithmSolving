import sys
input_data = sys.stdin.readline

N, M = map(int, input_data().split())

number_map = []
for _ in range(N):
    number_map.append(list(map(int, input_data().split())))
    
accum = [[0 for _ in range(N)] for _ in range(N)]

# print(accum)

for i in range(N):
    for j in range(N):
        accum[i][j] = number_map[i][j] if j == 0 else accum[i][j-1] + number_map[i][j]
        
accum2 = [[0 for _ in range(N)] for _ in range(N)]
# accum2 : 맨 처음 위치 (1,1)부터 (i,j)까지의 누적합

for i in range(N):
    for j in range(N):
        accum2[i][j] = accum[i][j] if i == 0 else accum2[i-1][j] + accum[i][j]
        
# print(accum2)

for _ in range(M):
    question = list(map(int, input_data().split()))
    x1, y1, x2, y2 = question
    if x1 == 1 and y1 == 1:
        print(accum2[x2-1][y2-1])
    elif x1 == 1:
        print(accum2[x2-1][y2-1] - accum2[x2-1][y1-2])
    elif y1 == 1:
        print(accum2[x2-1][y2-1] - accum2[x1-2][y2-1])
    else:
        print(accum2[x2-1][y2-1] - accum2[x1-2][y2-1] - accum2[x2-1][y1-2] + accum2[x1-2][y1-2])

    
# print(number_map)
# print(accum)

# for _ in range(M):
#     question = list(map(int, input_data().split()))
#     x1, y1, x2, y2 = question
#     result = 0
#     for i in range(y1-1, y2):
#         result += accum[i][x2-1] if x1 == 1 else accum[i][x2-1] - accum[i][x1-2]
#     print(result)
    