import sys

input_data = sys.stdin.readline
testPrint = False

N, C = map(int, input_data().rstrip().split())
weights = list(map(int, input_data().rstrip().split()))
# weights.sort()
# count = 1
# left, right = 0, 0
# sumOfWeights = 0
# c = [i for i in range(1, C + 1)]

# for currentweight in c:
#     left, right, sumOfWeights = 0, 0, weights[0]
#     # print(f"currentweight: {currentweight}")
#     while left <= right:
#         if sumOfWeights == currentweight:
#             count += 1
#             right += 1
#             if right == N:
#                 break
#             sumOfWeights += weights[right]
#             sumOfWeights -= weights[left]
#             left += 1
#         elif sumOfWeights < currentweight:
#             right += 1
#             if right == N:
#                 break
#             sumOfWeights += weights[right]
#         else:
#             sumOfWeights -= weights[left]
#             left += 1
#     # print(f"count: {count}")
    
# print(count)

# 위 알고리즘은, '연속된' 경우의 물건을 넣는 수를 구하는 것이므로 틀림.
# 시간 복잡도를 줄이기 위해 meet in the middle 알고리즘을 사용해야 함.

# 1) 배열을 두 부분으로 나누기
mid = N // 2
left_part = weights[:mid]
print(f"left_part: {left_part}") if testPrint else None
right_part = weights[mid:]
print(f"right_part: {right_part}") if testPrint else None

# 2) 부분 집합의 합을 구하는 함수
def get_subset_sums(arr):
    sums = []
    length = len(arr)
    # 부분 집합 개수: 2^length
    for mask in range(1 << length): # bit left shift. = range(1, 2^length)
        s = 0 # subset sum
        for i in range(length):
            if mask & (1 << i): # &: bitwise and operation
                # mask의 i번째 비트가 1인지 확인. i번째 비트가 1이면 부분 집합에 arr[i]가 포함된다고 해석.
                print(f"mask: {mask}, i: {i}, 1 << i: {1 << i}") if testPrint else None
                s += arr[i]
        sums.append(s)
    return sums

# 왼쪽, 오른쪽 부분 집합의 합들 구하기
left_sums = get_subset_sums(left_part)
print(f"left_sums: {left_sums}") if testPrint else None
right_sums = get_subset_sums(right_part)
print(f"right_sums: {right_sums}") if testPrint else None

# 정렬 - 투 포인터로 쌍을 효율적으로 계산하기 위함
left_sums.sort()
right_sums.sort()

count = 0
left_index, right_index = 0, len(right_sums) - 1

# 원래는 2^N 만큼의 확인을 해야하지만
# 절반을 나눠서 두 부분집합으로 만든 뒤
# 'left부분집합에서 임의의 원소들의 합' + 'right부분집합에서 임의의 원소들의 합' = '전체에서 임의의 원소들의 합'
# 이 된다는 거임.
# 그렇게 해서 시간 복잡도를 2^(N/2)로 줄일 수 있음. 

# 3) 투 포인터로 (left_sums[left_index] + right_sums[right_index]) <= C 인 경우 세기
while left_index < len(left_sums) and right_index >= 0:
    if left_sums[left_index] + right_sums[right_index] <= C:
        # right_index 이하의 모든 값과 짝지어도 C 이하
        count += (right_index + 1) # 현재의 left에 대해 right_index 이하의 모든 right 부분집합이 다 가능하단 것.
        left_index += 1
    else: # 합이 더 클 경우
        right_index -= 1
        # left_index는 초기화하지 않고 유지되는 게 맞음.
        # 왜냐면 이전의 left_index에 대해서는 가능한 모든 right 경우가 이미 다 세어졌기 때문.

print(count)