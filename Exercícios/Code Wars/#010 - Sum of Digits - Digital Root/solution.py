# Given n, take the sum of the digits of n. 
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
# The input will be a non-negative integer.
# 
# Examples
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

# 1 - Verificar se possui mais de um algarismo
    # Se sim, seguir o fluxo abaixo:
# 2 - Soma os algarismos
# Repete até possuir apenas um algarismo

def digital_root(n):  
    while len(str(n)) > 1: # Verificar se possui mais de um algarismo
        soma = 0
        for algarismo in str(n):
            soma += int(algarismo)
        n = soma
    return n

print(digital_root(132189))