# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# 
# Additionally, if the number is negative, return 0.
# 
# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    list = []
    sum = 0
    for n in range(1,number): # Verifica cada número abaixo
        if n not in list: # Se não estiver na lista
            if n % 3 == 0: # Se for múltiplo de 3
                sum += n
                list.append(n)
            elif n % 5 == 0: # Se for múltiplo de 5
                sum += n
                list.append(n)
            else:
                pass
        else:
            pass
    return sum