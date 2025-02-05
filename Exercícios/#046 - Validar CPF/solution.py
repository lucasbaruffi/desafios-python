# O objetivo aqui é criar um código que receba um CPF e retorne se é válidou ou inválido.

cpf = "79662289088"
cpf_verificado = ""

# Separa os dígitos
for n in range(0,9):
    cpf_verificado += cpf[n]


for n in range(0,2):
    # Soma os digitos
    soma_digitos = 0
    verificador = 0

    for cont, n in enumerate(cpf_verificado):
        soma_digitos += int(n) * (len(cpf_verificado) + 1 - cont) # Contagem decrescente
    verificador = 11 - (soma_digitos % 11)
    
    if verificador >= 10:
        cpf_verificado += "0"
    else:
        cpf_verificado += str(verificador)

if cpf == cpf_verificado:
    print("CPF Válido!")
else:
    print(f"""CPF Inválido!
CPF correto: {cpf_verificado}""")
