
frases = []
frases_invertidas = []

numero_de_frases = int(input())


# meter frases en un array de strings
for i in range(numero_de_frases):
    frases.append(input())

# print(frases)


# recorrer el array
ind_frase = 0
for frase in frases:
    frases_invertidas.append('')

    # recorrer cada string e ir cogiendo palabras separadas por espacio
    frase = frase.strip() + ' '
    ind_esp = frase.find(' ')
    while ind_esp > 0:
        frases_invertidas[ind_frase] = frase[:ind_esp] + ' ' + frases_invertidas[ind_frase]
        frase = frase[ind_esp + 1:]
        ind_esp = frase.find(' ')
        # print(frase, ind_esp)

    print('Case #', ind_frase+1, frases_invertidas[ind_frase])
    ind_frase = ind_frase + 1


