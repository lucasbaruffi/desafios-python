# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

from itertools import product

ADJ = {
    '0': ['0', '8'],
    '1': ['1', '2', '4'],
    '2': ['2', '1', '3', '5'],
    '3': ['3', '2', '6'],
    '4': ['4', '1', '5', '7'],
    '5': ['5', '2', '4', '6', '8'],
    '6': ['6', '3', '5', '9'],
    '7': ['7', '4', '8'],
    '8': ['8', '5', '7', '9', '0'],
    '9': ['9', '6', '8']
}

def get_pins(observed):
    """Return list of all possible PIN variations for the observed PIN."""
    # For each digit get the list of possible replacements, then take cartesian product
    options = [ADJ[d] for d in observed]
    return [''.join(p) for p in product(*options)]

# Obviamente peguei do GPT, estava criando algo muito mais complexo, mas de fato definir os adjacentes é o melhor.