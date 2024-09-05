N = int(input())

numbers = str(input())

splited = []

for i in range(N):
    splited.append(int(numbers[i]))
    
print(sum(splited))