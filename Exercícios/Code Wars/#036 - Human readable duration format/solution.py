# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

# years
# days
# hours
# minutes 
# seconds



def format_duration(seconds):

    horaFinal = []
    horaFormatada = ""
    # Se for menor que um minuto

    if seconds == 0:
        return "now"
    
    else:
        while True:
            
            if seconds < 60:
                if seconds == 1:
                    horaParcial = (f"{seconds} second")
                else:
                    horaParcial = (f"{seconds} seconds")
                
                if seconds > 0:
                    horaFinal.append(horaParcial)
                break

            # Se for menor que uma hora
            elif seconds < 3600:
                if seconds <= 119:
                    horaParcial = (f"{int(seconds/60)} minute")
                else:
                    horaParcial = (f"{int(seconds/60)} minutes") 
                horaFinal.append(horaParcial)
                seconds -= ((int(seconds/60))*60)


            # Se for menor que um dia
            elif seconds < 86400:
                if seconds <= 7199:
                    horaParcial = (f"{int(seconds/3600)} hour")
                else:
                    horaParcial = (f"{int(seconds/3600)} hours") 
                horaFinal.append(horaParcial)
                seconds -= ((int(seconds/3600))*3600)


            # Se for menor que um ano
            elif seconds < 31536000:
                if seconds <= 172799:
                    horaParcial = (f"{int(seconds/86400)} day")
                else:
                    horaParcial = (f"{int(seconds/86400)} days") 
                horaFinal.append(horaParcial)
                seconds -= ((int(seconds/86400))*86400)

            # Se for menor que um ano
            elif seconds >= 31536000:
                if seconds <= 63071999:
                    horaParcial = (f"{int(seconds/31536000)} year")
                else:
                    horaParcial = (f"{int(seconds/31536000)} years") 
                horaFinal.append(horaParcial)
                seconds -= ((int(seconds/31536000))*31536000)

        for cont, item in enumerate(horaFinal):

            if cont == 0:
                horaFormatada += f"{item}"
            
            elif cont + 1 == len(horaFinal):
                horaFormatada += f" and {item}"

            elif cont > 0:
                horaFormatada += f", {item}"

    return horaFormatada
    



print(format_duration(5687532))