# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
# 
# Examples:
# 
# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"

# 1 - Criar uma função para inverter palavras

def inverte_Palavra(palavra):
    novaPalavra = ""
    for letra in palavra:
        novaPalavra = letra + novaPalavra
    return novaPalavra

def spin_words(sentence):
    # Your code goes here
    return None

print(inverte_Palavra("Palavra"))