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
            if 2 * S < 2 * W: # 대각선 2번으로 평행이동 하는 게 더 효율적일 때
                if abs(Y - y) % 2 == 0:
                    time += abs(Y - y) * S
                    y = Y
                else:
                    time += (abs(Y - y) - 1) * S + W
                    y = Y
            else:
                time += abs(Y - y) * W
                y = Y
        else: # 목표지랑 Y가 같을 때
            if 2 * S < 2 * W: # 대각선 2번으로 평행이동 하는 게 더 효율적일 때
                if abs(X - x) % 2 == 0:
                    time += abs(X - x) * S
                    x = X
                else:
                    time += (abs(X - x) - 1) * S + W
                    x = X
            else:
                time += abs(X - x) * W
                x = X
        
    else: # 대각선으로 움직이는 게 더 효율적이지 않을 때
        time += (X - x) * W
        time += (Y - x) * W
        x = X
        y = Y
        
print(time)