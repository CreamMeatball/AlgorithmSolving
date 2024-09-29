# 1/1
# 1/2 2/1
# 3/1 2/2 1/3
# 1/4 2/3 3/2 4/1
# 5/1 4/2 3/3 2/4 1/5

N = int(input())

number = [0,0]
endvalue = 1
layer = 1
addvalue = 2
startvalue = 1

for i in range(1, N+1):
    if i > endvalue:
        layer += 1
        endvalue += addvalue
        addvalue += 1
        startvalue = endvalue - layer + 1
    # print("layer: ", layer)
    if layer % 2 == 0:
        number = [(i-startvalue+1), (layer+1)-(i-startvalue+1)]
    elif layer % 2 == 1:
        number = [(layer+1)-(i-startvalue+1), (i-startvalue+1)]
        
print(f"{number[0]}/{number[1]}")

