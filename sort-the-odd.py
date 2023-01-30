def is_odd (num):
    if num%2==0:
        return False
    else:
        return True
    
def num_swap (list, num1, num2):
    list[num1], list[num2] = list[num2], list[num1]
    return list

def check_list (list):
    print(list)
    i=0
    n=-1
    swapped=False
    while i<len(list):
        if is_odd(list[i]):
            if n==-1:
                n=i
                swapped=False
            elif list[n]>list[i]:
                num_swap(list, n, i)
                n=i
                swapped=True
            else:
                n=i
        i+=1
    
    return list, swapped
            

def sort_array(source_array):
    # Return a sorted array.
    if len(source_array)==0:
        return source_array
    check=True
    while check==True:
        source_array,check=check_list(source_array)
    return source_array
                