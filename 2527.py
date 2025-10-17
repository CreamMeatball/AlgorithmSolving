for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().rstrip().split())
    
    inter_x = max(x1, x2) # 공통영역의 왼쪽 x좌표
    inter_y = max(y1, y2) # 공통영역의 왼쪽 y좌표
    inter_p = min(p1, p2) # 공통영역의 오른쪽 x좌표
    inter_q = min(q1, q2) # 공통영역의 오른쪽 y좌표
    
    if inter_x < inter_p:
        if inter_y < inter_q:
            print('a')
        elif inter_y == inter_q:
            print('b')
        else:
            print('d')
    elif inter_x == inter_p:
        if inter_y < inter_q:
            print('b')
        elif inter_y == inter_q:
            print('c')
        else:
            print('d')
    else: # inter_x > inter_q:
        print('d')