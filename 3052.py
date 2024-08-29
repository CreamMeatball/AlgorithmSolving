remainders = []

for i in range(10):
    number = int(input())
    if number % 42 not in remainders:
        remainders.append(number % 42)
        
print(len(remainders))