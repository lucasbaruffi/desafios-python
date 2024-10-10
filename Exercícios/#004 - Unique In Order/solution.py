# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
# 
# For example:
# 
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

def unique_in_order(sequence):
    letraAntiga = ""
    lista = []
    for letra in sequence:
        if letra != letraAntiga:
            lista.append(letra)
        letraAntiga = letra
    print(lista)

unique_in_order((1, 2, 2, 3, 3))

# Versão CW:

# def unique_in_order(sequence):
#     letraAntiga = ""
#     lista = []
#     for letra in sequence:
#         if letra != letraAntiga:
#             lista.append(letra)
#         letraAntiga = letra
#     return(lista)