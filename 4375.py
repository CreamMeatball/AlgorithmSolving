while True:
    try:
        n = int(input())
        
        count = 1
        num = 1
        while num % n != 0:
            num = (num * 10 + 1) % n
            count += 1
        print(count)

    except EOFError:
        break
