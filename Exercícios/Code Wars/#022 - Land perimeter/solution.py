# Given an array arr of strings, complete the function by calculating the total perimeter of all the islands. Each piece of land will be marked with 'X' while the water fields are represented as 'O'. Consider each tile being a perfect 1 x 1 piece of land. Some examples for better visualization:
# 
# ['XOOXO',
#  'XOOXO',
#  'OOOXO',
#  'XXOXO',
#  'OXOOO'] 
# which represents:
# 
# should return: "Total land perimeter: 24".
# 
# Following input:
# 
# ['XOOO',
#  'XOXO',
#  'XOXO',
#  'OOXX',
#  'OOOO']
# which represents:
# 
# should return: "Total land perimeter: 18"

def land_perimeter(arr):
    terTotal = perTotal = 0
    for posLinha, linha in enumerate(arr):
        for posBloco, bloco in enumerate(linha):
            if bloco == "X":
                terTotal += 1
                
                # Se não for o da direita e a direita tiver preenchido:
                if posBloco < (len(linha)-1): 
                    if linha[posBloco+1] == "X":
                        perTotal -= 1
                        print(f"Menos 1 a Direita de X = {posLinha+1} Y = {posBloco+1}")

                # Se não for o primeiro e a esquerda tiver preenchido:
                if posBloco > 0: 
                    if linha[posBloco-1] == "X":
                        perTotal -= 1
                        print(f"Menos 1 a Esquerda de X = {posLinha+1} Y = {posBloco+1}")

                # Se não for o primeiro e em cima tiver preenchido:
                if posLinha > 0:
                    if arr[posLinha-1][posBloco] == "X":
                        perTotal -= 1                    
                        print(f"Menos 1 Acima de X = {posLinha+1} Y = {posBloco+1}")

                # Se não for a última linha e em baixo tiver preenchido:
                if posLinha < (len(arr)-1): 
                    if arr[posLinha+1][posBloco] == "X":
                        perTotal -= 1 
                        print(f"Menos 1 Abaixo de X = {posLinha+1} Y = {posBloco+1}")

    print(f"Área Total: {terTotal}")
    print(f"Perímetro Total: {terTotal*4}")
    perTotal += terTotal * 4
    print(f"Perímetro Final: {perTotal}")
    return  perTotal


land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"])

#  Para o CW:

def land_perimeter(arr):
    terTotal = perTotal = 0
    for posLinha, linha in enumerate(arr):
        for posBloco, bloco in enumerate(linha):
            if bloco == "X":
                terTotal += 1
                
                # Se não for o da direita e a direita tiver preenchido:
                if posBloco < (len(linha)-1): 
                    if linha[posBloco+1] == "X":
                        perTotal -= 1

                # Se não for o primeiro e a esquerda tiver preenchido:
                if posBloco > 0: 
                    if linha[posBloco-1] == "X":
                        perTotal -= 1

                # Se não for o primeiro e em cima tiver preenchido:
                if posLinha > 0:
                    if arr[posLinha-1][posBloco] == "X":
                        perTotal -= 1                    

                # Se não for a última linha e em baixo tiver preenchido:
                if posLinha < (len(arr)-1): 
                    if arr[posLinha+1][posBloco] == "X":
                        perTotal -= 1 

    perTotal += terTotal * 4
    return  f"Total land perimeter: {perTotal}"