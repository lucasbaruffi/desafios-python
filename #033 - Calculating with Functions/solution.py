# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

def calculator(expression):
    if expression[1] == "*": return int(expression[0]) * int(expression[2])       
    elif expression[1] == "/": return int(int(expression[0]) / int(expression[2]))        
    elif expression[1] == "+": return int(expression[0]) + int(expression[2])
    elif expression[1] == "-": return int(expression[0]) - int(expression[2])
        
def zero(p=False): return 0 if not p else calculator(f"0{p}")
def one(p=False): return 1 if not p else calculator(f"1{p}")
def two(p=False): return 2 if not p else calculator(f"2{p}")
def three(p=False): return 3 if not p else calculator(f"3{p}")
def four(p=False): return 4 if not p else calculator(f"4{p}")
def five(p=False): return 5 if not p else calculator(f"5{p}")
def six(p=False): return 6 if not p else calculator(f"6{p}")
def seven(p=False): return 7 if not p else calculator(f"7{p}")
def eight(p=False): return 8 if not p else calculator(f"8{p}")
def nine(p=False): return 9 if not p else calculator(f"9{p}")

def times(p): return f"*{p}"    
def plus(p): return f"+{p}"    
def minus(p): return f"-{p}"
def divided_by(p): return f"/{p}"
    

print(five(divided_by(six())))

