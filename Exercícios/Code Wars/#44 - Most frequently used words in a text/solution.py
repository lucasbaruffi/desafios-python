# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python

def top_3_words(text):
    formatText = ""
    text = text.lower()
    for cont, caractere in enumerate(text):
        if caractere.isalnum() :
            formatText += caractere
        elif caractere == " ":
            formatText += caractere
        elif caractere == "'" and (text[cont+1].isalnum() or text[cont-1].isalnum()):
            formatText += caractere

    listText = formatText.split()

    contDict = {}

    for palavra in listText:
        if palavra not in contDict.keys():
            contDict[palavra] = 1
        else: 
            contDict[palavra] += 1

    contDict = dict(sorted(contDict.items(), key=lambda item: item[1], reverse=True))
    
    finalDict = []
    cont = 0
    for palavra in contDict:
        if cont < 3:
            finalDict.append(palavra)
            cont +=1

    return finalDict
print(top_3_words("a a a  b  c c  d' d d d  e e e e e"), ["e", "d", "a"])
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
print(top_3_words("  //wont won't won't "), ["won't", "wont"])
print(top_3_words("  , e   .. "), ["e"])
print(top_3_words("  ...  "), [])
print(top_3_words("  '  "), [])
print(top_3_words("  '''  "), [])
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])

print("1".isalpha())