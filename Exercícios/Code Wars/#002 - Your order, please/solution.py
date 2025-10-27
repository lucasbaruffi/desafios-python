# Your task is to sort a given string. Each word in the string will contain a single number. 
# This number is the position the word should have in the result.
# 
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# 
# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
# 
# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

def order(sentence): 
    frase = {}
    if not sentence:  # Verifique se há algo, caso contrário retorne uma strig vazia
        return ""
    else:
        palavras = sentence.split() # Divide a frase em palavras,
        for palavra in palavras: # Para cada palavra
            for letra in palavra: # Para cada letra
                if letra.isnumeric(): #  verifique se é um número
                    num = int(letra) # Transforma o número em inteiro
                    frase[palavra] = num-1 # Insere na posição certa da frase
        frase_arrumada = []
        for p in sorted(frase, key = frase.get): # De alguma forma isso funciona
            frase_arrumada.append(p)
        frase_arrumada = " ".join(frase_arrumada)
        print(frase_arrumada)
order("4of Fo1r pe6ople g3ood th5e the2")

# Versão para o CW:

# def order(sentence): 
#     frase = {}
#     if not sentence:  # Verifique se há algo, caso contrário retorne uma strig vazia
#         return ""
#     else:
#         palavras = sentence.split() # Divide a frase em palavras,
#         for palavra in palavras: # Para cada palavra
#             for letra in palavra: # Para cada letra
#                 if letra.isnumeric(): #  verifique se é um número
#                     num = int(letra) # Transforma o número em inteiro
#                     frase[palavra] = num-1 # Insere na posição certa da frase
#         frase_arrumada = []
#         for p in sorted(frase, key = frase.get):
#             frase_arrumada.append(p)
#         frase_arrumada = " ".join(frase_arrumada)
#         return(frase_arrumada)