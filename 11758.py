P1 = tuple(map(int, input().split()))
P2 = tuple(map(int, input().split()))
P3 = tuple(map(int, input().split()))

# P1 -> P2 벡터: A벡터
# P2 -> P3 벡터: B벡터

# 어떤 방향(시계/반시계)을 이루고 있는지? 의 뜻
# A벡터와 B벡터의 출발점을 동일히 놓고
# A벡터를 B벡터 방향으로 회전시킬 때 (180도 이하로)
# 시계 방향으로 돌리는지 반시계 방향으로 돌리는지.

A = (P2[0] - P1[0], P2[1] - P1[1])
B = (P3[0] - P2[0], P3[1] - P2[1])

# 외적: Ax * By - Ay * Bx
cross_product = A[0] * B[1] - A[1] * B[0]

# 반시계 (CCW) : + 값
# 시계 (CW) : - 값
# 평행 : 0

# 참고
# https://www.acmicpc.net/blog/view/27

# print(cross_product)

if cross_product > 0: # 반시계일 때 + 값
    print(1)
elif cross_product < 0: # 시계일 때 - 값
    print(-1)
else:
    print(0)