from itertools import product

A, B = map(int, input().split())

# foursevens = []

# for i in range(len(str(A)), len(str(B)) + 1): # 자릿수
#     foursevens.extend(list(int(''.join(p)) for p in product(['4','7'], repeat=i)))
    
# count = 0
# for i in range(A, B + 1):
#     if i in foursevens:
#         count += 1

count = 0
for i in range(len(str(A)), len(str(B)) + 1): # 자릿수
    foursevens = list(int(''.join(p)) for p in product(['4','7'], repeat=i))
    for fs in foursevens:
        if A <= fs <= B:
            count += 1
print(count)