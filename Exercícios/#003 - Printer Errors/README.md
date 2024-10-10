# Descrição
Numa fábrica, uma impressora imprime etiquetas para caixas. Para um tipo de caixa a impressora tem de utilizar cores que, por uma questão de simplicidade, são nomeadas com letras de a a m.

As cores utilizadas pela impressora são registadas numa sequência de controlo. Por exemplo, uma string de controlo "boa" seria aaabbbbhaijjjm, o que significa que a impressora utilizou três vezes a cor a, quatro vezes a cor b, uma vez a cor h e uma vez a cor a...

Por vezes, há problemas: falta de cores, avaria técnica e é produzida uma cadeia de controlo "má", por exemplo. aaaxbbbbyyhwawiwjjjwwm com letras que não vão de a a m.

Tem de escrever uma função impressora_error que dada uma string irá devolver a taxa de erro da impressora como uma string representando um racional cujo numerador é o número de erros e o denominador o comprimento da string de controlo. Não reduza esta fração a uma expressão mais simples.

A string tem um comprimento maior ou igual a um e contém apenas letras até z.