# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
# 
# Examples:
# 
# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"

# 1 - Criar uma função para inverter palavras

def inverte_Palavra(palavra):
    return palavra[::-1]

def spin_words(sentence):
    novaFrase = []
    for palavra in sentence.split(" "):
        if len(palavra) >= 5:
            palavra = inverte_Palavra(palavra)
        novaFrase.append(palavra)
    novaFrase = " ".join(novaFrase)
    print(novaFrase)

spin_words("This is another test")

# Para o CW:

# def spin_words(sentence):
#     novaFrase = []
#     for palavra in sentence.split(" "):
#         if len(palavra) >= 5:
#             palavra = palavra[::-1]
#         novaFrase.append(palavra)
#     novaFrase = " ".join(novaFrase)
#     return(novaFrase)