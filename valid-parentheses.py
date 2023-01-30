def Convert(string):
    l=[]
    l[:0]=string
    return l

def valid_parentheses(string):
    count=0
    l=Convert(string)
    for i in l: 
        if i=="(":
            count+=1
        elif i==")":
            count-=1
            if count<0:
                return False
    if count == 0:
        return True
    else:    
        return False