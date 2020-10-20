
# Tarea_22 Algoritmo del lechero

Usted es un original empresario de Azkoitia, y tiene la brillante idea de abrir una tienda de la leche en la Plaza del pueblo. Como es una persona muy prudente, desea que la leche que venderá sea perfectamente natural y fresca, y por esa razón, va a traer unas sanísimas vacas de desde Tolosa.  
Dispone de un camión con un cierto límite de peso, y un grupo de vacas disponibles para la venta. Cada vaca puede tener un peso distinto, y producir una cantidad diferente de leche al día.  
Debes elegir qué vacas comprar y llevar en su camión, de modo que pueda maximizar la producción de leche, observando el límite de peso del camión.  

1.- Para este propósito tienes que definir las siguientes entradas:  
Entrada: Número total de vacas en la zona de Tolosa que están a la venta.  
Entrada: Peso total que el camión puede llevar.  
Entrada: Lista de pesos de las vacas.  
Entrada: Lista de la producción de leche por vaca, en litros por día.  
2.- El algoritmo que programes tiene que calcular la siguiente salida:  
Salida: Cantidad máxima de producción de leche se puede obtener.  
Fuente: http://www.nachocabanes.com/retos/reto.php?n=07  


# Solución

El problema se ha resuelto aplicando backtracking, y cortando las ramas en las condiciones que se explican a continuación.  
Primero se ordena la lista de vacas por rendimiento L/Kg, de mayor a menor. Con la idea de ir recorriendo la lista e ir primero colocando las vacas de mayor rendimiento.  
Cuando se ha llegado al punto en el que no caben más vacas en el camión, si el hueco que dejan es 0, hemos terminado, tenemos la solución optima.  
Si no, seguiremos por esa rama, para ello intentamos quitar la última vaca añadida para sustituirla por una o más vacas de menor rendimiento, con la idea de que aunque tengan menor rendimiento puedan dejar menos hueco en el camión y mejoren la suma de litros. Para saber si merece seguir por esa rama o no se mira la siguiente condición:  
- que las vacas a añadir tengan mejor rendimiento L/Kg que la vaca a quitar teniendo en cuenta el hueco. O sea que suponiendo en el mejor de los casos, que las vacas a añadir rellenaran el hueco completo, si con su rendimiento no mejoran la media, no merece seguir por esa rama.  
- y además que las vacas a añadir también en el mejor de los casos de rellenar el hueco pudieran mejorar la media de rendimiento del camión completo, de la solución optima provisional lograda hasta ahora.  

En el caso de no seguir por la rama, se echa para atrás, a parte de la vaca que ibamos a quitar para seguir para adelante, quitando otra vaca más, la última y penultima añadidas.  
Así se sigue ciclicamente hasta o bien recorrer todo el árbol o bien haber encontrado por el camino una solución que llena el 100% del camión.  



![Diagrama de Flujo](algoritmo_lechero.png) 


# Ejecución

El programa se ha hecho usando python 3.8  
  
Para ejecutarlo, se requiere tener python instalado. Abrir una consola, ir a la carpeta donde está el archivo .py  
Y ejecutar >algoritm_lechero.py  

Se debe introducir un path a un fichero CSV con la lista de vacas, en la que por cada vaca tenga la siguiente info: id de vaca, peso y litros por día. Ver ejemplos en carpeta /config.  
Peso que soporta el camión.  
Número de vacas.  
Se devuelve por pantalla la solución optima, con la lista de vacas metidas en el camión para oobtener el máximo número de litros. Y el número de litros logrado.  
