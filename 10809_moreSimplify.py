S = str(input())

for a in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(a), end=' ')
    # find(x) : in 이랑 .index() 합친 거. 찾는 x가 있으면 그 index 값을 반환해줌. 없으면 -1 반환. 시간 복잡도도 O(n)밖에 안됨.