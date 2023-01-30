def change_to_string(st):
    li=st.split(' ')
    x=1
    while x<len(li):
        word=li[x]
        new_word=word.capitalize()
        li[x]=new_word
        x+=1
    res=''
    for x in li:
        res+=x
    return res

def to_camel_case(text):
    #your code here
    aa=''
    bb=''
    res=''
    for x in range(1,len(text)):
        aa=text.replace('-',' ')
        
    for x in range(1,len(text)):
        bb=aa.replace('_',' ')
    cc=change_to_string(bb)
    return cc