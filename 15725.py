polynom = str(input())

idx_x = polynom.find('x')
if idx_x == -1:
    print(0)
else:
    coeff = polynom[:idx_x]
    if not coeff:
        print(1)
    elif coeff == '-': # 계수가 마이너스일 경우. 문제에서 마이너스 범위도 된다고 말하진 않았는데, '절대값'이 10000을 넘지 않는다고 한 것으로 보아 마이너스도 있는 것으로 보임. 애초에 n이 자연수라고 말하지도 않았으니.
        print(-1)
    else:
        print(coeff)