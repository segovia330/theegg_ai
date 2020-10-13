import math
import sys


fraccion_str = input()

try:
    fraccion = float(fraccion_str)
except ValueError:
    sys.exit('No es numerico')

if fraccion > 0.9999 or fraccion < 0.0001:
    sys.exit('No es entre 0 y 0.9999')

# multiplicamos por 10000 para quitar la parte decimal y así logramos el numerador y el denominador
# nota al convertir a int con int() redondea para abajo
denominador = 10000
numerador = round(fraccion * 10000)

#print(numerador)
#print(denominador)

# ahora reducimos la fraccion
# vamos intentando dividir numerador por los numeros primos que sea divisible, hasta la mitad de su valor. 
# Y a su vez dividimos el denominador por los mismos valores que el numerador es divisible 
numerador_2 = numerador
i = 2
while i <= numerador_2:
    # chequeamos si i es primo o no
    for j in range(2,i):
        if(i % j==0):
            i = i + 1
            break
    else:
        # i es primo. Dividimos numerador y denominador por i
        #print ('i ', i)
        if (numerador % i == 0 and denominador % i == 0):
            numerador = numerador / i
            denominador = denominador / i
        # no es primo. Buscamos siguiente primo
        else:
            i = i + 1
            

print(int(numerador), '/', int(denominador))

