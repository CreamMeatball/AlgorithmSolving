from collections import deque

N, M = map(int, input().split())

numbers = [i for i in range(1, N + 1)]

def dfs(depth, numbers, result):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    for number in numbers:
        indexOfNumber = numbers.index(number)
        result.append(number)
        numbers.remove(numbers[indexOfNumber])
        # 한 앞 숫자에 대해, 뒷 숫자 모두 탐색
        dfs(depth + 1, numbers, result)
        # 이전 단계로 돌아가는 역할
        result.pop()
        numbers.insert(indexOfNumber, number)
        
        
result = deque()
dfs(0, numbers, result)