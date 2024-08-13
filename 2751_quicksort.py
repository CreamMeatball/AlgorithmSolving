N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))
    
def quick_sort(list, start, end):
    if start>=end:
        return
    pivot = start
    left = start
    right = end
    
    while left <= right:
        while left <= end and list[left] <= list[pivot]:
            left += 1
        while right > start and list[right] >= list[pivot]:
            right -= 1
        if left > right:
            list[right], list[pivot] = list[pivot], list[right]
        else:
            list[left], list[right] = list[right], list[left]
    quick_sort(list, start, right-1)
    quick_sort(list, right+1, end)
    
# sorted_numbers = sorted(numbers)
quick_sort(numbers, 0, len(numbers)-1)

# print('\n'.join(str(n) for n in sorted_numbers))
print('\n'.join(str(n) for n in numbers))