a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

# 합집합
print(a | b)
print(set.union(a,b))

# 교집합
print(a & b)
print(set.intersection(a,b))

# 차집합
print(a - b)
print(set.difference(a,b))