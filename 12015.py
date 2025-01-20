import sys
input = sys.stdin.readline

# lis 문제.
# 가능한 경우가 여러 가지이고, 그 중 최장 길이를 찾는 것이기 때문에
# 일반적으로 DP로 푼다.

# length = int(input())
# arr = list(map(int, input().split()))
# dp = [1 for _ in range(length)] # dp[i] : i번째 원소를 마지막으로 하는 최장 증가 부분 수열의 길이
# for i in range(length):
#     for j in range(i):
#         if arr[i] > arr[j]:
#              dp[i] = max(dp[i], dp[j]+1)
# print(max(dp))

# 근데 이분탐색으로 풀면 시간복잡도를 O(n^2)에서 O(nlogn)으로 줄일 수 있다.

# 참고 : https://jainn.tistory.com/90

n = int(input())
cases = list(map(int, input().split()))
lis = [0]

test_print = False

for case in cases:
    if lis[-1]<case: # 원소가 lis의 마지막 원소보다 크다면 lis에 추가
        lis.append(case)
    else: # 원소가 lis의 마지막 원소보다 작다면 이분탐색을 통해 lis 내에서 위치를 찾아서 교체
        left = 0
        right = len(lis)

        # lis 배열 내에서 이분탐색을 쓰는 것.
        # 현재 상태의 lis 배열에서, case로 교체할 위치를 찾는다.
        while left<right:
            print(f"current lis : {lis}") if test_print else None
            mid = (right+left)//2
            if lis[mid]<case:
                left = mid+1 # 우측 범위 탐색
            else:
                right = mid # 좌측 범위 탐색
        # 원소를 lis 내에 교체할 위치를 찾으면
        print(f"lis substitute. lis[{right}] = {case}") if test_print else None
        lis[right] = case # 해당 위치에 원소를 교체
        # 현재의 원소를 lis 내에 가능한 최대한의 오른쪽에다 교체하는 것.
        # 이걸(교체) 왜햐냐면
        # 현재 상태의 lis를 최대한 압축해서 만드는 거.
        # 테스트 입력으로
        # 8
        # 10 20 10 30 20 70 40 60
        # 을 해보면
        # lis = [0, 10, 20, 30, 70] 이었던 상태에서
        # lis = [0, 10, 20, 30, 40] 으로 바뀌고
        # 그 뒤에 60을 추가할 수 있게 되어서 더 최장의 lis를 구할 수 있음.

print(f"final lis : {lis}") if test_print else None
print(len(lis)-1)

# 예제 이해 
# 수열 A = {10, 20, 10, 30, 20, 50}을 예로 들어 설명해보겠습니다.

# 초기 lis = [0]
# 첫 번째 원소 10:
# lis[-1] = 0 < 10 → lis = [0, 10]
# 두 번째 원소 20:
# lis[-1] = 10 < 20 → lis = [0, 10, 20]
# 세 번째 원소 10:
# lis[-1] = 20 >= 10 → 이분 탐색으로 10을 lis 내에 삽입할 위치 찾기
# lis = [0, 10, 20]에서 10을 대체 → lis = [0, 10, 20] (변화 없음)
# 네 번째 원소 30:
# lis[-1] = 20 < 30 → lis = [0, 10, 20, 30]
# 다섯 번째 원소 20:
# lis[-1] = 30 >= 20 → 이분 탐색으로 20을 lis 내에 삽입할 위치 찾기
# lis = [0, 10, 20, 30]에서 20을 대체 → lis = [0, 10, 20, 30] (변화 없음)
# 여섯 번째 원소 50:
# lis[-1] = 30 < 50 → lis = [0, 10, 20, 30, 50]
# 최종적으로 lis는 [0, 10, 20, 30, 50]이 되어, LIS의 길이는 4가 됩니다.