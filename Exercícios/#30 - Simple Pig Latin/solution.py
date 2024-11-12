# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python


def replace_str_index(text,index=0,replacement=''):
    return f'{text[:index]}{replacement}{text[index+1:]}'


def pig_it(text):
    textList = text.split()
    newList = []
    for palavra in textList:

        if palavra.isalnum():

            primeiraLetra = palavra[0]
            palavra = replace_str_index(palavra)
            palavra = palavra + primeiraLetra

            palavra = palavra + "ay"

        newList.append(palavra)

    newList = " ".join(newList)
    return newList


print(pig_it('Panem et circenses'))