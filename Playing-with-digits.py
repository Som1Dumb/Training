def dig_pow(n, p):
    # your code
    li = [int(x) for x in str(n)]
    i=0
    num=0
    while i<len(li):
        num+=li[i]**p
        i+=1
        p+=1
    checked=num/n
    if checked%1!=0:
        return -1
    else:
        return checked