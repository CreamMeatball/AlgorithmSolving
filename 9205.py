import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())

def calc_manh_dist(cr, cc, tr, tc):
    return int(abs(tr - cr) + abs(tc - cc))

for _ in range(t):
    n = int(input().rstrip())
    house_pos = tuple(map(int, input().rstrip().split()))
    conv_pos = [tuple(map(int, input().rstrip().split())) for _ in range(n)]
    penta_pos = tuple(map(int, input().rstrip().split()))
    
    visited = [False] * len(conv_pos)
    
    result = 0
    
    dq = deque()
    dq.append(house_pos)
    
    # 집, 편의점, 펜타락페 각각을 하나의 노드로 보기
    
    while dq:
        cr, cc = dq.popleft()
        if calc_manh_dist(cr, cc, penta_pos[0], penta_pos[1]) <= 50 * 20:
            print('happy')
            result = 1
            break
        
        for i, (conv_r, conv_c) in enumerate(conv_pos):
            if calc_manh_dist(cr, cc, conv_r, conv_c) <= 50 * 20 and not visited[i]:
                dq.append((conv_r, conv_c))
                visited[i] = True
                
    if not result:
        print('sad')