# Take the following IPv4 address: 128.32.10.1
# 
# This address has 4 octets where each octet is a single byte (or 8 bits).
# 
# 1st octet 128 has the binary representation: 10000000
# 2nd octet 32 has the binary representation: 00100000
# 3rd octet 10 has the binary representation: 00001010
# 4th octet 1 has the binary representation: 00000001
# So 128.32.10.1 == 10000000.00100000.00001010.00000001
# 
# Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361
# 
# Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.
# 
# Examples
# 2149583361 ==> "128.32.10.1"
# 32         ==> "0.0.0.32"
# 0          ==> "0.0.0.0"

def int32_to_ip(int32):
    binario = bin(int32)
    print(binario)
#    binario = str(binario).zfill(32)
#    print(binario)
#    print(divideint32(binario))

# Função para dividir um número de 32 dígitos em 4 de 8
def divideint32(int32):
    n1 = int32[0],int32[1],int32[2],int32[3],int32[4],int32[5],int32[6],int32[7]
    n2 = int32[8],int32[9],int32[10],int32[11],int32[12],int32[13],int32[14],int32[15]
    n3 = int32[16],int32[17],int32[18],int32[19],int32[20],int32[21],int32[22],int32[23]
    n4 = int32[24],int32[25],int32[26],int32[27],int32[28],int32[29],int32[30],int32[31]

    n1 = "".join(n1)
    n2 = "".join(n2)
    n3 = "".join(n3)
    n4 = "".join(n4)

    return n1, n2, n3, n4
#int32_to_ip(2154959208)


def binario(num):
    valorBinario = ""
    while num >1:
        zeroOuUm = num % 2
        valorBinario = str(zeroOuUm) + valorBinario
        num = num // 2
    print(valorBinario)
binario(2)