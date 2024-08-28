numbers = [i for i in range(31)]

for i in range(28):
    submit = int(input())
    numbers[submit] = -1
    
for i in range(1, 31):
    if numbers[i] != -1:
        print(numbers[i])