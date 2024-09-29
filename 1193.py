# 1/1
# 1/2 2/1
# 3/1 2/2 1/3
# 1/4 2/3 3/2 4/1
# 5/1 4/2 3/3 2/4 1/5

import sys

N = int(sys.stdin.readline().rstrip())

endvalue = 1
layer = 1

while N > endvalue:
    layer += 1
    endvalue += layer

startvalue = endvalue - layer + 1

firstvalue = N-startvalue+1
        
if layer % 2 == 0:
    print(f"{firstvalue}/{layer+1-firstvalue}")
else:
    print(f"{layer+1-firstvalue}/{firstvalue}")

