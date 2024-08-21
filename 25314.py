import sys

N = int(sys.stdin.readline().rstrip())

if(N%4 == 0):
    print("long " * (N//4) + "int")
else:
    print("long " * (N//4 + 1) + "int")