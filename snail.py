def snail(snail_map):
    res=[]
    count=0
    x=0
    y=0
    maxnum=len(snail_map)-1 #max value of x and y
    minnum=0 #minimum value of x and y
    numchanged=False
    while len(res)<len(snail_map[0])**2:
        if numchanged==False:
            res.append(snail_map[y][x])
        else:
            numchanged=False
        num=count%4
        if num==0:
            if x==maxnum:
                count+=1
                numchanged=True
            else:
                x+=1
        if num==1:
            if y==maxnum:
                count+=1
                maxnum-=1
                numchanged=True
            else:
                y+=1
        if num==2:
            if x==minnum:
                count+=1
                minnum+=1
                numchanged=True
            else:
                x-=1
        if num==3:
            if y==minnum:
                count+=1
                
                numchanged=True
            else:
                y-=1
    return res    