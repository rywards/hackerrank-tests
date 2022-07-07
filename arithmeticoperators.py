if __name__ == '__main__':
    a = int(input())
    b = int(input())

MAX_VAL = 10000000000
if (a < 1 or b < 1):
    exit()
if (a > MAX_VAL or b > MAX_VAL):
    exit()
print(a+b)
print(a-b)
print(a*b)