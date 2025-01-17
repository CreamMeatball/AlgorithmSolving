N = int(input())
k = int(input())

# A는 [N][N] 이란 뜻이고 (index 1 ~ N)
# B는 [N*N] 이란 뜻

# A = [[0 for _ in range(N+1)] for _ in range(N+1)]
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         A[i][j] = i * j
    
# print("A : ")
# for row in range(1, N+1):
#     print("\t".join(map(str, A[row][1:])))
    
# B = []
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         B.append(A[i][j])
        
# B.sort()
# print("B : ")
# print(B)

# 기본 숫자 1 ~ N이 1개씩 있고
# (1 ~ N) 에 *row_index 를 한 값들이 B에 들어감
# N = 9 일 때
# 36 : 1x36 2x18 3x12 4x9 6x6
# 에서 N이 9이므로 9 이하의 약수를 갖는 것만 보면
# 36 : 3x12 4x9 6x6
# 그래서 36은 총 3개 존재함

# def getDivisor(n):
#     divisorsList = []
#     for i in range(1, int(n**(1/2)) + 1):
#         # print(f"i : {i}")
#         if (n % i == 0):
#             divisorsList.append(i) 
#     # divisorsList.sort()
#     return divisorsList

# def countNumberOfThis(number):
#     global N
#     divisorsList = getDivisor(number)
#     count = 0
#     for d in divisorsList:
#         if d <= N and number // d <= N:
#             if d ** 2 == number:
#                 count += 1
#             else:
#                 count += 2
#     return count

def get_count(N, mid):
    """
    주어진 mid 값보다 작거나 같은 A[i][j]의 총 개수를 반환합니다.
    """
    count = 0
    for i in range(1, N + 1):
        count += min(N, mid // i)
    return count

def binary_search_recursive(N, k, low, high):
    """
    재귀적으로 이진 탐색을 수행하여 B[k] 값을 찾습니다.
    """
    if low > high:
        return low

    mid = (low + high) // 2
    count = get_count(N, mid)

    if count >= k:
        return binary_search_recursive(N, k, low, mid - 1)
    else:
        return binary_search_recursive(N, k, mid + 1, high)

low = 1
high = N * N

result = binary_search_recursive(N, k, low, high)
print(result)