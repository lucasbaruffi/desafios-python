# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(seq):
    for item in seq:
        if seq.count(item) % 2:
            return item

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
