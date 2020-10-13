# Diccionario TheEgg

# turing
Alan Turing. matematico informatico teorico, criptografo filosfo,...
Padre de la informatica
Maquina de Turing: 
    un dispositivo hipotético que representa una máquina de computación
    es un dispositivo que manipula símbolos sobre una tira de cinta de acuerdo con una tabla de reglas
    una cinta infinita, llena de simbolos. Los simbolos marcan el comportamiento de la máquina. La maquina lee un simbolo y puede modificarlo. Tambien puede mover la cinta para atrás y para adelante
https://es.wikipedia.org/wiki/Alan_Turing

# programación 
diseño y codificación. Que genera un sw, que posteriormente se ejecuta sobre una maquina hw     
hacer que una maquina haga lo que quieres
https://www.youtube.com/watch?v=5QapF7kt1xQ
     

# inteligencia-artificial 
agente flexible que percibe su entorno y lleva a cabo acciones que maximicen sus posibilidades de éxito en algún objetivo o tarea
la capacidad de un sistema para interpretar correctamente datos externos, para aprender de dichos datos y emplear esos conocimientos para lograr tareas y metas concretas a través de la adaptación flexible
capaz de evolucionar, aprender, modificarse a si mismo, percibir entorno, cumplir ciertas tareas (en un principio limitadas? tal vez si va evolucionando, se amplíen?)
tal vez replicarse, haciendo agentes parecidos, modificados
se habla de hacer tareas de forma similar a un humano
https://es.wikipedia.org/wiki/Inteligencia_artificial


# transistor
componente electronico que deja o no pasar corriente, dependiendo de la tension base que se le mete. Y en base a eso 1 o 0. bit.
flip flop  guardan ese 1 o 0. Cada señal de reloj devuelven lo guardado
diodo. silicio con carga N (9 lectrones) y P (7 electrones) el los dos lados. Que dejan pasar corriente. depende de la polaridad. Porque en el caso que no deja es porque se separan por polaridad y al separarse no deja pasar corriente. https://www.youtube.com/watch?v=GwrUC23M5xc
transistor bipolar NPN. P en medio finito. voltaje de N a P menor. QUe voltaje entre extremos
https://www.nutsvolts.com/magazine/article/may2015_Secura       output 5V o 0V


# ley-de-moore
cada 2 años se duplica el número de transistores
2020 rondamos los 10.000 millones de transistores

# puertas-lógicas
and
or
not
nand
nor
XOR   0 0 -> 0   0 1 -> 1  1 0 -> 1   1  1 -> 0
suma  de dos bits  AND y XOR

# periférico
dispositivo que se conecta a placa base, que es la interfaz con el usuario. raton teclado, pantalla, impresora,...

# arquitectura-von-neumann
arquitectura de computadoras. Unidad de procesamiento, ALU unidad aritmetico logica, registros del procesador, unidad de control, que tiene registro de instrucciones, contador de programa, memoria para almacenar datos e intrucciones, y memoria masiva, y E/S
          

# arquitectura-harvard
más moderna que von neumann, que también es un sistema de programa almacenado, pero tiene un conjunto dedicado de direcciones y buses de datos para leer datos desde memoria y escribir datos en la misma, y otro conjunto de direcciones y buses de datos para ir a buscar instrucciones.
    con pistas de almacenamiento y de señal físicamente separadas para las instrucciones y para los datos
    usaban cintas perforadas para guardar las instrucciones

# sistema-operativo
conjunto de programas y librerias que permite manejar los recursos hardware del PC


# software
la parte logica de un sistema informatico
el sw envia intrucciones al hw
     

# hardware
la parte fisica de un sistema informatico
componentes electronicos. PCU, RAM, perifericos, HDD,...
     

# raspberry pi
pequeño ordenador. bajo coste. Tiene CPU y RAM, y al que se le puede conectar pantallas. Usb, ethernet,...
sirve como smart tv, ordenador, base domotica, core para AI, robotica
     
     
# arduino 
placa con un microcontrolador. IOs. E/S digitales y E analogicas
proyecto de codigo abierto
muy usado en impresoras 3d, cuadcopters,
https://www.youtube.com/watch?v=UoBUXOOdLXY&feature=youtu.be
     

# compilador
convierte lenguaje de alto nivel en código máquina
chequea errores
     

# intérprete
programa que convierte lenguaje de alto nivel a lenguaje máquina
pero a diferencia del compilador que éste lo hace del programa completo y guarda el resultado
el interprete va traduciendo sobre la marcha según ejecuta las instrucciones


# lenguaje-de-programación
conjunto de simbolos o codigos para generar instrucciones que luego ejecute un procesador
     

# editor-de-código
editor de texto más o menos avanzado que ayuda con la sintaxis de distintos lenguajes de progarmación
     

# lenguaje-de-alto-nivel
lenguajes más legibles, más parecido al lenguaje humano
en los que se suele programar normalmente
comunes: c c++ c# java perl python, javascript objective c, visual basic
de bajo nivel: ensamblador
sus instrucciones más cercanas a instrucciones del hw


# lenguaje de-máquina 
es el lenguaje que entiende el procesador
se consigue compilando o interpretando lenguaje de alto nivel
lenguaje de bajo nivel 
conjunto de instrucciones particular para cada procesador
de una instruccion de lenguaje de alto nivel se convierte a varias de ensamblador
y de una de ensamblador a varias de bajo nivel
     

# python
lenguaje de programación interpretado y es multiplataforma
multiparadigma (ver paradigma en Lisp), interpretado y imperativo. En poca medida programación funcional
código muy legible
Python tiene bibliotecas como Numpy, Scipy y Pybrain, que se utilizan para la computación científica, computación avanzada, y el aprendizaje automático
https://unipython.com/como-se-relaciona-la-inteligencia-artificial-ia-con-python/#:~:text=La%20Inteligencia%20Artificial%20trabaja%20mejor%20con%20Python%20porque%3A&text=%2DCuenta%20con%20una%20cantidad%20de,r%C3%A1pidas%20que%20al%20utilizar%20Java.


# R
tiene muchos paquetes de programacion
se usa mucho para machine learning RODBC
tiene algoritmos de aprendizaje automático
bueno para analizar datos y tratarlos
     

# Lisp
trabaja con expresiones simbolicas y protoripado (orientada a objetos, pero no usa instancias usa clonacion, que serviran como prototipos)
se utiliza para imitar razonamientos humanos.
es un lenguaje multiparadigma
paradigma
    Los programas se pueden clasificar por el paradigma del lenguaje que se use para producirlos. Los principales paradigmas son: imperativos, declarativos y orientación a objetos
        declarativos. 2 categorias
            funcionales
            logicos
    https://es.wikipedia.org/wiki/Lenguaje_de_programaci%C3%B3n#Paradigmas
     

# Java
lenguaje orientado a objetos
tiene todas las herramientas para trabajar en IA
transparencia, mantenibilidad, portabilidad. Escalabilidad
     
     
# lenguaje-de-bajo-nivel
lenguaje más cercano al lenguaje máquina.
como ensamblador
c es más bajo nivel que java o python
     

# lenguaje-compilado
lenguaje al que se le pasa el compilador para que genere lenguaje máquina, para poder ejecutarlo

# lenguaje-interpretado 
lenguaje que no se compila, se interpreta por el interprete, que analiza y ejecuta el código directamente sobre la marcha.
     

# repositorio-de-control-de-versiones
sitio para subir código fuente, versión tras version
controla los cambios que ha habido, permite hacer comparaciones y merges
permite echar atrás cambios
permite trabajar en equipo, trabajando simultaneamente en mismo módulo
     

# git
web git vcs
en un sistema de control de versiones
de los más potentes y más utilizados
working staging area   y repo
    el staging area sirve para decirle lo que quieres comitear. Porque igual no quieres comitear todo lo que has modificado para separar cambios en varios commits. Prodria hacerse incluso con varios cambios del mismo fichero, hacer un add y seguir haciendo cambios.
permite ramas
    se suele usar rama master y paralela rama dev
        la master no se toca. Y se trabaja sobre la dev todos, y luego se hace merge. Y cuando todo está probado OK, se mergea hacia master
git bash
git comandos
    git init
    git status
    git add <file> o .    (el punto agrega todos)     add la primera vez. Pero tambien si cambias el file hay que volver a hacer add y commit
    git config --global user.email "email"   y   user.name "name"
    git commit -m "mensaje"
    git log
    git checkout <file>
    git diff <file>
    git branch nombre_rama     la crea
    git checkout nombre_rama      cambiamos de master a la rama
    git branch        muestra las ramas

    git remote add <link de github>
    git push -u origin master
    git clone <link git hub>      te haces copia del repo a local
       
archivo .gitignore    lista de archivos o carpetas a ignorar
fork   es distinto a una rama. Se crea otro proyecto partiendo de uno
herramientas graficas: gitkraken   github desktop
integrado en IDEs, VS Code o Atom  IntelliJ Idea


# github          
herramienta relacionada a Git para subir nuestro codigo a repositorio remoto
permite compartir trabajo con un equipo de desarrolladores
es de microsoft. no open source. Y más usado para hacer codigo open source
GitHub hace el dev ops con Azure Devops


# gitLab
open source. Aunque se usa más en empresas privadas, para hacer codigo cerrado
integra todo el proceso de desarrollo   dev ops
    integrando auto test unitarios test integracion y delivery automatico. Continious deployment
se puede instalar en un servidor propio
           

# javascript
lenguaje de programacion interpretado 
orientado a objetos, basado en prototipos, imperativo
se usar tanto en el lado del cliente (paginas web), como en el lado del servidor
nodejs para ejecutar javascript sin navegador. Sin html. Puedes ejecurtar js desde consola
         

# php
lenguaje sobre todo usado en desarrollo web con acceso a BBDD
invisible al navegador
es libre
hypertext preprocessor
el codigo php suele interpretarse en un servidor web 
          

# Java
es un lenguaje de programacion y plataforma informatica
las app java se compilan bytecode. Java byte code. instrucciones máquina simplificadas específicas de la plataforma Java
Y luego se ejecutan en una maquina virtual java
    independiente de plataforma
licencia GNU
     

# html
Hypertext marckup language
marcas adicionales al texto, que manejan el aspecto de la pagina y estructura del texto
se usa para paginas web
funciona a base de referencias externas, imagen video scripts,...
html5
    etiquetas para graficos 2D y 3D
    datos, datagrids,...
    mathML     
    grag & drop
    web semantica
    geolocalizacion


# CSS
hojas de estilo en cascada
es un lenguaje de diseño grafico
se utiliza para crear la presentación de paginas HTML
    tambien se puede aplicar a ficheros XML, XUL, RSS, SVG
separa entre contenido del documento y presentacion. Capas colores fuentes,...
permite que distintas paginas web compartan estilo con mismo fichero CSS
     

# R
entorno y lenguaje de programación orientado a analisis estadistico
usado en aprendizaje automático, mineria de datos, matematicas financieras, ...
orientado a objetos
capacidad grafica
     

# SQL
structured query language
utilizado para administrar y recuperar información de BBDD relacionales
incluye, insercion, consulta, borrado, y creación de datos. Así como esquemas, y control de acceso a los datos
         

# Algoritmo
una secuencia de instrucciones para ejecutar cualquier cosa. Lo que sea
tiene un estado inicial, coge un input como entrada, y siguiendo una secuencia de pasos, se genera un output
permite llevar a cabo una tarea o buscar solución a un determinado problema
         

# Diagrama-de-flujo 
representación gráfica de un algoritmo
elementos: linea de fliujo, terminal, proceso, decisión, entrada/salida


# convertidor-analógico-digital
AD y DA
señal analogica puede ser voltage o corriente
sistema analogico, toma valores continuos. Sistema digital toma valores discretos
manejando señales digitales se puede aplicar algoritmos sofisticados por sw
1. muestreo. 2 cuantificar. 3 codificar en binario

     
# transistores-bipolares
     ver transistores


# frecuencia-de-muestreo
cuantas muestras se toman por segundo en un sistema digital
     

# sistema-binario
sistema numerico que utiliza nada más 0 y 1
     

# algebrabooleana 
matematicas binarias
reglas: A+0=A     A+1=1     A*0=0     A*1=A     A+A=A     A+NA=1     A*A=A     A*NA=0     NNA=A
        A+AB=A    A+NA*B=A+B     (A+B)*(A+C)=A+B*C

