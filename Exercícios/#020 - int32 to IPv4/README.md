# Descrição
Pegue o seguinte endereço IPv4: 128.32.10.1

Este endereço tem 4 octetos onde cada octeto é um único byte (ou 8 bits).

O 1º octeto 128 tem a representação binária: 10000000
O 2º octeto 32 tem a representação binária: 00100000
O 3º octeto 10 tem a representação binária: 00001010
O 4º octeto 1 tem a representação binária: 00000001
Então 128.32.10.1 == 10000000.00100000.00001010.00000001

Como o endereço IP acima tem 32 bits, podemos representá-lo como o número de 32 bits sem sinal: 2149583361

Complete a função que pega um número de 32 bits sem sinal e retorna uma representação de string de seu endereço IPv4.

Exemplos

2149583361 ==> "128.32.10.1"

32 ==> "0.0.0.32"

0 ==> "0.0.0.0"

(Link do desafio)[https://www.codewars.com/kata/52e88b39ffb6ac53a400022e/train/python]