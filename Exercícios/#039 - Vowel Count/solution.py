# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

def get_count(sentence):
    cont = 0
    for letter in sentence:
        if letter in "aeiou":
            cont += 1
    return cont
