A, B = map(list, input().split())

sum_ = 0
sum_B = sum(map(int, B))

for a in A:
    sum_ += int(a) * sum_B
        
print(sum_)