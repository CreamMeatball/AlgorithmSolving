while(True):
    inputdata = input()
    if inputdata == '0 0 0':
        break
    a, b, c = map(int, inputdata.split())
    
    if max(a,b,c) >= a + b + c - max(a,b,c):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
        
