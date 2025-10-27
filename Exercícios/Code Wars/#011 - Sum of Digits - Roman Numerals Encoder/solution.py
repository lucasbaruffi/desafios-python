# Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.
# 
# Modern Roman numerals are written by expressing each digit separately starting with the leftmost digit and skipping any digit with a value of zero. There cannot be more than 3 identical symbols in a row.
# 
# In Roman numerals:
# 
# 1990 is rendered: 1000=M + 900=CM + 90=XC; resulting in MCMXC.
# 2008 is written as 2000=MM, 8=VIII; or MMVIII.
# 1666 uses each Roman symbol in descending order: MDCLXVI.
# Example:
# 
#    1 -->       "I"
# 1000 -->       "M"
# 1666 --> "MDCLXVI"
# Help:
# 
# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

# 1 - Verificar do maior ao menor


# 1 - I
# 2 - II
# 3 - III
# 4 - IV
# 5 - V
# 6 - VI
# 7 - VII
# 8 - VIII
# 9 - IX



def solution(n):
    
    romanoFinal = ""

    # Se tiver milhar
    if n // 1000:
        milharDecimal = n // 1000
        n = n % 1000
        milharRomano = ("M" * milharDecimal) # Como o desafio vai até 3999, só isso é necessário
        romanoFinal = milharRomano

    # Se tiver centena
    if n // 100:
        centenaDecimal = n // 100 # Pega a Centena, capturando a divisão inteira
        n = n % 100 # Define o restante como o resto da divisão, na variável principal para chegar apenas isso no próximo
        listaCentenaRomano = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] # Lista com as possibilidades
        centenaRomano = listaCentenaRomano[centenaDecimal] # A Localização do decimal dentro da lista
        romanoFinal += centenaRomano # Adiciona ao main

    # Se tiver decimal
    if n // 10:
        dezenaDecimal = n // 10
        n = n % 10
        listaDecimalRomano = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        decimalRomano = listaDecimalRomano[dezenaDecimal]
        romanoFinal += decimalRomano

    # Se tiver Unidade
    unidadeDecimal = n
    listaUnidadeRomano = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    unidadeRomano = listaUnidadeRomano[unidadeDecimal]
    romanoFinal += unidadeRomano
    return romanoFinal

print(solution(1666))