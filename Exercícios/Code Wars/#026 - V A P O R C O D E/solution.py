# https://www.codewars.com/kata/5966eeb31b229e44eb00007a/train/python


#V1
def vaporcode(s):
    s = s.upper()
    s = s.replace(" ","")
    s = list(s)
    s = "  ".join(s)
    return s

# V2

def vaporcode(s):
    return "  ".join(list(s.upper().replace(" ","")))


print(vaporcode("Lets go to the movies"))