# Recebe um número de 1 a 26 e retorna uma lista com as letras, 2 = ["A", "B"]

def qual_a_letra(n):
    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    res = []

    for n in range(0, n):
        res.append(alfabeto[n])

    return res
print(qual_a_letra(1))