N = int(input())
F = int(input())

N_edit = N // 100 * 100
remain = N_edit % F
if remain == 0:
    print('00')
else:
    print(str(F - remain).zfill(2))