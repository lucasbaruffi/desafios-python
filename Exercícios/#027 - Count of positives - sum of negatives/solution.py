# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(lst):
    zeros = 0
    while 0 in lst:
        indice = lst.index(0)
        zeros += 1
        lst.pop(indice)
        print(indice)
    for c in range(0,zeros):
        lst.append(0)
    return lst

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))