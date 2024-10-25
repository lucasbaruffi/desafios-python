# Your job is to write a function which increments a string, to create a new string.
# 
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:
# 
# foo -> foo1
# 
# foobar23 -> foobar24
# 
# foo0042 -> foo0043
# 
# foo9 -> foo10
# 
# foo099 -> foo100
# 
# Attention: If the number has leading zeros the amount of digits should be considered.

def increment_string(strng):
    # Se não for vazia
    numbers = invertedNumber =  ""
    if strng:
        # So último caractere for um número
        if strng[-1] in "0123456789":
            stReversa = "".join((reversed(strng)))
            for char in stReversa:
                if char in "0123456789":
                    numbers = char + numbers
                    invertedNumber = numbers + char
                else:
                    break
            print(invertedNumber, strng)
            tam = len(numbers)
            numbers = int(numbers) + 1
            numbers = str(numbers).zfill(tam)
            print(numbers)





 
        # Se não tiver um número no final    
        else:
            return strng + "1"
    # Se a string for vazia:
    else:
        return "1"
print(increment_string("Fo1o0023"))













#     números = []
#     letras = ""
#     letrasReversed = reversed(strng)
#     print(letrasReversed)
#     for letra in strng:
#         if letra in "0123456789":
#             números.append(letra)
#         else:
#             letras += letra
#     if números:
#         num = "".join(números)
#         tam = len(num)
#         num = int(num)
#         num += 1
#         novoNumero = (str(num).zfill(tam))
#         novaStr = letras + str(novoNumero)
#         return novaStr
#     else:
#         return strng + "1"
# print(increment_string("fo99obar99"))