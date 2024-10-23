# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
# 
# H = hours, padded to 2 digits, range: 00 - 99
# M = minutes, padded to 2 digits, range: 00 - 59
# S = seconds, padded to 2 digits, range: 00 - 59
# he maximum time never exceeds 359999 (99:59:59)

def make_readable(seconds):
    horas = 00
    segundos = seconds % 60
    minutos = seconds // 60
    if minutos > 59:
        horas = minutos // 60
        minutos = minutos % 60        
    return f"{str(horas).zfill(2)}:{str(minutos).zfill(2)}:{str(segundos).zfill(2)}"



print(make_readable(359999))