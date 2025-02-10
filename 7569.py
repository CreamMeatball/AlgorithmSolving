import sys

input_data = sys.stdin.readline

M, N, H = map(int, input_data().split())
# M : col, N : row, H : height

box = [[[0] * (M + 2) for _ in range(N + 2)] for _ in range(H)]
visited = [[[False] * (M + 2) for _ in range(N + 2)] for _ in range(H)]

totalTomatoes = N * M * H

for h in range(H):
    for n in range(N):
        # box[h][n] = [0] + list(map(int, input_data().split())) + [0]
        tomato_data = list(map(int, input_data().split()))
        

count = 0

def bfs(box, current_node):
    