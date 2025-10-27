# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python

def max_sequence(arr):
    if not arr: return 0
    else:
        negativos = 0
        positivos = 0

        for numero in arr:
            if numero >= 1:
                positivos += 1
            elif numero <= 1:
                negativos +=1

        if positivos == 0:
            return 0

        else:
            v = 0
            somas = []
            tam = len(arr)


            for cont, numero in enumerate(arr):
                v = 0
                for c in range(cont, tam):
                    print(arr[c])
                    v += arr[c]
                somas.append(v)
                print(somas)
            return somas
            pass


print(max_sequence([-2, 1, -3, 4]))

