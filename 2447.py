import sys

# def draw_star(k):
#     if k == 0:
#         return ["*"]

#     stars = draw_star(k - 1)
#     L = []
#     for line in stars:
#         L.append(line * 3)
#     for line in stars:
#         L.append(line + " " * (3 ** (k-1)) + line)
#     for line in stars:
#         L.append(line * 3)
#     return L

# k = int(int(sys.stdin.readline().rstrip()) ** (1/3))
# print('\n'.join(draw_star(k)))

# 처음에 k 를 구해서 k 를 input 으로 넣은 다음에
# k 를 1씩 빼는 방식으로 하면 메모리 초과 남

def draw_star(N):
    if N == 1:
        return ["*"]

    stars = draw_star(N//3)
    L = []
    for line in stars:
        L.append(line * 3)
    for line in stars:
        L.append(line + " " * (N//3) + line)
    for line in stars:
        L.append(line * 3)
    return L

N = int(sys.stdin.readline().rstrip())
print('\n'.join(draw_star(N)))