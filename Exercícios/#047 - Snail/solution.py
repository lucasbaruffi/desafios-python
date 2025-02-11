# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

def snail(snail_map):
    resultado = []
    pos_vistas = []
    x = y = 0
    tamanho = len(snail_map)-1

    while True:
        pos_vistas.append(f"{str(x)}{str(y)}") # Salva posições vistas


        while y+1 <= tamanho:
            if f"{str(x)}{str(y+1)}" not in pos_vistas:
                print(snail_map[x][y+1])
                y += 1

        while x+1 <= tamanho:           
            print(snail_map[x+1][y])
            x += 1

        while y-1 >= 0:  
            if f"{str(x)}{str(y-1)}" not in pos_vistas:         
                print(snail_map[x][y-1])
                y -= 1

        while x-1 >= 0:           
            print(snail_map[x-1][y])
            x -= 1


        break

        



array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

expected = [1,2,3,6,9,8,7,4,5]

snail(array)