# PyPy3

X, Y, W, S = map(int, input().split())

x, y = 0, 0

costEff = False
if S < 2 * W:
    costEff = True
    
time = 0

while (x, y) != (X, Y):
    if costEff: # 대각선으로 움직이는 게 더 효율적일 때
        if abs(X - x) > 0 and abs(Y - y):
            time += S
            if X - x > 0:
                x += 1
            else:
                x -= 1
            if Y - y > 0:
                y += 1
            else:
                y -= 1
        elif X == x: # 목표지랑 X가 같을 때
            if abs(Y - y) == 1: # 한 칸 차이일 때
                time += W
                if Y - y > 0:
                    y += 1
                else:
                    y -= 1
            else:
                if 2 * S < 2 * W: # 목표지가 평행 위치지만, 대각선 이동 2번 해서 평행 이동 하는 게 더 빠를 때
                    time += 2 * S
                    if Y - y > 0:
                        y += 2
                    else:
                        y -= 2
                else:
                    time += W
                    if Y - y > 0:
                        y += 1
                    else:
                        y -= 1
        else: # 목표지랑 Y가 같을 때
            if abs(X - x) == 1: # 한 칸 차이일 때
                time += W
                if X - x > 0:
                    x += 1
                else:
                    x -= 1
            else:
                if 2 * S < 2 * W: # 목표지가 평행 위치지만, 대각선 이동 2번 해서 평행 이동 하는 게 더 빠를 때
                    time += 2 * S
                    if X - x > 0:
                        x += 2
                    else:
                        x -= 2
                else:
                    time += W
                    if X - x > 0:
                        x += 1
                    else:
                        x -= 1
        
    else: # 대각선으로 움직이는 게 더 효율적이지 않을 때
        time += (X - x) * W
        time += (Y - x) * W
        x = X
        y = Y
        
print(time)