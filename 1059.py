L = int(input())
number_set = list(map(int, input().split()))
n = int(input())

# A ~ B 까지 전부 집합 S에 포함되지 않는 (A, B)의 개수

sorted_number_set = sorted(number_set)
# print(sorted_number_set)

# count = 0

# for i in range(1, len(sorted_number_set)):
#     if (sorted_number_set[i-1] < n) and (n < sorted_number_set[i]):
#         for j in range(sorted_number_set[i-1]+1, sorted_number_set[i]):
#             for k in range(1, sorted_number_set[i] - sorted_number_set[i-1] + 1):
#                 start = j
#                 end = j + k
#                 if end < sorted_number_set[i] and (start <= n) and (n <= end):
#                     count += 1
#     else:
#         continue

# print(count)

# ⬆️ 틀렸다고 나옴.

left, right = 0, 0

# # n이 들어갈 왼쪽 구간, 오른쪽 구간 찾기
# for i in range(1, len(sorted_number_set)):
#     if sorted_number_set[i] == n:
#         # n이 이미 집합 S에 들어있으면, 좋은 구간은 만들 수 없음
#         print(0)
#         exit()
#     if sorted_number_set[i] > n:
#         right = sorted_number_set[i]
#         left = sorted_number_set[i - 1]
#         break

# # 가능한 (A, B)는
# #   A ∈ [left+1, n], B ∈ [n, right-1] 이고 A < B
# #   A의 개수: n - (left+1) + 1 = n - left
# #   B의 개수: (right-1) - n + 1 = right - n
# #   전체 쌍: (n - left) × (right - n)
# #   A = B = n 인 1가지(불가능) 제거 => -1
# count = (n - left) * (right - n) - 1
# # 학교에서 예전에 '상의와 하의를 조합해 입는 경우의 수'를 구할 때처럼
# # (n - left) 영역에서 하나 고르고, (right - n) 영역에서 하나 골라서 곱함
# # 그리고 A = B = n인 경우를 제외하면 됨 (1가지)
# print(count)

# ⬆️ 얘도 틀림.

# # n이 들어갈 왼쪽 구간, 오른쪽 구간 찾기
# for i in range(len(sorted_number_set)):
#     if sorted_number_set[i] == n:
#         # n이 이미 집합 S에 들어있으면, 좋은 구간은 만들 수 없음
#         print(0)
#         exit()
#     if sorted_number_set[i] > n and i != 0 and sorted_number_set[i - 1] < n:
#         right = sorted_number_set[i] - 1
#         left = sorted_number_set[i - 1] + 1
#         break

# count = (n - left + 1) * (right- n + 1) - 1
# print(count)

# ⬆️ 얘도 틀림.
# 2
# 3 7
# 4
# 라는 반례가 있음.
# left = n 이 되는 경우에 문제가 생김.



# n이 집합에 있으면 0
if n in sorted_number_set:
    print(0)
else:
    # n보다 작은 수 중 최댓값(left)과, n보다 큰 수 중 최솟값(right)을 찾기
    left, right = 0, 0
    for num in sorted_number_set:
        if num < n:
            left = num
        elif num > n and right == 0:
            right = num
            break
    left += 1
    right -= 1

    count = (n - left) * (right - n + 1) + (right - n)
    print(count)