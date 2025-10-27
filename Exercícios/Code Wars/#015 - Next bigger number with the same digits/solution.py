# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:
# 
#   12 ==> 21
#  513 ==> 531
# 2017 ==> 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):
# 
#   9 ==> -1
# 111 ==> -1
# 531 ==> -1

def next_bigger(n):
    listaOrignal = []
    for alg in str(n):
        listaOrignal.append(int(alg))

    listaInversa = listaOrignal.copy()
    listaInversa.reverse()

    valoresEsq = []
    for index, num in enumerate(listaInversa):
        if index == 0:
            valoresEsq.append(num)
        else:
            for valores in valoresEsq:
                if valoresEsq[valores]
        print(listaInversa[index])

    pass
# Procurar o primeiro número (<-) que seja menor que UM dos números anteriores (da direita)
# Procurar o núero que seja maior que seu anterior (da direita para esquerda) e subsituir um pelo outro

# 1- Identificar, da Direita para a Esquerda, o primeiro número que seja maior que seus anteriores (da direita)
    # Para isso, cada número que passar, adiciona em uma lista com o append

# 2- Tendo identificado, separo, dos adicionados na lista, 


next_bigger(34971)

# Não foi