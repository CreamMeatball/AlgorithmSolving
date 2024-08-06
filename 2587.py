num = []

for _ in range(5):
    num.append(int(input()))
    
sorted_num = sorted(num)

print(sum(sorted_num)//5)
print(sorted_num[2])