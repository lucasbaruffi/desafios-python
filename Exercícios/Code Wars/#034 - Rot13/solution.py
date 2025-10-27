# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

alfabeto = [ "a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", 
            "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", 
            "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z" ]

def rot13(message): 
    palavra = ""
    for letra in message:
        if letra in alfabeto:
            posFinal = alfabeto.index(letra) + 26
            if posFinal >= 52:
                posFinal -= 52
            letra = alfabeto[posFinal]
        palavra = palavra+letra
    return palavra
