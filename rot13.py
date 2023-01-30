def rot13(message):
    print(message)
    res=""
    for i in message:
        num=ord(i)
        if num<91 and num>64:
            num+=13
            if num>90:
                num-=26
        elif num>96 and num<123:
            num+=13
            if num>122:
                num-=26
        print(chr(num))
        res+=chr(num)
    return res