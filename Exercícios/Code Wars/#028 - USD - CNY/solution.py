# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python

def count_positives_sum_negatives(arr):
    contPos = sumNeg = 0
    for num in arr:
        if num > 0:
            contPos += 1
        elif num < 0:
            sumNeg += num
    return [contPos, sumNeg] if arr else []

print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))