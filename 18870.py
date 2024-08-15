import sys

N = int(sys.stdin.readline().rstrip())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

sorted_set_numbers = sorted(set(numbers))
# 요건 오히려 시간 초과가 나지 않음!!

# .index() 안 쓰고 딕셔너리로 해결(값 : 인덱스 형태로 매핑)
indexDictOf_sorted_set_numbers = {sorted_set_numbers[i] : i for i in range(len(sorted_set_numbers))}

# 메모리 덜 먹고, 시간 더 오래 걸림.
# for i in numbers:
#     print(indexDictOf_sorted_set_numbers[i], end=' ')

# 메모리 더 먹고, 시간 덜 걸림.
print(' '.join(str(indexDictOf_sorted_set_numbers[i]) for i in numbers))

# print(' '.join(map(str, list(indexDictOf_sorted_set_numbers[i] for i in numbers))))