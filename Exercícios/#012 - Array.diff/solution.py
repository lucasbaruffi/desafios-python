# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
# 
# It should remove all values from list a, which are present in list b keeping their order.
# 
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
# 
# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
# 1 - Passar por cada valor da lista a
# 2 - Passar por cada valor da lista b
    # Se o valor for igual ao da lista a, remove o mesmo
    novoA = []
    novoB = []
    for valA in a:
        novoA.append(str(valA))
    valoresA = "".join(novoA)
    
    for valB in b:
        valoresA.replace(str(valB), "")

    print(valoresA)

print(array_diff([1,2,2,2,3],[1, 2]))