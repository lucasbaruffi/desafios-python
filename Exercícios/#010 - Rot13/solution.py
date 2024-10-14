# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. 
# ROT13 is an example of the Caesar cipher.
# 
# Create a function that takes a string and returns the string ciphered with Rot13. 
# If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
# 
# Please note that using encode is considered cheating.

alfabeto = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]

def rot13(message): 
    for letra in message:
        if letra in alfabeto:
            pos = alfabeto.index(letra) + 13
            if pos > 26:
                pos -= 26
            novaLetra = alfabeto[pos]
            print(novaLetra)
        else:
            print(letra)
#    print(alfabeto.index("g"))
#   for letra in message:
#       if letra in alfabeto:
#           print(letra)
#
rot13("abcz123@")