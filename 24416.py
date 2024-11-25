# def fib(n):
#     global count_recur
#     if (n == 1 or n == 2):
#         count_recur += 1
#         return 1
#     else:
#         return (fib(n - 1) + fib(n - 2))
    
# def fibonacci(n):
#     global count_dyn
#     f = [0 for _ in range(41)]
#     f[1] = 1
#     f[2] = 1
    
#     for i in range(3, n+1):
#         f[i] = f[i - 1] + f[i - 2]
#         count_dyn += 1
#     return f[n]

def count_only(n):
    global count_recur
    global count_dyn
    
    cr = [0 for _ in range(41)]
    cr[1] = 1
    cr[2] = 1
    for i in range(3, n+1):
        cr[i] = cr[i - 1] + cr[i - 2]
    count_recur = cr[n]
    count_dyn = n - 2

count_recur = 0
count_dyn = 0

N = int(input())

# fib(N)
# fibonacci(N)

count_only(N)

print(f"{count_recur} {count_dyn}")