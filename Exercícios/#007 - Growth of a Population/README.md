# Descrição
Complete a solução de modo a que esta divida a string em pares de dois caracteres. Se a string contiver um número ímpar de caracteres, deverá Numa pequena cidade a população é p0 = 1.000 no início do ano. A população aumenta regularmente 2% ao ano e, além disso, passam a viver na cidade 50 novos habitantes por ano. Quantos anos necessita a cidade para ter uma população maior ou igual a p = 1200 habitantes?

No final do primeiro ano haverá:
1000 + 1000 * 0,02 + 50 => 1070 habitantes

No final do 2º ano haverá:
1070 + 1070 * 0,02 + 50 => 1141 habitantes (** número de habitantes é um número inteiro **)

No final do 3º ano haverá:
1141 + 1141 * 0,02 + 50 => 1213

Serão necessários 3 anos completos.
Parâmetros dados de forma mais geral:

p0, percentagem, ago (habitantes que entram ou saem em cada ano), p (população a igualar ou a superar)

a função nb_year deve devolver n número de anos inteiros necessários para obter uma população maior ou igual a p.

aug é um número inteiro, percent um número flutuante positivo ou nulo, p0 e p são números inteiros positivos (> 0)

Exemplos:
nb_ano(1500, 5, 100, 5000) -> 15
nb_ano(1500000, 2,5, 10000, 2000000) -> 10
Nota:
Não se esqueça de converter o parâmetro percentual em percentagem no corpo da sua função: se o parâmetro percentual for 2 deverá convertê-lo para 0,02.

Não existem frações de pessoas. No final de cada ano, a contagem da população é um número inteiro: 252,8 pessoas, arredondado para 252 pessoas.