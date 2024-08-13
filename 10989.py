import sys
# 메모리가 작기 때문에 계수정렬을 이용해야 함
# 계수정렬 : 각 데이터가 몇 번 등장했는지 세는 정렬 알고리즘
# 1이 3개, 4가 2개, 3이 1개 등장했다면 111344 이런 식으로 개수만큼 출력하는 방식
# 다만 계수정렬의 경우 안 쓰는 공간이 많아질 수 있기에 array 내에 낭비되는 공간이 많을 수 있음.

N = int(input())

numbers = [0 for _ in range(10001)]

# 메모리가 작기 때문에 input()을 사용하면 안됨
for _ in range(N):
    # 메모리가 작기 때문에 .append()를 사용하면 안됨
    # append는 시행할 때마다 메모리 재할당(필요한 메모리 크기를 다시 설정함)을 함.
    # 빈번한 메모리 재할당은 메모리를 비효율적으로 사용함.
    # >> 한 번에 메모리를 할당하고 그대로 사용하는 것이 메모리 효율성이 좋음.
    # numbers.append(int(sys.stdin.readline().rstrip()))
    
    # 입력 받은 숫자에 해당하는 순서에 개수를 1개 추가함.
    numbers[int(sys.stdin.readline().rstrip())] += 1
    
    
# 메모리가 작기 때문에 sorted 사용하면 안됨
# sorted_numbers = sorted(numbers)

# print('\n'.join(str(i*numbers[i]) for i in range(1, len(numbers))))

for i in range(1, len(numbers)):
    # print(i * numbers[i]) if numbers[i] != 0 else None
    print(f'{i}\n' * numbers[i], end='') if numbers[i] != 0 else None