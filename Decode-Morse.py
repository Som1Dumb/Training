def remove_beginning_end(li):
    x=0
    while x<len(li):
        if li[0]=='':
            li.pop(0)
        else:
            x+=1
        if li[-1]=='':
            li.pop(-1)
        else:
            x+=1
    return li
    

def check_list(li):
    print('11')
    x=0
    while x<len(li):
        if li[x]==' ' and li[x-1]==' ':
            li.pop(x)
        x+=1
    print(li)
    return li

def decode_morse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    li=morse_code.split(" ")
    print(li)
    li=remove_beginning_end(li)
    print(li)
    li2=[]
    i=0
    while i<len(li): 
        mors=li[i]
        if mors=='':
            word=' '
        else:
            word=MORSE_CODE[mors]
        li2.append(word)
        i+=1
        
    print(li2)
    res=""
    x=0
    li3=check_list(li2)
    while x< len(li3):
        res+=li3[x]
        x+=1
    print(res)
    return res