# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

def dir_reduc(arr):
    palavras = " ".join(arr)
    while "EAST WEST" in palavras or "NORTH SOUTH" in palavras or "WEST EAST" in palavras or "SOUTH NORTH" in palavras:
        palavras = palavras.replace("EAST WEST","").replace("NORTH SOUTH","").replace("WEST EAST","").replace("SOUTH NORTH","")
        palavras = palavras.split()
        palavras = " ".join(palavras)
    return palavras.split()





a = ['EAST', 'SOUTH', 'NORTH', 'NORTH', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'WEST', 'EAST', 'WEST', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH']
print(dir_reduc(a), ['WEST'])
    

# ['EAST', 'EAST', 'EAST', 'SOUTH', 'WEST', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH'] should equal ['EAST', 'EAST', 'EAST', 'SOUTH', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH']

# ['EAST', 'EAST', 'EAST', 'SOUTH', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH']