from itertools import permutations
import math

abilities = list(map(int, input().split()))

perms = permutations(abilities, 8)

def isAcute(val1, val2, val3):
    x1, y1 = - (val1 / math.sqrt(2)), (val1 / math.sqrt(2))
    x2, y2 = 0, val2
    x3, y3 = (val3 / math.sqrt(2)), (val3 / math.sqrt(2))
    
    # print(x1, y1)
    # print(x2, y2)
    # print(x3, y3)
    
    v1 = (x3 - x1, y3 - y1)
    v2 = (x2 - x1, y2 - y1)
    
    crossProduct = v1[0] * v2[1] - v1[1] * v2[0] # 외적 (CCW 판정)
    
    # print(crossProduct)
    
    if crossProduct > 0:
        return True
    else:
        return False
    
count = 0
    
for per in perms:
    for i in range(8):
        if not isAcute(per[(i%8)], per[(i+1)%8], per[(i+2)%8]):
            break
    else:
        count += 1
        
print(count)