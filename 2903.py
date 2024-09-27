N = int(input())

init_x = 2
result = (init_x)**2

for i in range(N):
    init_x = init_x + (init_x - 1)
    result = init_x ** 2
    
print(result)