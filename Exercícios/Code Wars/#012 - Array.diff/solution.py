# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
# 
# It should remove all values from list a, which are present in list b keeping their order.
# 
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
# 
# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
    if b:
        novoA = []
        for valA in a:
            novoA.append(int(valA))
        valoresA = " ".join(novoA)
        for valB in b:
            valoresA= valoresA.replace(str(valB), "")
        
#       print(valoresA.split())
#       # Transforma em lista
#       listaFinal = []
#       for valor in valoresA:
#           listaFinal.append(int(valor))
#       return valoresA.split()
    else:
        return b

print(array_diff([-4, -4, -13, 12, 12, -6, 7], [-19, 10, 19, -1, 0, -3, 15]))

# Não deu ;-;