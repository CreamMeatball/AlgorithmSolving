L, R = map(int, input().split())

str_L = str(L)
str_L = str_L.zfill(len(str(R)))
str_R = str(R)

count = 0

for i in range(len(str_L)):
    if str_L[i] != str_R[i]:
        break
    if str_L[i] == str_R[i] == '8':
        count += 1
        
print(count)