# https://www.codewars.com/kata/57f609022f4d534f05000024/train/python

def stray(arr):
    for num in arr:
        cont = arr.count(num)
        if cont == 1:
            return num

print(stray([2, 3, 2, 2, 2]))