def generate_hashtag(s):
    if s==''or len(s)>139:
        return False
    tit=s.title()
    space_check=tit.find(" ",)
    if space_check>-1:
        #has space
        almost=tit.split(" ")
        res="#"
        for i in almost:
            res+=i
        
    else:
        #does not have space
        res="#"+tit
    print(res)
    return res