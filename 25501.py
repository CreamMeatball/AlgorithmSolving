def recursion(sentence, start, end):
    global count
    count += 1
    if start >= end:
        return 1
    elif (sentence[start] != sentence[end]):
        return 0
    else:
        return recursion(sentence, start+1, end-1)

def isPalindrome(sentence):
    return recursion(sentence, 0, len(sentence)-1)

count = 0

T = int(input())

for _ in range(T):
    sentence = input()
    print(isPalindrome(sentence), end=' ')
    print(count)
    count = 0