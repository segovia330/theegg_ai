
import csv, operator


csv_path = input()
tara_camion = int(input())
num_vacas = int(input())


lista = []
lista_camion = []
lista_camion_opt = []
lista_vacas_a_meter = []
peso_ocupado = 0
peso_libre = tara_camion - peso_ocupado
peso_libre_a_meter = 0
media_rendimiento_cargadas = 0.0
media_rendimiento_camion = 0.0
ind_ultima_metida = 0
ind_penultima_metida = 0
ind_ultima_quitada = 0
litros_metidos = 0
litros_metidos_opt = 0


def actualizar_ult_penult_añadidas() :
    # si no encuentra -1
    # la ultima será la metida de mas a la derecha. Y la penultima la anterior de mas a la derecha    
    j = len(lista_camion) - 1
    ind_u_m = -1
    ind_pu_m = -1
    while j>=0 :
        if lista_camion[j] == 1 and ind_u_m >= 0 :
            # print('act ----------------', lista_camion, j, lista_camion[j] )
            ind_pu_m = j
            break

        if lista_camion[j] == 1 and ind_u_m < 0 :
            ind_u_m = j
        
        j = j - 1    

    return ind_pu_m, ind_u_m



def meter_vaca (ind):
    global lista_vacas_a_meter
    global lista_camion
    global ind_penultima_metida
    global ind_ultima_metida
    global litros_metidos
    global media_rendimiento_camion
    global media_rendimiento_cargadas
    global peso_ocupado
    global peso_libre

    lista_vacas_a_meter[ind] = 0
    lista_camion[ind] = 1
    litros_metidos = litros_metidos + lista_rend[ind][2]
    media_rendimiento_camion = (media_rendimiento_cargadas * peso_ocupado + lista_rend[ind][2]) / tara_camion
    media_rendimiento_cargadas = (media_rendimiento_cargadas * peso_ocupado + lista_rend[ind][2]) / (peso_ocupado + lista_rend[ind][1])   # calcular media sin recorrer todos otra vez actualizando con el ultimo añadido
    peso_ocupado = peso_ocupado + lista_rend[ind][1]
    peso_libre = tara_camion - peso_ocupado
    ind_penultima_metida, ind_ultima_metida = actualizar_ult_penult_añadidas()


def quitar_vaca (ind) :
    global lista_camion
    global media_rendimiento_cargadas
    # global ind_penultima_metida
    # global ind_ultima_metida
    global litros_metidos
    global media_rendimiento_camion
    global peso_ocupado
    global peso_libre
    global ind_ultima_quitada

    lista_camion[ind] = 0
    litros_metidos = litros_metidos - lista_rend[ind][2]
    media_rendimiento_camion = (media_rendimiento_cargadas * peso_ocupado - lista_rend[ind][2]) / tara_camion

    if (peso_ocupado - lista_rend[ind][1] == 0) :
        media_rendimiento_cargadas = 0
    else :
        media_rendimiento_cargadas = (media_rendimiento_cargadas * peso_ocupado - lista_rend[ind][2]) / (peso_ocupado - lista_rend[ind][1])   # calcular media sin recorrer todos otra vez actualizando con el ultimo añadido

    peso_ocupado = peso_ocupado - lista_rend[ind][1]
    peso_libre = tara_camion - peso_ocupado
    ind_ultima_quitada = ind

    # ind_penultima_metida, ind_ultima_metida = actualizar_ult_penult_añadidas()


def printar_sol_opt() :
    k = 0
    str_print = ''
    while (k < len(lista_camion_opt)) :
        if lista_camion_opt[k] == 1 :
            str_print = str_print + str(lista_rend[k][0]) + ' '
        k = k + 1

    print('SOL OPT: Litros ', litros_metidos_opt)    # lista_camion_opt
    print('Vacas ')
    print(str_print)



with open(csv_path) as csvarchivo:
    entrada = csv.reader(csvarchivo)
    cabecera = next(entrada)
    i = 0

    # recorremos csv y lo metemos en una lista
    for reg in entrada:
        # print(reg)  # Cada línea se muestra como una lista de campos
        id_vaca, peso, produccion = reg
        # Se calcula rendimiento L/Kg por vaca
        rendimiento = int(produccion) / int(peso)
        # print(id_vaca, peso, produccion)
        lista.append([int(id_vaca), int(peso), int(produccion), rendimiento])
        lista_camion.append(0)
        lista_vacas_a_meter.append(0)
        # print(lista[i])    
        a, b, c, d = lista[i]
        # print(a, b, c, d)
        i = i + 1

    # ordenamos lista por rendimiento de mayor a menor
    lista_rend = sorted(lista, key=operator.itemgetter(3), reverse=True)
    #print(lista_rend)


    # empezamos a meter vacas al camion hasta que no entren mas empezando por la primera de la lista
    i = 0
    for vaca_lr in lista_rend:
        if vaca_lr[1] <= peso_libre :
            # metemos vaca i
            meter_vaca(i)

        i = i + 1

    lista_camion_opt = lista_camion[:]
    litros_metidos_opt = litros_metidos
    # print(lista_camion, lista_camion_opt, media_rendimiento_cargadas, media_rendimiento_camion, ind_ultima_metida, litros_metidos)

    if peso_libre == 0 : 
        printar_sol_opt()
        exit()

    # Estado 0 para adelante en la rama, se quita la ultima para meter mas.  Estado 1 se ha quitado dos hacia atras, ahora hay que intentar meter sin quitar, empezamos una nueva rama.
    estado = 0   

    # aquí ya partimos de x vacas metidas
    debug_cycles = 0

    # en el bucle vamos recorriendo todas las combinaciones de vacas. Quitando la ultima añadida y añadiendo más de las siguientes en la lista.
    # y cuando no se mejora más por esa rama. Se corta, y se echa hacia atrás quitando las dos vacas últimas añadidas. Y volviendo a intentar añadir más de las siguientes en la lista.
    while (peso_libre > 0) :  #    and debug_cycles < 100 

        # 1ero calculamos z(s), las vacas siguientes a sustituir la ultima metida con la idea de mejorar el rendimiento. Se van guardando los inds de las vacas a meter
        if estado == 0 : 
            i = ind_ultima_metida + 1
            peso_libre_a_meter = peso_libre + lista_rend[ind_ultima_metida][1]  # sumarle el de la vaca que quitariamos
        elif estado == 1 :
            i = ind_ultima_quitada + 1
            peso_libre_a_meter = peso_libre
        
        Lz = 0
        Pz = 0
        z = 0
        while (z < num_vacas) :
            lista_vacas_a_meter[z] = 0
            z = z + 1
        while (i < num_vacas) :
            if (lista_rend[i][1] <= peso_libre_a_meter) :
                lista_vacas_a_meter[i] = 1
                peso_libre_a_meter = peso_libre_a_meter - lista_rend[i][1]
                Lz = Lz + lista_rend[i][2]
                Pz = Pz + lista_rend[i][1]
            i = i + 1
        
        # print(lista_vacas_a_meter, 'Peso libre', peso_libre, 'Pz', Pz)

        #if Pz != 0 :
        #    print('IF ', peso_libre, lista_rend[ind_ultima_metida][2], lista_rend[ind_ultima_metida][1], Lz, Pz, lista_rend[ind_ultima_metida][2] / (lista_rend[ind_ultima_metida][1] + peso_libre), Lz / Pz)
        #    print('IF2', peso_libre, litros_metidos_opt / tara_camion, ((media_rendimiento_cargadas * peso_ocupado - lista_rend[ind_ultima_metida][2]) + Lz / Pz * (lista_rend[ind_ultima_metida][1] + peso_libre)) / tara_camion)

        # antes de quitar ninguna vaca, calcular si (Ly + 0) / (Py + x) < Lz / Pz. Donde 'y' es la ultima vaca metida, posible vaca a quitar. Y 'z' es las siguiente(s) vacas a meter para sustituir a 'y'
        # 'z' serán tantas vacas como quepan al quitar 'y'. Y no tienen porque ser seguidas, serán las primeras en la lista que entren.
        # tambien se mira si la rama por la que vamos tiene posibilidad de mejorar la solucion optima hasta el momento
        if (Pz > 0 and lista_rend[ind_ultima_metida][2] / (lista_rend[ind_ultima_metida][1] + peso_libre) < Lz / Pz
            and litros_metidos_opt / tara_camion < ((media_rendimiento_cargadas * peso_ocupado - lista_rend[ind_ultima_metida][2]) + Lz / Pz * (lista_rend[ind_ultima_metida][1] + peso_libre)) / tara_camion) :

            # estado 0. Vamos hacia adelante en la rama.
            if estado == 0 :
                # quitar vaca
                quitar_vaca(ind_ultima_metida)

                # print(lista_camion, 'Q', media_rendimiento_cargadas, media_rendimiento_camion, ind_ultima_metida, litros_metidos, peso_libre, peso_ocupado)

            # meter vacas nuevas. Recorrer lista_vacas_a_meter desde ind_ultima_metida. Y actualizar ind_ultima_metida también
            if (estado == 0) :
                i = ind_ultima_metida + 1
            elif (estado == 1) :
                i = ind_ultima_quitada + 1

            while (i < num_vacas) :
                if (lista_vacas_a_meter[i] == 1):
                    # metemos vaca i
                    meter_vaca(i)

                i = i + 1

            ind_penultima_metida, ind_ultima_metida = actualizar_ult_penult_añadidas()
            estado = 0
            
            # print(lista_camion, 'A', media_rendimiento_cargadas, media_rendimiento_camion, ind_ultima_metida, litros_metidos, peso_libre, peso_ocupado)
            
            # si es solucion optima temporal se actualiza
            if (litros_metidos > litros_metidos_opt) :
                lista_camion_opt = lista_camion[:]
                litros_metidos_opt = litros_metidos

            # no hay hueco. Es optima. No se puede mejorar más
            if peso_libre == 0 : 
                printar_sol_opt()
                exit()

        else :
            # hay que hechar hacia atras. No solo quitar la ultima, porque con esto no vale para mejorar porque el if no sé cumple. Hay que quitar la anterior a la ultima
            # si no se puede quitar más vacas hacia atrás hemos llegado al final
            # quitar vaca última metida
            ind_penultima_metida, ind_ultima_metida = actualizar_ult_penult_añadidas()
            # print(ind_penultima_metida, ind_ultima_metida)

            if (ind_ultima_metida >= 0) : 

                # Si venimos de añadir (estado 0), quitamos 2 vacas. Si venimos de quitar (estado 1) quitamos una.
                if (estado == 0 and ind_penultima_metida >= 0) :
                    quitar_vaca(ind_ultima_metida)
                    quitar_vaca(ind_penultima_metida)
                elif (estado == 1) :
                    quitar_vaca(ind_ultima_metida)

                ind_penultima_metida, ind_ultima_metida = actualizar_ult_penult_añadidas()

                # print(lista_camion, 'Q2', media_rendimiento_cargadas, media_rendimiento_camion, ind_penultima_metida, ind_ultima_metida, litros_metidos, peso_libre, peso_ocupado)
                estado = 1

            # Si no se puede echar 2 para atras terminamos. No hay más caminos por recorrer
            else :
                printar_sol_opt()
                exit()

        # debug_cycles = debug_cycles + 1
