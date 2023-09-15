a = [1,2,3,4,5,6,7,8,9]

print(a[3])

print(a[1:4])

i = 9
j = [11,12,13,14,15]

b = [i for i in range(10)]
print("b : ", b)

c = [i for j in range(10)]
print("c : ", c)

d = [i for _ in range(10)]
print("d : ", d)

e = [i for i in j]
print("e : ", e)

e2 = [j for i in range(10)]
print("e2 : ", e2)

e3 = [j for j in range(10)]
print("e3 : ", e3)

e4 = [i for j in j]
print("e4 : ", e4)

x = 9

hello = 'hello'

print(x)

for x in hello:
    print(x)
    
print(x)

goodbye = 'goodbye'