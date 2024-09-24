number, scale = map(str, input().split())

scale10 = 0

# print(ord('A') - 55)

for i in range(len(number)):
    if ord(number[-(i+1)]) >= 65:
        scale10 += int(ord(number[-(i+1)])-55) * (int(scale) ** i)
    else:
        scale10 += int(number[-(i+1)]) * (int(scale) ** i)
    
print(scale10)