# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python


def decToHex(v):
    conv = {
     0: "0",
     1: "1",
     2: "2",
     3: "3",
     4: "4",
     5: "5",
     6: "6",
     7: "7",
     8: "8",
     9: "9",
     10: "A",
     11: "B",
     12: "C",
     13: "D",
     14: "E",
     15: "F"
     }
    return conv[v]

def toHex(n):
    if n < 0:
        return "00"
    
    elif n > 255:
        return "FF"

    elif n < 16:
        return decToHex(n).zfill(2)

    else:
        divInt = []
        while True:
            if n < 16:
                divInt.append(n)
                break
            divInt.append(n % 16)
            n = n // 16
        divInt.reverse()

        valFinal = ""
        for num in divInt:
            valFinal += decToHex(num)
        return valFinal

def rgb(r, g, b):
    return f"{toHex(r)}{toHex(g)}{toHex(b)}"


print(rgb(0, 0, 0), "000000", "testing zero values")
print(rgb(1, 2, 3), "010203", "testing near zero values")
print(rgb(255, 255, 255), "FFFFFF", "testing max values")
print(rgb(254, 253, 252), "FEFDFC", "testing near max values")
print(rgb(-20, 275, 125), "00FF7D", "testing out of range values")

