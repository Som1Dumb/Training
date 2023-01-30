import math 

def isPP(n):
    a=2
    max=math.sqrt(n)
    while a<=max:
        i=2
        while a**i<=n:
            if a**i==n:
                return [a,i]
            else: 
                i+=1
        a+=1