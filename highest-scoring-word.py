def high(x):
    # Code here
    li=x.split(" ")
    i=0
    count=0
    res=""
    while i<len(li):
        num=0
        for element in li[i]:
            num+=ord(element)-96
        if num>count:
            count=num
            res=li[i]
        i+=1
    return res