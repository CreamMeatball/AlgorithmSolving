total = int(input())
result = 0

while(total>=0):
    if(total%5==0):
        result += int(total/5)
        print(result)
        break
    elif total>=3:
        total -= 3
        result+=1
    else:
        print(-1)
        break