import math
def idk(num):
    num=num/5
    count=math.floor(num)
    return count, num

def zeros(n):
    count=0
    while n>5:
        a, n= idk(n)
        count+= a
    return count