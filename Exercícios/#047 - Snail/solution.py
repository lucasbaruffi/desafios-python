# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

def snail(snail_map):
    resultado = []
    pos_vistas = []
    x = y = 0
    tamanho = len(snail_map)-1

    while True:
        pos_vistas.append(f"{str(x)}{str(y)}") # Salva posições vistas
        print(snail_map[x][y])
        resultado.append(snail_map[x][y])

        direita = y + 1
        esquerda = y - 1
        cima = x - 1
        baixo = x + 1

        if direita <= tamanho and f"{str(x)}{str(direita)}" not in pos_vistas:
            y += 1
            print("Foi para a Direita")

        elif baixo <= tamanho and f"{str(baixo)}{str(y)}" not in pos_vistas:
            x += 1       
            print("Foi para Baixo")

        elif esquerda >= 0 and f"{str(x)}{str(esquerda)}" not in pos_vistas:
            y -= 1    
            print("Foi para a Esquerda")    

        elif cima >= 0 and f"{str(cima)}{str(y)}" not in pos_vistas:
            x -= 1    
            print("Foi para Cima")    

        else:
            break
    print(resultado)

array = [[1,2,3,4],
         [8,9,4,5],
         [7,6,5,6],
         [10,11,12,13]]

expected = [1,2,3,6,9,8,7,4,5]

snail(array)