# Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.
# 
# The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.
# 
# For Sudoku rules, see the Wikipedia article.
# 
# puzzle = [[5,3,0,0,7,0,0,0,0],
#           [6,0,0,1,9,5,0,0,0],
#           [0,9,8,0,0,0,0,6,0],
#           [8,0,0,0,6,0,0,0,3],
#           [4,0,0,8,0,3,0,0,1],
#           [7,0,0,0,2,0,0,0,6],
#           [0,6,0,0,0,0,2,8,0],
#           [0,0,0,4,1,9,0,0,5],
#           [0,0,0,0,8,0,0,7,9]]
# 
# sudoku(puzzle)
# # Should return
#  [[5,3,4,6,7,8,9,1,2],
#   [6,7,2,1,9,5,3,4,8],
#   [1,9,8,3,4,2,5,6,7],
#   [8,5,9,7,6,1,4,2,3],
#   [4,2,6,8,5,3,7,9,1],
#   [7,1,3,9,2,4,8,5,6],
#   [9,6,1,5,3,7,2,8,4],
#   [2,8,7,4,1,9,6,3,5],
#   [3,4,5,2,8,6,1,7,9]]


import random
def miniSudoku(puzzle):
    originPuzzle = puzzle.copy()
    # Randomiza um número
    sorteados = 0

    while True:
        sort = random.randrange(0,9)
        #print(f'Número Sorteado:{sort}')
        sorteados += 1
        # Que naõ esteja na linha
        if sort not in puzzle:
            #print(f'Número Aceito:{sort}')

            posição = puzzle.index(0)
            #print(f"A posição do primeiro 0 é {posição}")

            puzzle.pop(posição)

            puzzle.insert(posição, sort)
            #print(puzzle)
        
        if sum(puzzle) == 45:
            print(f"Entrou: {originPuzzle}")
            print(f"Solução: {puzzle}")
            print(f"Tentativas: {sorteados}")

            break
    






puzzle = [5,3,0,6,0,0,0,9,8]
puzzle = miniSudoku(puzzle)












# def sudoku(puzzle):
#     groups = {}
#     for contLinha, linha in enumerate(puzzle):
#        # groups[f'Coluna{contLinha+1}'] = 
#         for contValor, valor in enumerate(linha):
#             print(linha[contLinha][contValor]
# )
# 
#     print(groups)
# 

#def sudoku(puzzle):
#    coluna1 = []
#    coluna2 = []
#    coluna3 = []
#    coluna4 = []
#    coluna5 = []
#    coluna6 = []
#    coluna7 = []
#    coluna8 = []
#    coluna9 = []
#    
#    grupo1 = []
#    grupo2 = []
#    grupo3 = []
#    grupo4 = []
#    grupo5 = []
#    grupo6 = []
#    grupo7 = []
#    grupo8 = []
#    grupo9 = []
#    
#    # Define as colunas e grupos
#    for contLinha, linha in enumerate(puzzle):
#        coluna1.append(linha[0])
#        coluna2.append(linha[1])
#        coluna3.append(linha[2])
#        coluna4.append(linha[3])
#        coluna5.append(linha[4])
#        coluna6.append(linha[5])
#        coluna7.append(linha[6])
#        coluna8.append(linha[7])
#        coluna9.append(linha[8])
#            
#        
#    
#    
#    
#    
#
#    return puzzle
#
#
# puzzle = [[5,3,0,0,7,0,0,0,0],
#           [6,0,0,1,9,5,0,0,0],
#           [0,9,8,0,0,0,0,6,0],
#           [8,0,0,0,6,0,0,0,3],
#           [4,0,0,8,0,3,0,0,1],
#           [7,0,0,0,2,0,0,0,6],
#           [0,6,0,0,0,0,2,8,0],
#           [0,0,0,4,1,9,0,0,5],
#           [0,0,0,0,8,0,0,7,9]]
# # 
# puzzle = sudoku(puzzle)
#
#print(f"{puzzle[0][0]} {puzzle[0][1]} {puzzle[0][2]} | {puzzle[0][3]} {puzzle[0][4]} {puzzle[0][5]} | {puzzle[0][6]} {puzzle[0][7]} {puzzle[0][8]}")
#print(f"{puzzle[1][0]} {puzzle[1][1]} {puzzle[1][2]} | {puzzle[1][3]} {puzzle[1][4]} {puzzle[1][5]} | {puzzle[1][6]} {puzzle[1][7]} {puzzle[1][8]}")
#print(f"{puzzle[2][0]} {puzzle[2][1]} {puzzle[2][2]} | {puzzle[2][3]} {puzzle[2][4]} {puzzle[2][5]} | {puzzle[2][6]} {puzzle[2][7]} {puzzle[2][8]}")
#print("-"*22)
#print(f"{puzzle[3][0]} {puzzle[3][1]} {puzzle[3][2]} | {puzzle[3][3]} {puzzle[3][4]} {puzzle[3][5]} | {puzzle[3][6]} {puzzle[3][7]} {puzzle[3][8]}")
#print(f"{puzzle[4][0]} {puzzle[4][1]} {puzzle[4][2]} | {puzzle[4][3]} {puzzle[4][4]} {puzzle[4][5]} | {puzzle[4][6]} {puzzle[4][7]} {puzzle[4][8]}")
#print(f"{puzzle[5][0]} {puzzle[5][1]} {puzzle[5][2]} | {puzzle[5][3]} {puzzle[5][4]} {puzzle[5][5]} | {puzzle[5][6]} {puzzle[5][7]} {puzzle[5][8]}")
#print("-"*22)
#print(f"{puzzle[6][0]} {puzzle[6][1]} {puzzle[6][2]} | {puzzle[6][3]} {puzzle[6][4]} {puzzle[6][5]} | {puzzle[6][6]} {puzzle[6][7]} {puzzle[6][8]}")
#print(f"{puzzle[7][0]} {puzzle[7][1]} {puzzle[7][2]} | {puzzle[7][3]} {puzzle[7][4]} {puzzle[7][5]} | {puzzle[7][6]} {puzzle[7][7]} {puzzle[7][8]}")
#print(f"{puzzle[8][0]} {puzzle[8][1]} {puzzle[8][2]} | {puzzle[8][3]} {puzzle[8][4]} {puzzle[8][5]} | {puzzle[8][6]} {puzzle[8][7]} {puzzle[8][8]}")