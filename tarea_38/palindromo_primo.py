
n = int(input())

# función que dice si un número es primo o no.
def es_primo(num):
    for i in range(2, int(num/2) + 1):
        if(num % i==0):
            return False
    return True


# función que dice si un número es palindromo o no.
def es_palindromo(num):
    num_str = str(num)
    len_str = len(num_str)

    # se recorre media cadena
    for i in range(int(len_str/2)):
        if (num_str[i] != num_str[len_str-1-i]):
            return False    
    return True


# Se recorre de n a 2000000, porque n es max 1000000, y entre 1000000 y 2000000 ya hay palindromos primos.
for i in range(n, 2000000):
    # primero se mira si es palindromo que es mucho más rápido que mirar si es primo.
    if (es_palindromo(i) and es_primo(i)):
        print(i)
        break

