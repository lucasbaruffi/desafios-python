# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
# 
# The binary number returned should be a string.
# 
# Examples:(Input1, Input2 --> Output (explanation)))
# 
# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)


# Conversão par binário:
    # Dividir por 2
    # O resto será adicionaro ao início do número em binário
    # Dividir o quociente por base 2

def add_binary(a,b):
    quociente = número = a+b # Define o número como a soma, e o quociente apenas para ser maior que 1
    listaResto = [] # abre a lista
    while quociente > 1: # Enquanto o quociente for maior que 1
        resto = número % 2 # Define o resto como o restante da divisão
        listaResto.insert(0, str(resto)) # Adiciona o resto no início da lista - transforma em string
        quociente = número // 2 # Pega o quociente da equaçaõ (resultado)
        número = quociente # define o número como quociente, para não entrar em loop
    listaResto.insert(0, str(quociente)) # Por fim, insere o último quociente o início da lista - transforma em string
    binario = "".join(listaResto)
    print(binario)

add_binary(1,1 )

# Versão do CW:

# def add_binary(a,b):
#     quociente = número = a+b # Define o número como a soma, e o quociente apenas para ser maior que 1
#     listaResto = [] # abre a lista
#     while quociente > 1: # Enquanto o quociente for maior que 1
#         resto = número % 2 # Define o resto como o restante da divisão
#         listaResto.insert(0, str(resto)) # Adiciona o resto no início da lista - transforma em string
#         quociente = número // 2 # Pega o quociente da equaçaõ (resultado)
#         número = quociente # define o número como quociente, para não entrar em loop
#     listaResto.insert(0, str(quociente)) # Por fim, insere o último quociente o início da lista - transforma em string
#     binario = "".join(listaResto)
#     return(binario)
