


def secuencia_comun_mas_larga(secuencia1, secuencia2):
    substr = ''
    if len(secuencia1) > 0 and len(secuencia2) > 0:
        # recorremos todos los substrings posibles en secuencia1
        for i in range(len(secuencia1)):
            for j in range(len(secuencia1)-i+1):
                # si el substring de secuencia1 supera al actual substring común y el substring de secuencia1 está en secuencia2, tenemos un substring mayor.
                if j > len(substr) and (secuencia1[i:i+j] in secuencia2) :
                    substr = secuencia1[i:i+j]

    return substr


cadena1 = input()
cadena2 = input()

res = secuencia_comun_mas_larga(cadena1, cadena2)
print('Secuencia común más larga: ', res)
