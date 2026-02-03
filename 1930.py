import sys

input = sys.stdin.readline

K = int(input().rstrip())

for _ in range(K):
    a1, a2, a3, a4, b1, b2, b3, b4 = map(int, input().rstrip().split())
    
    # 첫 번째 정사면체의 면 구성 (리스트)
    A = [a1, a2, a3, a4]
    
    target = (b1, b2, b3, b4)

    # 그냥 greedy 하게 하면 되는 듯. 더 효율적인 방법 있나 생각해봤는데, 딱히 없는 듯
    # 정사면체를 회전해서 얻을 수 있는 모든 인덱스 조합 (12가지)
    # 노트에 실제로 그림 그려서 보면 편하고 정확한 듯
    rotations = [
        (0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2), # 밑면이 A[0]인 경우
        (1, 0, 3, 2), (1, 3, 2, 0), (1, 2, 0, 3), # 밑면이 A[1]인 경우
        (2, 0, 1, 3), (2, 1, 3, 0), (2, 3, 0, 1), # 밑면이 A[2]인 경우
        (3, 0, 2, 1), (3, 2, 1, 0), (3, 1, 0, 2)  # 밑면이 A[3]인 경우
    ]
    
    found = 0
    
    for r in rotations:
        # 회전된 상태의 색상 조합 생성
        current_view = (A[r[0]], A[r[1]], A[r[2]], A[r[3]])
        
        if current_view == target:
            found = 1
            break
            
    print(found)
