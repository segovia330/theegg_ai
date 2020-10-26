import random

# treboles diamantes corazones picas
cartas_orig = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
               14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
               27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
               40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
               'A', 'B']

cartas_inicio_barajadas = []
cartas_en_juego = []
clave = []

mensaje = ''
mensaje_encriptado_str = ''

mensaje_desencriptado_str = ''

def barajar (cartas) :
    global cartas_en_juego
    global cartas_inicio_barajadas
    cartas_inicio_barajadas = cartas[:]
    random.shuffle(cartas_inicio_barajadas)
    cartas_en_juego = cartas_inicio_barajadas[:]
    print('Posicion cartas inicio ', cartas_en_juego)

def buscar_joker_A (cartas) :
    return cartas.index('A')

def buscar_joker_B (cartas) :
    return cartas.index('B')


def generar_numero () :
    global cartas_en_juego

    # paso 1. Encuentra el comodín A. Intercámbialo con la carta que tiene debajo. Si el comodín está al final de la baraja, ponlo debajo de la primera carta.
    ind_jok = buscar_joker_A(cartas_en_juego)
    jok = cartas_en_juego.pop(ind_jok)
    cartas_en_juego.insert((ind_jok+1) % 54, jok)

    # paso 2. Encuentra el comodín B. Muévelo bajo la carta que está debajo de la que tiene debajo. Si el comodín está al final de la baraja, muévelo debajo de la segunda carta. Si el comodín es la penúltima carta, muévelo debajo de la primera carta.
    ind_jok = buscar_joker_B(cartas_en_juego)
    jok = cartas_en_juego.pop(ind_jok)
    cartas_en_juego.insert((ind_jok+2) % 54, jok)

    #print(cartas_en_juego)

    # paso 3. Corta la baraja en tres, intercambiando las cartas antes del primer comodín con las cartas que están detrás del segundo comodín.
    ind_1 = min(buscar_joker_A(cartas_en_juego), buscar_joker_B(cartas_en_juego))
    ind_2 = max(buscar_joker_A(cartas_en_juego), buscar_joker_B(cartas_en_juego))
    cartas_corte_3 = cartas_en_juego[ind_2+1:] + cartas_en_juego[ind_1:ind_2+1] + cartas_en_juego[:ind_1]
    cartas_en_juego = cartas_corte_3[:]

    #print(cartas_en_juego)

    # paso 4. Mira la última carta. Conviértela a un número de 1 a 53 (usa el orden normal: tréboles, diamantes, corazones y picas. NOTA: ya tenemos en la lista las cartas convertidas a números de 1 a 53.
    #         Si la carta es un trébol, toma su número tal cual. Si es de diamantes, suma 13 a su valor. Si es de corazones, súmale 26. Si es de picas, súmale 39. Ambos comodines suman 53). 
    #         Cuenta el valor valor obtenido empezando en la carta superior (normamente yo cuento de 1 a 13 una y otra vez, si es preciso; es más fácil que contar hasta un número alto de forma secuencial). 
    #         Corta tras esa carta, dejando la última carta de la baraja a final
    ind_corte_2 = cartas_en_juego[53]
    if type(ind_corte_2) == str :
        ind_corte_2 = 53
    cartas_corte_2 = cartas_en_juego[ind_corte_2:] + cartas_en_juego[:ind_corte_2] 
    cartas_en_juego = cartas_corte_2[:]

    #print(cartas_en_juego)

    # paso 5. Mira la primera carta. Conviértela en un número de 1 a 53, de la misma manera que en el paso 4. Cuenta esas cartas (la primera carta es la uno). 
    #         Escribe la carta tras la que hayas terminado en un papel; no la quites de la baraja. Si la carta es un comodín, no la apuntes, y vuelve al paso 1.
    ind_5 = cartas_en_juego[0]
    if type(ind_5) == str :
        ind_5 = 53
    if type(cartas_en_juego[ind_5-1]) == str :   # si es joker 'A' o 'B'
        return generar_numero()
    else :
        # paso 6. Convierte la carta del paso anterior en un número. Del As de tréboles al Rey de tréboles se cuentan del 1 a 13. Del As de diamantes al Rey de diamantes se cuentan como 14-26. Del As de corazones al Rey de corazones se cuentan como 1 a 13. Por último, del As de picas al Rey de picas se cuentan como 14 a 26. Necesitamos ir de 1 a 26, no de 1 a 52, para poder convertir a letras.
        # print(cartas_en_juego[ind_5-1] % 26)
        return cartas_en_juego[ind_5-1] % 26


# generamos clave, númerica. No la convertimos a char, porque despues al encriptar y desencriptar habría que volverla a convertir a números
def generar_clave(num_chars) :
    clave_gen = []
    while num_chars > 0 :
        clave_gen.append(generar_numero())
        num_chars = num_chars - 1

    print('Clave ', clave_gen)
    return(clave_gen)


# funcion que coge un mensaje y aplicando el solitario lo encripta
def encriptar_mensaje (mensaje) :
    global cartas_en_juego
    mensaje_encriptado = []
    mensaje_encriptado_str = ''

    # quitamos espacios
    mensaje = mensaje.replace(" ", "")

    # inicializamos cartas
    cartas_en_juego = cartas_inicio_barajadas[:]

    # generamos clave
    clave = generar_clave(len(mensaje))
    # print(clave)

    # Convertimos el mensaje original de letras a números, A=1, B=2, etc.
    # Y le sumamos los números de mensaje original con los correspondientes de la ristra Solitario, módulo 26.
    ind = 0
    for caracter in mensaje :
        mensaje_encriptado.append((ord(caracter) - 64 + clave[ind] - 1) % 26 + 1)
        ind = ind + 1

    print('Mensaje encriptado numerico', mensaje_encriptado)

    # convertimos el mensaje numerico en texto. Y le añadimos espacios cada 5
    ind = 0
    for caracter in mensaje_encriptado :
        if (ind != 0 and ind % 5 == 0) :
            mensaje_encriptado_str = mensaje_encriptado_str + ' '

        mensaje_encriptado_str = mensaje_encriptado_str + chr(mensaje_encriptado[ind] + 64)
        ind = ind + 1

    return mensaje_encriptado_str


# funcion que coge un mensaje encriptado y aplicando el solitario lo desencripta
def desencriptar_mensaje (mensaje) : 
    global cartas_en_juego
    mensaje_desencriptado = []
    mensaje_desencriptado_str = ''

    # quitamos espacios
    mensaje = mensaje.replace(" ", "")

    # inicializamos cartas
    cartas_en_juego = cartas_inicio_barajadas[:]

    # generamos clave
    clave = generar_clave(len(mensaje))
    # print(clave)

    # Convertimos el mensaje cifrado de letras a números, A=1, B=2, etc.
    # Y le restamos a cada número del texto cifrado el número correspondiente de la ristra, módulo 26: for ejempo, 22-1=21, 1-22=5. 
    # Es fácil. Si el primer número es menor o igual que el segundo, sumamos 26 al primer número antes de restar.
    ind = 0
    for caracter in mensaje :
        mensaje_desencriptado.append((ord(caracter) - 64 - clave[ind] - 1) % 26 + 1)
        ind = ind + 1

    print('Mensaje desencriptado numerico ', mensaje_desencriptado)

    # convertimos el mensaje numerico en texto. Y le añadimos espacios cada 5
    ind = 0
    for caracter in mensaje_desencriptado :
        if (ind != 0 and ind % 5 == 0) :
            mensaje_desencriptado_str = mensaje_desencriptado_str + ' '

        mensaje_desencriptado_str = mensaje_desencriptado_str + chr(mensaje_desencriptado[ind] + 64)
        ind = ind + 1

    return mensaje_desencriptado_str



mensaje = input()
barajar (cartas_orig)


mensaje_encriptado_str = encriptar_mensaje(mensaje)
print('Mensaje encriptado', mensaje_encriptado_str)

mensaje_desencriptado_str = desencriptar_mensaje(mensaje_encriptado_str)
print('Mensaje desencriptado', mensaje_desencriptado_str)
