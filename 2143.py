import sys
from collections import Counter

input_ = sys.stdin.readline

T = int(input_().rstrip())
n = int(input_().rstrip())
A = list(map(int, input_().rstrip().split()))
m = int(input_().rstrip())
B = list(map(int, input_().rstrip().split()))

def all_sub_sums(arr): # 부 배열(sub-array): '연속된' 부분 수열(subsequence)
    """
    arr의 모든 부 배열 합을 반환한다.
    방법: 누적합을 구하고, 누적합[j+1] - 누적합[i]
    """
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    # prefix: 
    
    # A: 1 3 1 2
    # prefix: 0 1 4 5 7

    sub = []
    for i in range(n):
        # prefix[i]가 고정일 때 j를 증가시키며 합을 추가
        for j in range(i, n):
            sub.append(prefix[j + 1] - prefix[i]) # (j + 1)번째 누적합 - i 번째 누적합 = 부분 합
            
    # A: 1 3 1 2        
    # prefix: 1 4 5 7
    # sub: 1 - 0, 4 - 0, 5 - 0, 7 - 0, 4 - 1, 5 - 1, 7 - 1, 5 - 4, 7 - 4, 7 - 5
    # -> : 1, 4, 5, 7, 3, 4, 6, 1, 3, 2
    
    return sub

subA = all_sub_sums(A)
# print(subA)
subB = all_sub_sums(B)
# print(subB)
countB = Counter(subB) # Counter: Dictionary

count = 0

for a in subA:
    count += countB[T - a]

print(count)
