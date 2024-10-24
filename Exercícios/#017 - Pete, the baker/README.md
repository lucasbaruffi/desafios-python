# Descrição
O Pete gosta de fazer bolos. Tem algumas receitas e ingredientes. Infelizmente não é bom a matemática. Pode ajudá-lo a descobrir quantos bolos poderia fazer considerando as suas receitas?

Escreva uma função cakes(), que recebe a receita (objeto) e os ingredientes disponíveis (também um objeto) e devolve o número máximo de bolos que o Pete consegue cozer (inteiro). Para simplificar, não existem unidades para as quantidades (por exemplo, 1 quilo de farinha ou 200 g de açúcar são simplesmente 1 ou 200). Os ingredientes que não estão presentes nos objetos podem ser considerados 0.

Exemplos:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})

# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})


(Link do desafio)[https://www.codewars.com/kata/525c65e51bf619685c000059/train/python]