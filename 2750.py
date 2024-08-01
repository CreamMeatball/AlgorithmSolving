numberOf = int(input())
number = []

for i in range(numberOf):
    number.append(int(input()))
    
sortedNumber = sorted(number)
# 역순 : , reverse=True

for i in range(len(sortedNumber)):
    print(sortedNumber[i])

