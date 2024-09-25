def decimal_to_base(n, base):
    if n == 0:
        return "0"
    
    digits = []
    while n:
        remainder = n % base
        if remainder < 10:
            digits.append(str(remainder))
        else:
            digits.append(chr(remainder + 55))
        n //= base  # n을 base로 나눈 몫을 n에 다시 할당

    return ''.join(digits[::-1])

# 입력 받기
number, scale = map(int, input().split())

# 변환
converted_number = decimal_to_base(number, scale)

# 결과 출력
print(converted_number)