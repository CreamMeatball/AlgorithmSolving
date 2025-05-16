n = str(input())
origin_n = n
count = 0
while (True):
    count += 1
    if int(origin_n) < 10:
        origin_n = "0" + origin_n
    # print(f"origin_n: {origin_n}")
    new_n = str(int(origin_n[0]) + int(origin_n[-1]))
    # print(f"new_n: {new_n}")
    new_n2 = str(origin_n[-1]) + str(new_n[-1])
    # print(f"new_n2: {new_n2}")
    origin_n = new_n2
    if int(origin_n) == int(n):
        break
print(count)