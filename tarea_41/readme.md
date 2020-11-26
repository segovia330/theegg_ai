
# Tarea_41 Regex

Para esta tarea proponemos el siguiente ejercicio: el @egger mediante técnicas de Regex debe  
calcular el número de caracteres, el número palabras y ranking de palabras por frecuencia de uso  
del siguiente texto. La aplicación debe servir para cualquier otro texto:  

"En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como  
referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento?  
Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas  
olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por  
hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo,  
ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.  
Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta  
increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando  
quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no  
porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me  
solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso  
yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.  
El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios  
congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando  
semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.  
Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar  
hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que  
se encarga de pensar, y hasta cantamos juntos la canción de Annie.  
Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de  
Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así."  
Ref: https://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/  


# Solución

Para calcular en número de letras, se utiliza la siguiente expresión regular: '[^ ]'  
De esta manera cogemos todos los caracteres menos los espacios. Después contamos el número de coincidencias encontradas.  

Para calcular el número de palabras, se utiliza la siguiente expresión regular: '[^¡!.¿?«»,:\n ]+'  
De está manera coge un conjunto de caracteres que no tengo ninguno de los definidos en la expresión. Cualquier caracter de esos determina el inicio o final de la palabra.  

Para calcular el número de apariciones de cada palabra, se genera la siguiente expresión regular: r'\b' + palabra + r'\b'  
De esa manera busca todas las apariciones de cada palabra, que aparezca en el texto de forma completa.  

Posteriormente se mete cada palabra y su número de apariciones en una lista, y se ordena por número de apariciones.  



# Ejecución

El programa se ha hecho usando python 3.8  
  
Para ejecutarlo, se requiere tener python instalado. Abrir una consola, ir a la carpeta donde está el archivo .py  
Y ejecutar >regex.py  
Pasarle como input el path completo del fichero que contiene el texto a analizar. En este caso el nombre del archivo es 'texto.txt'.  

