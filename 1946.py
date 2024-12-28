import sys

input_data = sys.stdin.readline

T = int(input_data())

for _ in range(T):
    N = int(input_data())
    applicant = []
    for _ in range(N):
        applicant.append(list(map(int, input_data().split())))
    sorted_applicant = sorted(applicant, key=lambda x: x[0])
    # print(sorted_applicant)
    
    count = 1
    cutline = sorted_applicant[0][1]
    for i in range(1, N):
        if cutline >= sorted_applicant[i][1]:
            cutline = sorted_applicant[i][1]
            count += 1
    print(count)