S = input()
# abab
reverse_S = S[::-1]
# baba

for i in range(len(S)):
    # 팰린드롬이 되는 부분을 찾는 과정.
    if S[i:] == reverse_S[0:len(S) - i]:
        # 팰린드롬이 되는 부분을 찾았을 경우,
        # 팰린드롬이 안되던 앞부분만큼 더해주면 됨. 그럼 전체가 팰린드롬이 됨.
        print(len(S) + i)
        break