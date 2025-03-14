import sys
input_data = sys.stdin.readline

string1 = input_data().rstrip()
string2 = input_data().rstrip()

len1 = len(string1)
len2 = len(string2)

# dp[i][j] = string1의 앞 i글자와 string2의 앞 j글자를 이용했을 때 
# 얻을 수 있는 LCS의 최대 길이
dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

def backtrack_lcs(string1, string2, dp):
    """
    dp 테이블(길이 정보)에서 시작해, (len(string1), len(string2)) 지점부터
    역추적하여 LCS 문자열을 구한다.
    """
    i, j = len(string1), len(string2)
    lcs_chars = []
    
    while i > 0 and j > 0:
        # 같은 문자면 LCS의 일부 → 왼쪽 위(i-1, j-1)로 이동
        if string1[i - 1] == string2[j - 1]:
            lcs_chars.append(string1[i - 1])
            i -= 1
            j -= 1
        # 다르면 dp 값을 비교해 더 큰 쪽(즉, 공통 부분이 긴 쪽)으로 이동
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
    
    # 역추적하면서 문자를 뒤에서부터 모았으므로 뒤집어서 반환
    return "".join(reversed(lcs_chars))

# 1) dp 테이블 채우기(길이 정보만 저장)
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if string1[i - 1] == string2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# 2) LCS 길이
lcs_length = dp[len1][len2]
print(lcs_length)

# 3) 역추적을 통해 LCS 문자열 구하기
if lcs_length > 0:
    lcs_string = backtrack_lcs(string1, string2, dp)
    print(lcs_string)