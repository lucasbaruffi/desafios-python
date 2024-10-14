# Complete the solution so that the function will break up camel casing, using a space between words.
# 
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    frase = ""
    for letra in s:
        if letra.isupper():
            frase = f"{frase} {letra}"
        else:
            frase = f"{frase}{letra}"
    print(frase)

solution("camelCasing")

# Para o CW:

def solution(s):
    frase = ""
    for letra in s:
        if letra.isupper():
            frase = f"{frase} {letra}"
        else:
            frase = f"{frase}{letra}"
    return(frase)