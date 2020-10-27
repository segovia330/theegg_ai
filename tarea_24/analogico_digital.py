
valor_analogico_str = input()
valor_analogico = 0
valor_binario = []


def analogico_digital(analogico) :
    binario = []

    # ir diviendo entre dos el valor analogico y ver si tiene resto o no. Si tiene resto en binario tenemos un 1. Si no un 0. Y así vamos concatenando esos 1s y 0s.
    while analogico > 0 :
        if analogico % 2 == 0 :
            binario.insert(0, 0)
        else :
            binario.insert(0, 1)
        analogico = int(analogico / 2)
    return binario


# chequear que es un número positivo
try:
    valor_analogico = int(valor_analogico_str)
except ValueError:
    sys.exit('No es numerico')

if valor_analogico < 0 :
    sys.exit('No es un número positivo')

valor_binario = analogico_digital(valor_analogico)

print(''.join(map(str, valor_binario)))




