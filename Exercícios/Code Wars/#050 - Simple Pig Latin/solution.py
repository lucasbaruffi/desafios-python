# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

def pig_it(text:str):
    alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

    newText = []

    for word in text.split(" "):
        for c, letter in enumerate(word):

            # Verifica se é uma letra
            if not letter in alphabet:
                continue
            
            if c == 0:
                word = word.removeprefix(letter) + letter + "ay"

        newText.append(word)    
    
    return " ".join(newText)

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
