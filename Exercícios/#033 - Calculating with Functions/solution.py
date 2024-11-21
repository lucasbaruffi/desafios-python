# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

def zero(p=0): 
    return p

def one(p=1): 
    return p
def two(): return 2
def three(): return 3
def four(): return 4
def five(): return 5
def six(): return 6

def seven(p=False): 
    if not p:
        return 7
    else:
        return p

def eight(): return 8
def nine(): return 9

def plus(): pass #your code here
def minus(): pass #your code here
def times(p): pass #your code here
def divided_by(): pass #your code here

print(seven())
print(seven(times(five())), 35)