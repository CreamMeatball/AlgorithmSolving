N = int(input())
difference = []
for i in range(N):
    temp = list(map(int, input().split()))
    d = temp[0] - temp[1]
    difference.append(d)
difference.sort()
# # print(difference)
# difference_set = set(difference)
# difference = list(difference_set)
# print(difference)

if len(difference) % 2 == 1:
    print(1)
else:
    print(abs(difference[len(difference)//2 - 1] - difference[len(difference)//2]) + 1)