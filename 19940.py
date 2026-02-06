import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    
    best_res = (float('inf'), 0, 0, 0, 0, 0)
    
    q = N // 60
    for h in [q, q + 1, q - 1]:
        if h < 0:
            continue
            
        rem_h = N - 60 * h
        
        qb = rem_h // 10
        for b in [qb, qb + 1, qb - 1]:
            o = rem_h - 10 * b
            
            tp = b if b > 0 else 0 # ADDT
            tm = -b if b < 0 else 0 # MINT
            op = o if o > 0 else 0 # ADDO
            om = -o if o < 0 else 0 # MINO
            
            total_press = h + tp + tm + op + om
            
            current_res = (total_press, h, tp, tm, op, om)
            
            if current_res < best_res:
                best_res = current_res
    
    print(f"{best_res[1]} {best_res[2]} {best_res[3]} {best_res[4]} {best_res[5]}")