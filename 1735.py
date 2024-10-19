A, B = map(int, input().split())
C, D = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

low_gcd = lcm(B, D)
# print(low_gcd)
multiplier_B = low_gcd // B
multiplier_D = low_gcd // D

sum_high = A * multiplier_B + C * multiplier_D
sum_low = B * multiplier_B

gcd_sum = gcd(sum_high, sum_low)

print(sum_high // gcd_sum, sum_low // gcd_sum)