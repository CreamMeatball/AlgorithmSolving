N = int(input())

numbers = []
result = 0
locationSave = [-1,-1]

for i in range(N):
    numbers.append(int(input()))

def MaxAndDelete(numbers, result):
    
    currentNumbers = numbers
    currentResult = result
    locationSave = [-1, -1]
    
    if len(currentNumbers) == 0:
        return currentNumbers, currentResult
    
    multifly = [[] for _ in range(len(currentNumbers))]

    for i in range(len(currentNumbers)):
        for number in currentNumbers:
            multifly[i].append(currentNumbers[i] * number)

    maxMul = max(currentNumbers)
 
    for i in range(len(multifly)):
        for j in range(len(multifly[i])):
            if i == j:
                continue
            elif maxMul < multifly[i][j]:
                maxMul = multifly[i][j]
                locationSave[0] = i
                locationSave[1] = j

    if -1 not in locationSave:
        currentResult += maxMul
    
    if -1 not in locationSave:
        currentNumbers[locationSave[0]] = 1001
        currentNumbers[locationSave[1]] = 1001
    
    currentNumbers = [i for i in currentNumbers if i != 1001]
    
    if -1 not in locationSave:
        return MaxAndDelete(currentNumbers, currentResult)
    else:
        currentResult += max(currentNumbers)
        currentNumbers.remove(max(currentNumbers))
        return MaxAndDelete(currentNumbers, currentResult)

result = MaxAndDelete(numbers, result)[1]
print(result)