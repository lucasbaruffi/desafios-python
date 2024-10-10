# Descrição
Implemente a função unique_in_order que toma como argumento uma sequência e devolve uma lista de itens sem qualquer elemento com o mesmo valor próximos uns dos outros e preservando a ordem original dos elementos.

Por exemplo:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]