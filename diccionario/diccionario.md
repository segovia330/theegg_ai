# Diccionario TheEgg

# turing
Alan Turing. matematico informatico teorico, criptografo filosfo,...  
Padre de la informatica.  
Maquina de Turing:  
- Un dispositivo hipotético que representa una máquina de computación.  
- Es un dispositivo que manipula símbolos sobre una tira de cinta de acuerdo con una tabla de reglas.  
- Una cinta infinita, llena de simbolos. Los simbolos marcan el comportamiento de la máquina. La maquina lee un simbolo y puede modificarlo. Tambien puede mover la cinta para atrás y para adelante.  
https://es.wikipedia.org/wiki/Alan_Turing


# programación 
Diseño y codificación. Que genera un sw, que posteriormente se ejecuta sobre una maquina hw.  
Hacer que una maquina haga lo que quieres.  
https://www.youtube.com/watch?v=5QapF7kt1xQ
     

# inteligencia-artificial 
Agente flexible que percibe su entorno y lleva a cabo acciones que maximicen sus posibilidades de éxito en algún objetivo o tarea.  
La capacidad de un sistema para interpretar correctamente datos externos, para aprender de dichos datos y emplear esos conocimientos para lograr tareas y metas concretas a través de la adaptación flexible.  
Capaz de evolucionar, aprender, modificarse a si mismo, percibir entorno, cumplir ciertas tareas (en un principio limitadas? tal vez si va evolucionando, se amplíen?)  
Tal vez replicarse, haciendo agentes parecidos, modificados.  
Se habla de hacer tareas de forma similar a un humano.  
https://es.wikipedia.org/wiki/Inteligencia_artificial


# transistor
Componente electronico que deja o no pasar corriente, dependiendo de la tension base que se le mete. Y en base a eso 1 o 0. bit.  
Flip flop  guardan ese 1 o 0. Cada señal de reloj devuelven lo guardado.  
Diodo. silicio con carga N (9 lectrones) y P (7 electrones) el los dos lados. Que dejan pasar corriente. depende de la polaridad. Porque en el caso que no deja es porque se separan por polaridad y al separarse no deja pasar corriente. https://www.youtube.com/watch?v=GwrUC23M5xc  
Transistor bipolar NPN. P en medio finito. voltaje de N a P menor. QUe voltaje entre extremos.  
https://www.nutsvolts.com/magazine/article/may2015_Secura       output 5V o 0V  


# ley-de-moore
Cada 2 años se duplica el número de transistores.  
2020 rondamos los 10.000 millones de transistores.  


# puertas-lógicas
and  
or  
not  
nand  
nor  
XOR   0 0 -> 0   0 1 -> 1  1 0 -> 1   1  1 -> 0  
suma  de dos bits  AND y XOR  


# periférico
Dispositivo que se conecta a placa base, que es la interfaz con el usuario. raton teclado, pantalla, impresora,...  

# arquitectura-von-neumann
Arquitectura de computadoras. Unidad de procesamiento, ALU unidad aritmetico logica, registros del procesador, unidad de control, que tiene registro de instrucciones, contador de programa, memoria para almacenar datos e intrucciones, y memoria masiva, y E/S.  
          

# arquitectura-harvard
Más moderna que von neumann, que también es un sistema de programa almacenado, pero tiene un conjunto dedicado de direcciones y buses de datos para leer datos desde memoria y escribir datos en la misma, y otro conjunto de direcciones y buses de datos para ir a buscar instrucciones.  
Con pistas de almacenamiento y de señal físicamente separadas para las instrucciones y para los datos.  
Usaban cintas perforadas para guardar las instrucciones.  

# sistema-operativo
Conjunto de programas y librerias que permite manejar los recursos hardware del PC.  


# software
La parte logica de un sistema informatico.  
El sw envia intrucciones al hw.  
     

# hardware
La parte fisica de un sistema informatico.  
Componentes electronicos. PCU, RAM, perifericos, HDD,...  
     

# raspberry pi
Pequeño ordenador. bajo coste. Tiene CPU y RAM, y al que se le puede conectar pantallas. Usb, ethernet,...  
Sirve como smart tv, ordenador, base domotica, core para AI, robotica.  
     
     
# arduino 
Placa con un microcontrolador. IOs. E/S digitales y E analogicas.  
Proyecto de codigo abierto.  
Muy usado en impresoras 3d, cuadcopters.  
https://www.youtube.com/watch?v=UoBUXOOdLXY&feature=youtu.be  
     

# compilador
Convierte lenguaje de alto nivel en código máquina.  
Chequea errores.  
     

# intérprete
Programa que convierte lenguaje de alto nivel a lenguaje máquina.  
Pero a diferencia del compilador que éste lo hace del programa completo y guarda el resultado.  
El interprete va traduciendo sobre la marcha según ejecuta las instrucciones.  


# lenguaje-de-programación
Conjunto de simbolos o codigos para generar instrucciones que luego ejecute un procesador.  
     

# editor-de-código
Editor de texto más o menos avanzado que ayuda con la sintaxis de distintos lenguajes de progarmación.  
     

# lenguaje-de-alto-nivel
Lenguajes más legibles, más parecido al lenguaje humano.  
En los que se suele programar normalmente.  
Comunes: c c++ c# java perl python, javascript objective c, visual basic.  
De bajo nivel: ensamblador.  
Sus instrucciones más cercanas a instrucciones del hw.  


# lenguaje de-máquina 
Es el lenguaje que entiende el procesador.  
Se consigue compilando o interpretando lenguaje de alto nivel.  
Lenguaje de bajo nivel.  
Conjunto de instrucciones particular para cada procesador.  
De una instruccion de lenguaje de alto nivel se convierte a varias de ensamblador.  
Y de una de ensamblador a varias de bajo nivel.  
     

# python
Lenguaje de programación interpretado y es multiplataforma.  
Multiparadigma (ver paradigma en Lisp), interpretado y imperativo. En poca medida programación funcional.  
Código muy legible.  
Python tiene bibliotecas como Numpy, Scipy y Pybrain, que se utilizan para la computación científica, computación avanzada, y el aprendizaje automático.  
https://unipython.com/como-se-relaciona-la-inteligencia-artificial-ia-con-python/#:~:text=La%20Inteligencia%20Artificial%20trabaja%20mejor%20con%20Python%20porque%3A&text=%2DCuenta%20con%20una%20cantidad%20de,r%C3%A1pidas%20que%20al%20utilizar%20Java.  


# R
Tiene muchos paquetes de programacion.  
Se usa mucho para machine learning RODBC.  
Tiene algoritmos de aprendizaje automático.  
Bueno para analizar datos y tratarlos.  
     

# Lisp
Trabaja con expresiones simbolicas y protoripado (orientada a objetos, pero no usa instancias usa clonacion, que serviran como prototipos).  
Se utiliza para imitar razonamientos humanos.  
Es un lenguaje multiparadigma.  
Paradigma.  
- Los programas se pueden clasificar por el paradigma del lenguaje que se use para producirlos. Los principales paradigmas son: imperativos, declarativos y orientación a objetos.  
  - Declarativos. 2 categorias.  
    - funcionales.  
    - logicos.  
- https://es.wikipedia.org/wiki/Lenguaje_de_programaci%C3%B3n#Paradigmas
     

# Java
Lenguaje orientado a objetos.  
Tiene todas las herramientas para trabajar en IA.  
Transparencia, mantenibilidad, portabilidad. Escalabilidad.  
     
     
# lenguaje-de-bajo-nivel
Lenguaje más cercano al lenguaje máquina.  
Como ensamblador.  
c es más bajo nivel que java o python.  
     

# lenguaje-compilado
Lenguaje al que se le pasa el compilador para que genere lenguaje máquina, para poder ejecutarlo.  

# lenguaje-interpretado 
Lenguaje que no se compila, se interpreta por el interprete, que analiza y ejecuta el código directamente sobre la marcha.  
     

# repositorio-de-control-de-versiones
Sitio para subir código fuente, versión tras version.  
Controla los cambios que ha habido, permite hacer comparaciones y merges.  
Permite echar atrás cambios.  
Permite trabajar en equipo, trabajando simultaneamente en mismo módulo.  
     

# git
web git vcs.  
En un sistema de control de versiones.  
De los más potentes y más utilizados.  
Working staging area y repo.  
- El staging area sirve para decirle lo que quieres comitear. Porque igual no quieres comitear todo lo que has modificado para separar cambios en varios commits. Prodria hacerse incluso con varios cambios del mismo fichero, hacer un add y seguir haciendo cambios.  
Permite ramas.  
- Se suele usar rama master y paralela rama dev.  
  - La master no se toca. Y se trabaja sobre la dev todos, y luego se hace merge. Y cuando todo está probado OK, se mergea hacia master.  
  
git bash.  
git comandos.  
- git init       
- git status        muestra estado de las modificaciones y fichero pendientes para subir.  
- git add <file> o .    (el punto agrega todos)     add la primera vez. Pero tambien si cambias el file hay que volver a hacer add y commit.  
- git config --global user.email "email"   y   user.name "name".  
- git commit -m "mensaje"     guarda cambios al repositorio.  
- git log  
- git checkout <file>  
- git diff <file>  
- git branch nombre_rama     la crea.  
- git checkout nombre_rama      cambiamos de master a la rama.  
- git branch        muestra las ramas.  

- git remote add <link de github>  
- git push -u origin master     sube al repo remoto.  
- git clone <link git hub>      te haces copia del repo a local.  
       
Archivo .gitignore    lista de archivos o carpetas a ignorar.  
ork   es distinto a una rama. Se crea otro proyecto partiendo de uno.  
Herramientas graficas: gitkraken   github desktop.  
Integrado en IDEs, VS Code o Atom  IntelliJ Idea.  


# github          
Herramienta relacionada a Git para subir nuestro codigo a repositorio remoto.  
Permite compartir trabajo con un equipo de desarrolladores.  
Es de microsoft. no open source. Y más usado para hacer codigo open source.  
GitHub hace el dev ops con Azure Devops.  


# gitLab
Open source. Aunque se usa más en empresas privadas, para hacer codigo cerrado.  
Integra todo el proceso de desarrollo   dev ops.  
- integrando auto test unitarios test integracion y delivery automatico. Continious deployment.  
Se puede instalar en un servidor propio.  
           

# javascript
Lenguaje de programacion interpretado.  
Orientado a objetos, basado en prototipos, imperativo.  
Se usar tanto en el lado del cliente (paginas web), como en el lado del servidor.  
nodejs para ejecutar javascript sin navegador. Sin html. Puedes ejecurtar js desde consola.  
         

# php
Lenguaje sobre todo usado en desarrollo web con acceso a BBDD.  
Invisible al navegador.  
Es libre.  
hypertext preprocessor.  
El codigo php suele interpretarse en un servidor web.  
          

# Java
Es un lenguaje de programacion y plataforma informatica.  
Las app java se compilan bytecode. Java byte code. instrucciones máquina simplificadas específicas de la plataforma Java.  
Y luego se ejecutan en una maquina virtual java.  
    independiente de plataforma.  
Licencia GNU.  
     

# html
Hypertext marckup language.  
Marcas adicionales al texto, que manejan el aspecto de la pagina y estructura del texto.  
Se usa para paginas web.  
Funciona a base de referencias externas, imagen video scripts,...  
html5.  
- etiquetas para graficos 2D y 3D.  
- datos, datagrids,...  
- mathML  
- grag & drop  
- web semantica  
- geolocalizacion  


# CSS
Hojas de estilo en cascada.  
Es un lenguaje de diseño grafico.  
Se utiliza para crear la presentación de paginas HTML.  
- Tambien se puede aplicar a ficheros XML, XUL, RSS, SVG.  
Separa entre contenido del documento y presentacion. Capas colores fuentes,...  
Permite que distintas paginas web compartan estilo con mismo fichero CSS.  
     

# R
Entorno y lenguaje de programación orientado a analisis estadistico.  
Usado en aprendizaje automático, mineria de datos, matematicas financieras, ...  
Orientado a objetos.  
Capacidad grafica.  
     

# SQL
Structured query language.  
Utilizado para administrar y recuperar información de BBDD relacionales.  
Incluye, insercion, consulta, borrado, y creación de datos. Así como esquemas, y control de acceso a los datos.  
         

# Algoritmo
Una secuencia de instrucciones para ejecutar cualquier cosa. Lo que sea.  
Tiene un estado inicial, coge un input como entrada, y siguiendo una secuencia de pasos, se genera un output.  
Permite llevar a cabo una tarea o buscar solución a un determinado problema.  
         

# Diagrama-de-flujo 
Representación gráfica de un algoritmo.  
Elementos: linea de fliujo, terminal, proceso, decisión, entrada/salida.  


# convertidor-analógico-digital
AD y DA.  
Señal analogica puede ser voltage o corriente.  
Sistema analogico, toma valores continuos. Sistema digital toma valores discretos.  
Manejando señales digitales se puede aplicar algoritmos sofisticados por sw.  
Pasos de la conversión:
1. muestreo. 
2. cuantificar. 
3. codificar en binario

     
# transistores-bipolares
ver transistores


# frecuencia-de-muestreo
Cuantas muestras se toman por segundo en un sistema digital.  
     

# sistema-binario
Sistema numerico que utiliza nada más 0 y 1.  
     

# algebrabooleana 
Matematicas binarias.  
Reglas:  
- A+0=A     A+1=1     A*0=0     A*1=A     A+A=A     A+NA=1     A*A=A     A*NA=0     NNA=A  
- A+AB=A    A+NA*B=A+B     (A+B)*(A+C)=A+B*C  


# arquitectura-cliente-servidor
Modelo en el que las comunicaciones se dividen en dos procesos que cooperan entre sí, intercambiando información de esta forma se separa la lógica de visualización y presentación de datos en cliente, con la lógica de negocio que corre en el servidor. Más que nada por seguridad y por eficiencia.  
Cliente: el que inicia la petición.  
Servidor: el que responde a esa petición.  
Al cliente también se le llama ForntEnd. La parte del lado del navegador web.  
Al servidor se le llama back end. La parte que corre en servidor físico.  
- Aqui pueden correr varios servidores sw. http, https, ftp, dns, de correo,...  
Entre las tecnologias que se utilizan para el desarrollo de frontend y back end, más BBDD, más servidor http puerto 80, se le llama stack.  
- LAMP: Linux Apache MySQL PHP  
- MEAN: MondoDB Express Angular NodeJS  
		

# FTP
Protocolo de transferencia de archivos, que corre entre equipos conectados a red TCP.  
Está basado en modelo cliente servidor.  
	

# servidor-web
Programa que procesa una aplicacion del lado del servidor, realizando conexiones con el cliente.  
Las conexiones pueden ser unidireccionales bidireccionales, sincronas, asincronas.  
Generando una respuesto en cualquier lenguaje del lado del cliente.  
	

# IP
Dirección de un equipo. Númerico.  
Indentifica a un dispositivo conectado a una red.  
Normalmente usada IP4. 32 bits.  
Puede ser fija o dinámica, por DHCP.  

# DNS
Domain name system.  
Sistema para dar nombres a equipos conectados a una red IP.  
Se utiliza una BBDD distribuida jerarquica.  
El uso más comun traducción de nombres a IPs.  

# protocolo-TCP/IP
Conjunto de protocolos.  
TCP: protocolo de control de tranmisión.
IP: protocolo de control de internet
Protocolos que engloba: ARP, FTP, HTTP, SMTP, Telnet, DHCP, DNS, SNMP,...  


# ETL
Extract, transform, load.  
Es el proceso de preparación de los datos antes de ser utilizados.  
- Extracción: Total. Extrae los datos de una tacada. Incremental. Va extrayendo poco a poco, por lotes.  
- Transformación: aquí influye la lógica de negocio. Se hacen en el staging area.  
  - Las directrices de transformación deben ser:  
    - Declarativas.  
    - Independientes.  
    - Claras.  
    - Inteligibles.   
    - Con finalidad util para el negocio.  
  - Varias transformaciones típicas.  
    - Filtrar filas por ciertas características.  
    - Eliminar duplicados.  
    - Transformar datos. Nombres a indices por ejemplo.  
    - Calcular datos nuevos.  
    - Agrupar datos de multiples fuentes.  
    - Unir o combinar datos de distintas fuentes.  
    - Pivotar las tablas.  
    - Dividir columnas.  

- Carga  
  - Se pasan los datos transformados a BBDD analitica.  
  - Importante que motor usar de BBDD. Eficiente en insertar datos.  
  - Dos formas  
    - Acumulación simple: se hace un resumen y se carga sólo el resultado.  
    - Rolling: se resume información a varios niveles de granularidad.  


# bases-de-datos
Conjunto de datos que pertenecen al mismo contexto.  
Almacenados y gestinados por un motor de BBDD.  
Modelos relacionales y no relacionales.  
- Realcionales: MySQL Oracle
- No relacionales: Documentales: MongoDB



# data-preprocessing
Paso importante en data mining y machine learning.  
A veces ocurre que hay datos fuera de rango, combinaciones imposibles absurdas, valores faltantes.  
Es importante la calidad de los datos. Frase tipica, entra basura, sale basura.  
Tareas:
- Data cleaning: corregir datos erroneos, irrelevantes o imprecisos.  
- Data editing: revisión y ajuste de los datos. Puede ser manual o auto.  
- Data reduction: trasformacion de info numerica o alfabetica en una forma ordenada y simplificada.  
- Data wrangling: conversión de dotos en crudo a otro formato más apropiado.  


# bucles-en-programación
Es una secuencia de instrucciones que se ejecuta ciclicamente, mientras se cumpla cierta condición.  
Los más tipicos: while y for  


# API
Application programming interface.  
Permite comunicar distintos componentes sw.  
Conjunto de funciones y metodos que ofrece una parte para ser utilizada en una aplicación.  
Es una capa de abstracción.  
Permite utilizar cosas hechas de terceros.  
Tipos  
- Locales  
- Remotas  
  - Web Service  
    - SOAP  
    - REST  
      - Get Post Put Delete
      - 


# JSON
Jasva Script Object notation.  
Formato usando en APIs.  
Es más moderno que XML. Más sencillo de parsear. Se usa en volumentes grandes de información.  
El más usando actualmente. 2020.  
Se considera un formato independiente del lenguaje.  


# XML
eXtensible Marckup Language.  
Usado también en APIs. Para intercambio de información estructurada entre distintas plataformas.  


# protocolo-de-comunicación
Sistema de reglas que permite que varias computadoras se comuniquen entre ellas, y transmitan información.  
Se define una sintaxis, semantica y sincronización.  
También se define modo de recuperar errores.  
Se definen los mensajes o tramas que se transmiten por la red.  
Suele haber distintos protocolos en base al nivel de capa de abstracción.  
- capa de aplicación.  
- de transporte.  
- de red.  
- de enlace de datos.  
- capa física.  


# bases-de-datos
Colección de datos relacionados.  
Almacenados y organizados de tal forma que los datos puedas ser consultados y actualizados.
Componentes:
- Campo: area de almacenamiento de un tipo concreto.  
- Registro: coleccion de datos relacionada entre sí.  
- Tabla: colección de registros.
Tipos de BBDD:  
- Relacionales: la información se encuentra en tablas relacionadas entre sí. Manejan la integridad de los datos.  
- No relacionales: se usan para grandes volumenes de información.  
- Distribuidas: Estan replicadas en distintas hubicaciones fisicas.  
- Orientadas a objetos: A parte de contener los datos del objeto en sí, contienen su comportamiento.  


# SQL
BBDD relacionales.  
Normalmente centralizadas.  
MySQL, Oracle, SQL Server.  
Con lenguaje SQL se pueden hacer las siguientes operaciones:  
- Consultas.  
- Insertar, acutalizar, borrar.  
- Crear BBDD  
- Crear procedimientos almacenados.  
- Crear tablas.  
- Crear vistas.  
- Gestionar permisos de acceso.  


# NoSQL
Not only SQL. Puede usar SQL de apoyo.  
Como prioridad la velocidad de acceso e insercion de datos. No la integridad de datos.  
Manejan cantidades enormes de información.  
Pueden ser distribuidas.  
Varias NoSQL: MongoDB, Casandra, CouchDB  
Lenguajes utilizados:  
- JSON: JavaScript Object Notation.  
- CQL: Contextual Query Language.  
- GQL: Graph Query Language.  



# dirección-IP
ver IP.  


# Internet
Conjunto descentralizado de redes conectadas entre sí. Basado en TCP/IP.  
El servicio más utlizado la web o www.  
Otros servicios: Correo, FTP, IRC, VoIP, SSH, Telnet,...  



# red-WAN
Wide area network.  
Redes de gran extension, que une varias redes locales u otro tipo de redes.  
La redes WAN son creadas por empresas privadas o proveedores de internet.  
Normalmente se utiliza la topologia de estrella.  


# red-LAN
Local area network.  
Red de peqwueña extensión. Abarca un area como de una casa, un edificio.  


# máscara-de-subred
Define lo que se encuentra dentro y fuera de la subred.  
A las máquinas que están dentro de la red, se puede acceder directamente, y a las que están fuera mediante un router.  


# router
Dispositivo inteligente, que la primera vez envia por todas las bocas, pero una vez que averigua el camino del equipo de destino, lo memoriza.  
Sirve como pasarela entre redes.  
Funcionan en la capa de red, manejando a nivel de IP.  



# switch
Dispositivo que conecta varios equipos, a nivel de capa de enlace de datos.  
Pasa datos de un segmento a otro, en base a direcciones MAC.  
Mejoran rendimiento comparando con hubs. Que transmiten por todas las bocas lo que entra por una.  


# TCP-IP
ver protocolo TCP-IP.  
Protocolos:
- TCP: 
  - Orientado a la conexión.  
  - Asegura la transmisión.  
- UDP:  
  - Servición no asegurado y sin conexión.  
- IP: Protocolo de internet. Basado en direcciones de 4 octetos.  
TCP/IP está basado en capas. Cada capa se comunica con la inferior y la superior.  
- Nivel de enlace o acceso a la red. Capa física.   
- Nivel de red o internet: proporciona paquetes de datos y maneja direcciones IP.  
- Nivel de transporte: maneja estado de la transmisión como datos de enrutamiento.  
- Nivel de aplicación: Telnet, FTP, SNMP,...  


# IP-pública
Es la dirección que identifica nuestra red en el exterior.  


# IP-privada
Es la dirección que identifica nuestro dispositivo en la nuestra interna.  


# algoritmo
ver arriba  
carácteristicas:
- Definido.  
- Preciso.  
- Finito.  
tipo:
- Grafico.  
- No grafico: pseudo código.  


# diagrama-de-flujo
Diagrama que describe un proceso, sistema o algoritmo.  
Se puede utilizar para explicar la lógica del programa, y demostrar como está organizado el código.  

Elementos:  
- Terminador: ![Terminador](flowchart-symbols-terminator.svg)  
- Proceso: ![process](flowchart-symbols-process.svg)  
- Documento: ![process](flowchart-symbols-document.svg)  
- Decisión: ![process](flowchart-symbols-decision.svg)  
- Datos de entrada/salida: ![process](flowchart-symbols-data.svg)  
- Datos almacenados: ![process](flowchart-symbols-database.svg)  
- Proceso predefinido: ![process](flowchart-symbols-predefined_process.svg)  



# convención-de-programación
Conjunto de reglas para nombrar identificadores, tipos, funciones, y entidades en general del código fuente.  
Permite reducir esfuerzo para leer y entender código fuente.  
Mejora la apariencia.  
Evita conflictos de nombres.  
Mejora consistencia dentro del equipo de desarrollo.  
Permite refactorización automática con menos errores.  
Cada lenguaje de programación tiene la suya.  


# redes-informáticas
IPv4  
- ClaseA: primero octeto red, 3 siguientes host. IP/8. Primer octeto 0..127.  
- ClaseB: primeros dos octetos red y siguientes dos host. IP/16. Primer octero 128..191  
- ClaseC: primeros tres octetos red y siguiente host. IP/24. Primer octero 192..223  
Mascara de red:  
- IP/8.   255.0.0.0  
- IP/16.  255.255.0.0  
- IP/24.  255.255.255.0  
Subred:  
- Se divide la parte host. Y se cogen varios bits de ahí, para separar entre subred y host.  
- La mascara de red se convierte en mascara de subred. Por ej para un clase A. 255.240.0.0 usando 4 bits para la subred.  
Dirección de red o subred: Es la de host 0.  La de broadcast la ultima.


# Pentesting
Testear a ver como se podría penetrar en un sistema.  
Imitaría lo que haría un atacante.  


# XSS
Cross-side scripting. Secuencia de comandos en sitios cruzados.  
En web apps.  
Es una tecnica en la que un tercero inyecta código JavaScript (sobre todo) en paginas web que visita un usuario.  
Sirve para robar info delicada, o secuestrar sesiones de usuario.  
Se puede evitar con encriptación.  
Dos tipos:  
- Directa: inserta código html, con etiquetas como script o iframe.  
- Indirecta: cuando se modifican valores de una app web para pasar valores entre dos paginas.  


# Inyección SQL
se trata de infiltrar codigo para hacer operaciones sobre una BBDD.  
un programa es vulnerable a esto si no valida las entradas.   
puede ocurrir cuando se piden parámetros al usuario para formar una SQL.  
mediante esta tecnica se pueden borrar, insertar y/o modificar lineas en la BBDD.  
en cada lenguaje de programación hay funciones para evitar estos ataques.  

# Ataque informático
operación que tiene como objetivo tomar en control, desestabilizar o dañar un sistem informático.  
puede ser desde algo pequeño un ordenador personal, hasta ataques a empresas o organizaciones importantes, con grandes daños economicos.  



# Ataque DDoS
DoS. Ataque de denegación de servicio.  
hace perder conectividad o por consumo del ancho de banda de la victima o sobrecarga de recursos informaticos.  
DDoS. Ataque de denegación de servicio distribuido. Distributed denial service.  
- generan gran flujo de trafico desde varios puntos a la vez a un sólo punto de destino.  


# Ingeniería social
se trata de manilpular a los usuarios para conseguir información sensible. Como permisos o acceso.  
se hacen pasar por un banco, por tecnicos, clientes, compañeros de trabajo.  


# hacker
el que descubre vulnerabilidades en un sistema informatico.  
no es un delincuente o pirata informatico.  
se habla de la ética hacker que tiene los siguientes valores: 
- pasión
- libertad
- conciencia social
- verdad
- anti-corrupción
- igualdad social
- libre acceso a la información
- valor social
- preocupación responsable
- curiosidad
- creatividad


# cracker
es el que rompe un sistema de seguridad.  
puede ser con animo de lucro, por protesta o por desafio.  
tipos de cracks:
- troyanos: se instala un programa en la computadora infectada y ofrece control remoto. pasa desapercibido.  
- analizadores de trafico de red.  
- fuerza bruta: es probar todas las combinaciones de contraseñas.  
- DDoS  
- phishing  
- suplantación. depsues de haber metido un troyano y sacar las claves por ejemplo. hacerse pasar por el otro, para seguir atacando a otros contactos.  


# Man-in-the-middle
el que se pone en medio de la transmisión con la capacidad de leer, modificar einsertar.  
se utiliza cuando hay un intercambio de claves sin cifrar.  
defensas a este tipo de ataque:
- clave publica.  
- autenticación mutua fuerte.  
- contraseñas.  
- uso de certificados.  


# Phishing
Se envia un mail suplantando una identidad, con la idea de obtener información confidencial.    
Spam phishing se manda a muchos los mismo.  
Spear phishing, se envia un mensaje particularizado al usuario.  
Hay app para robar token oauth. Que se saltan el paso de contraseña y todo tipo de identificaciones, como claves queneradas al momento, smm al movil,..  
  sappo  
  esto no es un phishin al uso, porque no se suplanta la pagina de tu banco, gmail, office360,...  
  el token oauth, sustituye al todo tipo de mecanismo de acceso, como usuario y contraseña,...  
  el que tenga este token puede acceder a tu correo o lo que sea durante meses.  
Con una IA se puede suplantar la voz e imagen (video conferencia).  


# expresiones-regulares
Son un potente lenguaje de descripción de texto.  
Permiten:
- buscar un substring al principio o al final.  
- o alguna parte que se repita x veces.  
- o algo que no aparezca. O sea un string que no contenga ciertas cosas.  
Con ello se puede extraer partes de un texto, o sustituirlas por otras.  


# procesamiento-del-lenguaje-natural
Abarca las ciencias de la computación, inteligencia artificial y la linguistica.  
Trata de desarrollar sistemas que faciliten la comunicación de personas y máquinas mediante el lenguaje natural.  
En los inicios esto se hacia mediante unas reglas fijas.  
Actualmente se usan tecnicas de aprendizaje automático.  
Dificultades: separación de la entrada en palabras. Gestionar ambiguedades. Recepción imperfecta de datos.  
Aplicaciones: sintesis de voz. Reconocimiento de voz. Traducción automática. Comprensión del lenguaje. Extración de información...   


# scrapping
WebScraping: Extraer información de una pagina web.  
- Para hacer web scrapping con Python. Beautifulsoup  
  - Permite extraer contenido de una web en formato HTML o XML.  
  - Permite buscar en los siguientes tipos de elementos: Tag, NavigableString, hijos, padres...
  - Y dentro de cada elemento: id, attrs, class,...
- O Framework Sracpy.  
  - 

# crawling
Descubrir enlaces de una web y navegar entre ellos.  
Crawlers o arañas web son programas que inspeccionan webs de forma metodica y automatizada.  
- se recorren todos los enlaces.
- posteriormente mediante scraping se descargan las paginas.  
- se recorren recursivamente por si hay modificaciones o nuevos enlaces.  


# Código-fuente
conjunto de líneas de texto, con instrucciones a ejecutar.  
Puede estar escrito en distintos lenguajes de programación. c, c++, perl, python, java, javascript,...  
- dependiendo del lenguaje será interpretado directamente o compilado.  


# AJAX
es una tecnología web.  
permite tener comunicación asincrona con el servidor.  
AJAX = Asynchronous Javascript and XML.  
Maneja las siguientes tecnologías:
- HTML  
- DOM  
- Javascript  
- XMLHTTPREQUEST  
- Formato de datos:  
  - JSON
  - XML
  - HTML
  - TXT






# HTML
HTML5  ver HTML arriba.  
En los inicios paginas web estaticas. Sin apenas backend. Sin BBDD. Para actualizar contenido había que hacer muchos cambios en el FrontEnd.  
Posterior, webs dinámicas.  
- Backend  
- BBDD  
- Con PHP al principio.  
- Empieza la comunicación bidireccional.  
Al principio se debía refrescar toda la pagina.  
- Posterior mediante porgramación asincrona no hace falta. Y sólo se refresca la parte que se requiere.  
- web 2.0  

Etiquetas. Las etiquetas sólo describen el contenido. No el aspecto.  
- DOCTYPE
- head. Cosas que salen en la pestaña de la pagina, como el titulo.  
- body. Cosas que salen en la pagina en blanco.  
- header
- nav.  Barra de navegación.  
- title
- meta: metadatos. Description, authon, keywords,...  
- p, p1..p6
- h, h1..h6. También hay un hgroup para agruparlos.  
- ul: lista desordenada.  
- li: list item
- section.  
- article.  
- aside. barra lateral
- footer.  
- a href. link a otra pagina.  

APIs HTML5
- Canvas  
- Drag & drop
- Geolocation
- Storage
- File
- Web workes
- History
- Offline




# Javascript
ver arriba javascript.  


# CSS
CSS3 sirve para hacer responsive design.  
- Hacer que una web se adapte a cualquier dispositivo. PC, movil, tablet,...  
- hace que sea multiplataforma.  
Varios frameworks
- Bootstrap.  
- Fundation 3.  
- HTML 5 Boilerplate.  



# Síncrono
En una comunicación sincrona, cuando el cliente hace una petición al servidor, éste se queda a la espera del servidor.
No permite continuar con la interacción del usuario mientras estamos en esa espera.  


# Asíncrono
Cuando el cliente hace una petición al servidor, no se queda bloqueado a la espera.  
AJAX está en medio de ambos y es el que gestiona la petición, y la respuesto. En ambos sentidos.  
Y cuando se obtiene respuesta sólo se refresca esa parte.  
De está forma la pagina web es mucho más fluida, y el rendimiendo es mucho mejor al no tener que recargar todo cada vez.  


# Interfaz
El medio con el que se comunica el usuario con una máquina.  
Puede ser un interfaz gráfico, línea de comandos, control por voz, táctil,...  
Permite muchas funcionalidades:  
- Poner en marcha o apagar el equipo.  
- Configuración del equipo.  
- Comunicación con otros sistemas.  
- ...