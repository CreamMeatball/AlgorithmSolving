string = str(input())

is_Palindrome = True

for i in range(0, len(string)//2):
    if string[i] == string[-1-i]:
        continue
    else:
        is_Palindrome = False
        break
    
if is_Palindrome:
    print(1)
else:
    print(0)
    