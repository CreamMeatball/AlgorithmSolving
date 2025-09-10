N = int(input())

numbers = list(map(int, input().split()))

possibleCases = set() # (a, b)

for i in range(1, N):
    prev, next = numbers[i-1], numbers[i]
    
    # 초기 생성
    if i == 1:
        possible_a = set()
        # a가 +/-인지 체크
        if next // prev > 0: sign = 1
        elif next // prev < 0: sign = -1
        else: sign = 0
        
        # find a (positive)
        if sign == 1:
            # for a in range(0, next // prev + 1, 1): # a = 0 인 경우까지 포함
            for a in range(0, 201, 1):
                b = next - prev * int(a)
                possibleCases.add((a, b))
                
        elif sign == -1:
            # for a in range(next // prev, 1, 1): # a = 0 인 경우까지 포함
            for a in range(-200, 1, 1):
                b = next - prev * int(a)
                possibleCases.add((a, b))
        
        else: # a = 0
            b = next - prev
            possibleCases.add((0, b))
            
        continue
    
    # 기존에 존재하던 Case에서 여전히 가능한 경우 탐색
    removeCases = set()
    for a, b in possibleCases:
        if not ((prev * a + b) == next):
            removeCases.add((a, b))
    for a, b in removeCases:
        possibleCases.remove((a, b))
            
# print(f"possibleCases:\n{possibleCases}")

if N == 1 or 2:
    print('A')            
elif len(possibleCases) == 0:
    print('B')
elif len(possibleCases) == 1:
    print(numbers[-1] * a + b)
else: # len > 1
    init = None
    for a, b in possibleCases:
        tempResult = numbers[-1] * a + b
        if init == None:
            init = tempResult
        elif tempResult != init:
            print('A')
            break
    else:
        print(init)