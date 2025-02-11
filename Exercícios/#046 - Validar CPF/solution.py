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


{
    "id_origem_cliente": 50,
    "descricao": "01 - Call - Ativo"
},
{
    "id_origem_cliente": 51,
    "descricao": "02 - Call - Receptivo"
},
{
    "id_origem_cliente": 41,
    "descricao": "03 - PAP - Próprio"
},
{
    "id_origem_cliente": 87,
    "descricao": "04 - Loja - Ativo"
},
{
    "id_origem_cliente": 86,
    "descricao": "05 - Loja - Online"
},
{
    "id_origem_cliente": 18,
    "descricao": "06 - Loja - Receptivo"
},
{
    "id_origem_cliente": 25,
    "descricao": "07 - Indicação"
},
{
    "id_origem_cliente": 49,
    "descricao": "10 - Call - Online"
},
{
    "id_origem_cliente": 56,
    "descricao": "11 - Call - Facebook/Instagram"
},
{
    "id_origem_cliente": 57,
    "descricao": "12 - Call - Google"
},
{
    "id_origem_cliente": 94,
    "descricao": "13 - PAP - Terceirizado"
},
{
    "id_origem_cliente": 103,
    "descricao": "14 - Ponto de Revenda"
},
{
    "id_origem_cliente": 108,
    "descricao": "16 - Call - TikTok"
},
{
    "id_origem_cliente": 52,
    "descricao": "20 - ActionCall"
},
{
    "id_origem_cliente": 93,
    "descricao": "21 - UPcall"
},
{
    "id_origem_cliente": 60,
    "descricao": "30 - B2B"
},
{
    "id_origem_cliente": 55,
    "descricao": "31 - Licitação / Pregão - Público"
},
{
    "id_origem_cliente": 106,
    "descricao": "98 - Funcionário Brayo"
},
{
    "id_origem_cliente": 54,
    "descricao": "99 - Cortesia"
}