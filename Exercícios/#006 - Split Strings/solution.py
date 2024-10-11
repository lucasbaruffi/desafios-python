# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
# 
# Examples:
# 
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

def solution(s):
    lista = []
    listaFinal = []
    if len(s) % 2 == 1: # Adiciona _ no final se for Impar
        s = s + "_"
    for letra in s: # Transforma em uma lista
        lista.append(letra)   
    for n, letra in enumerate(lista):
        if n % 2 == 0:
             duas_letras = f"{letra}{lista[n+1]}"
             listaFinal.append(duas_letras)
    print(listaFinal)

solution("abcdef")

# Solução CW:

def solution(s):
    lista = []
    listaFinal = []
    if len(s) % 2 == 1: # Adiciona _ no final se for Impar
        s = s + "_"
    for letra in s: # Transforma em uma lista
        lista.append(letra)   
    for n, letra in enumerate(lista):
        if n % 2 == 0:
             duas_letras = f"{letra}{lista[n+1]}"
             listaFinal.append(duas_letras)
    return(listaFinal)
