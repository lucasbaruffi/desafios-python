cpf = "145.382.206-20"

cpf = cpf.replace(".","").replace("-","")

validador_1 = cpf[9]
validador_2 = cpf[10]


soma_digitos = 0
for n in range(0,9):
    soma_digitos += int(cpf[n]) * (len(cpf)-1-n)

resto = soma_digitos % 11

valor_final = 11-resto

if valor_final < 10:
    validador_correto_1 = valor_final
else:
    validador_correto_1 = 0

soma_digitos = 0
for n in range(0,19):
    soma_digitos += int(cpf[n]) * (len(cpf)-1-n)

resto = soma_digitos % 11

valor_final = 11-resto




print(valor_final)