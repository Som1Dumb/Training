def find_uniq(arr):
    # your code here
    tested=[]
    for i in arr:
        if tested.count(i)==0:
            if arr.count(i)==1:
                return i   # n: unique number in the array
            else:
                tested.append(i)