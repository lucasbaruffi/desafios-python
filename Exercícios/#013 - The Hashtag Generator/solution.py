# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
# 
# Here's the deal:
# 
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false


def generate_hashtag(s):
    # Verifica se não está vazia
    if s:
        # Divide a frase em palavras
        s = s.split()
        frase = "#"
        for palavra in s:
            palavra = palavra.capitalize()
            frase = frase + palavra
        if len(frase) <= 140:
            return frase
        else:
            return False           
    else:
        return False


print(generate_hashtag(" Hello there thanks for trying my Kata"))