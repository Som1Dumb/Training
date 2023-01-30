def find_nb(m):
    # your code
    i=1 
    num=0
    while num<m:
        num+=i**3
        i+=1
    if num==m:
        return i-1
    else:
        return -1