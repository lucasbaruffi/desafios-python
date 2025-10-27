# https://www.codewars.com/kata/5518a860a73e708c0a000027/train/python

def last_digit(lst):
    lst.reverse()
    totSum = 0
    for contNum, num in enumerate(lst):
        if contNum == 0:
            totSum = pow(lst[contNum+1], num)
        elif contNum == len(lst)-1:
            pass
        else:
            totSum = pow(lst[contNum+1], totSum)
        
    totSum = str(totSum)
    ultimo = totSum[-1]
    return(ultimo)
    

last_digit([3, 4, 2])