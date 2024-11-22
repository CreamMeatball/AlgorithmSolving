N = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))

# print(-30//4)
# print(-(30//4))

# print(N)
# print(A)
# print(operator)

max_result = -1000000000
min_result = 1000000000

def dfs(depth, A, operator, result):
    # print(f"N : {depth}, received result : {result}")
    result = result
    global max_result, min_result
    if depth == N - 1:
        # print("result : ", result)
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        
    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            if i == 0:
                result = A[depth] + A[depth + 1]
            elif i == 1:
                result = A[depth] - A[depth + 1]
            elif i == 2:
                result = A[depth] * A[depth + 1]
            else:
                result = A[depth] // A[depth + 1]
                # 문제에 주어진 C++14 기준
                if result < 0:
                    result = -(-A[depth] // A[depth + 1])
            prevA = A[depth + 1]
            A[depth + 1] = result
            dfs(depth + 1, A, operator, result)
            operator[i] += 1
            A[depth + 1] = prevA
            
dfs(0, A, operator, A[0])
print(max_result)
print(min_result)
