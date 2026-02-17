# HowTo/Sockets

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# HOWTO de programación de sockets 

**Versión original de Gordon McMillan**

Traducción del [\"Socket Programming HOWTO\"](http://docs.python.org/howto/sockets.html)

Los sockets se usan casi en cualquier parte, pero son una de las tecnologías peor comprendidas. Este documento es una panorámica de los sockets. No se trata de un tutorial - debe poner trabajo de su parte para hacer que todo funcione. No cubre las cuestiones puntuales (y hay muchas), pero espero que le dé un conocimiento suficiente como para empezar a usarlos decentemente.

Este documento está disponible, en el idioma original, en [http://www.python.org/doc/howto](http://www.python.org/doc/howto). La versión original de esta traducción fue realizada por David Villa. Una versión actualizada se puede descargar de [http://arco.esi.uclm.es/\~david.villa/doc/repo/python-sockets/Socket-es.pdf](http://arco.esi.uclm.es/~david.villa/doc/repo/python-sockets/Socket-es.pdf), cuyo fuente está disponible en [https://arco.esi.uclm.es/svn/public/doc/python-sockets/](https://arco.esi.uclm.es/svn/public/doc/python-sockets/).

## Sockets 

Los sockets se usan casi en cualquier parte, pero son una de las tecnología peor comprendidas. Este documento es una panorámica de los sockets. No se trata de un tutorial - debes poner trabajo de tu parte para hacer que todo funcione. No cubre las cuestiones puntuales (y hay muchas), pero espero que le dé un conocimiento suficiente como para empezar a usarlos decentemente.

Sólo se van a tratar los sockets INET, pero éstos representan el 99% de los sockets que se usan. Y sólo se hablará de los STREAM sockets - a menos que realmente sepa lo que estás haciendo (en cuyo caso este documento no le será útil), conseguirá un comportamiento mejor y más rendimiento de un STREAM socket que de cualquier otro. Intentaré revelar el misterio de qué es un socket, así como las cuestiones relativas a cómo trabajar con sockets bloqueantes y no bloqueantes. Pero empezaré hablando sobre sockets bloqueantes. Necesita saber cómo trabajan los primeros antes de pasar a los sockets no bloqueantes.

Parte del problema para entender qué es \'socket\' puede significar unas cuantas cosas con sutiles diferencias, dependiendo del contexto. Lo primero de todo, hay que hacer una distinción entre socket \'cliente\' - un extremo de la conversación, y un socket \'servidor\', que es más como un operador de una centralita. La aplicación cliente (tu navegador, por ejemplo) usa exclusivamente sockets \'cliente\'; el servidor web con el que habla usa tanto sockets \'servidor\' como sockets \'cliente\'.

### Historia 

De las diferentes formas de IPC (Inter Process Communication), los sockets son de lejos la más popular. En una plataforma dada, probablemente hay otras formas de IPC más rápidas, pero para comunicaciones inter-plataforma, los sockets son casi la única elección.

Se inventaron en Berkeley como parte de la variante BSD de UNIX. Se extendieron muy rápidamente junto con Internet. Y con razón \-- la combinación de los sockets con INET hace que la comunicación entre máquinas cualesquiera sea increiblemente sencilla (al menos comparada con otros esquemas).

## Creación de un socket 

Cuando ha pulsado el enlace que le ha traído a esta página, su navegador ha hecho algo parecido a lo siguiente:

        # crea un socket INET de tipo STREAM
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # ahora se conecta al servidor web en el puerto 80 (http)
        s.connect(("www.mcmillan-inc.com", 80))

Cuando la conexión se completa, el socket se usa para enviar una petición para el texto de la página. El mismo socket puede leer la respuesta, y después se destruye. Sí, así es, se destruye. Los socket cliente normalmente sólo se usan para un intercambio (o una pequeña secuencia de ellos).

Lo que ocurre en el servidor es un poco más complejo. Primero el servidor web crea un \'socket servidor\'.

        # crea un socket INET de tipo STREAM
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # asocia el socket a un host público
        # y aun puesto bien conocido
        serversocket.bind((socket.gethostname(), 80))

        # lo convierte en socket servidor
        serversocket.listen(5)

Un par de cosas a tener en cuenta: cuando se usa `socket.gethostname()` el socket debería ser visible desde el exterior. Si hubiera usado `s.bind(('', 80))` or `s.bind(('localhost', 80))` or `s.bind(('127.0.0.1', 80))` también tendría un socket servidor, pero solo sería accesible desde la misma máquina

Una segunda cuestión: los puertos con número bajo normalmente están reservados para servicios \'bien conocidos\' (HTTP; SNMP, etc). Si está experimentando, use un número alto (4 dígitos)

Finalmente, el argumento de `listen()` le dice a la librería socket que quiere encolar un máximo de 5 peticiones de conexión (lo normal) antes de rechazar conexión externas. Si el resto del código está bien escrito, debería ser suficiente.

Bien, ahora tiene un socket servidor, escuchando en el puerto 80. Ahora entra en el bucle principal del servidor web.

        while True:
            # acepta conexiones externas
            (clientsocket, address) = serversocket.accept()
            # ahora se trata el socket cliente
            # en este caso, se trata de un servir multihilado
            ct = client_thread(clientesocket)
            ct.run()

Realmente, hay tres modos en los que este bucle puede trabajar - creando un hilo para manejar `clientsocket`, o reestructurar esta aplicación para usar sockets no bloqueantes, y *multiplexar* entre el socket servidor y uno de los clientsockets activos usando `select()`. Lo verá más adelante. La cuestión que es importante entender ahora es ésta: esto es {todo} lo que hace un socket servidor. No envía ningún dato. No recibe ningún dato. Simplemente produce un `clientsocket`. Un socket cliente se crea en respuesta a *otro* socket cliente que invoca `connect()` al host y puerto al que está vinculado el socket servidor. Tan pronto como se crea el socket cliente, se vuelve a escuchar en espera de nuevas conexiones. Los dos clientes son libres de hablar - usan un puerto temporal que se reciclará cuando la conversación termine.

### IPC 

Si necesita IPC rápida entre dos procesos en una misma máquina, debería echar un vistazo a otras formas de memoria compartida que ofrece la plataforma. Un protocolo simple basado en memoria compartida y semáforos es la técnica más rápida.

Si decide usar sockets, vincule el socket *servidor* a \'localhost\'. En otras plataformas, esto implica una atajo a través de varias capas del código de red y puede bastante rápido.

## Uso del socket 

Lo primero que debe tener en cuenta, es que le socket *cliente* del navegador web y el socket cliente del servidor web son idénticos. Es decir, es una conversación entre iguales. O por decirlo de otra manera, *como diseñador, debe decidir qué reglas de etiqueta utilizar en la conversación*. Normalmente el socket que conecta comienza la conversación, enviando una petición, o puede que una señal de inicio. Pero eso es una decisión de diseño - no es una norma de los sockets.

Ahora hay dos conjuntos de primitivas para usar en la comunicación. Puede usar `send()` y `recv()`, o puede transformar su socket cliente en algo similar a un fichero y usar `read()` y `write()`. Esta última forma es la que usa Java en sus sockets. No vamos a tratar ese tema aquí, excepto para advertir de la necesidad de usar `flush()` en los sockets. Hay *ficheros* buffereados, y un error habitual es escribir algo, y a continuación leer la respuesta. Si no se hace `flush()`, puede que tenga que esperar para siempre, porque la petición sigue en el buffer de salida.

Ahora llegamos al mayor tropiezo de los sockets - `send()` y `recv()` operan en buffers de red. No tratan necesariamente todos los bytes que se les entrega (o se espera de ellos), porque ellos están más preocupados de gestionar los buffers de red. En general, retornan cuando los buffers de red asociados se han llenado (`send()`) o vaciado (`recv()`). Es en esos momentos cuando informan de cuantos bytes han tratado. Es su responsabilidad invocar de nuevo hasta que el mensaje se haya aceptado completamente.

Cuando una llamada a `recv()` devuelve 0 bytes, significa que el otro lado ha cerrado (o está cerrando) la conexión. No recibirá más datos en esta conexión. Sin embargo, puede estar autorizado para enviar datos con éxito; veremos esto más adelante.

Un protocolo como HTTP usa un socket para una sola transferencia. El cliente envía una petición, lee la respuesta. Es decir. El socket es descartado. Esto significa que un cliente puede detectar el fin de una respuesta recibiendo 0 bytes.

Pero si planea reutilizar su socket para sucesivas transferencias, debe tener claro que no hay un EOT (*End of Transfer*) en un socket. Repito: si un `send()` o `recv()` indica que ha tratado 0 bytes, la conexión se ha roto. Si la conexión no se ha roto, debería esperar en un `revc()` para siempre, porque el socket nunca dirá que no queda nada más por leer (por ahora). Ahora, si piensa un poco en ello, se dará cuenta de una cuestión fundamental de los sockets: los mensajes deben tener longitud fija, o estar delimitado, o indicar su longitud (mucho mejor), o acabar cerrando la conexión. La elección corresponde únicamente al diseñador (aunque hay algunas maneras mejores que otras.

Suponiendo que no quiere terminar la conexión, la solución más simple es utilizar mensajes de longitud fijo.

        class mysocket:
            '''solo para demostración
              - codificado así por claridad, no por eficiencia'''
            def __init__(self, sock=None):
                if sock is None:
                    self.sock = socket.socket(
                        socket.AF_INET, socket.SOCK_STREAM)
                else:
                    self.sock = sock
            def connect(host, port):
                self.sock.connect((host, port))
            def mysend(msg):
                totalsent = 0
                while totalsent < MSGLEN:
                    sent = self.sock.send(msg[totalsent:])
                    if sent == 0:
                        raise RuntimeError, \\
                            "conexión interrumpida"
                    totalsent = totalsent + sent
            def myreceive():
                msg = ''
                while len(msg) < MSGLEN:
                    chunk = self.sock.recv(MSGLEN-len(msg))
                    if chunk == '':
                        raise RuntimeError, \\
                            "conexión interrumpida"
                    msg = msg + chunk
                return msg

El código de envío de este ejemplo se puede usar para casi cualquier esquema de intercambio de mensajes - en Python puede enviar cadenas, y puede usar `len()` para obtener la longitud (incluso si tiene caracteres `\e 0`. Normalmente, es el código de recepción el que es más complejo. (Y en C; no es mucho peor, excepto que no puede usar `strlen()` si el mensaje contiene `\e 0`).

La mejora más fácil es hacer que el primer carácter del mensaje sea un indicador del tipo del mensaje, y hacer que el tipo que determine la longitud. Ahora hay dos `recv()` - el primero lee (al menos) el primer carácter de modo que se puede averiguar el tamaño, y el segundo en un bucle para leer el resto. Si decide elegir el método del delimitador, recibirá un bloque de tamaño arbitrario, (de 4096 a 8192 normalmente es una buena elección para los tamaños de buffer de la red), y esperar a recibir el delimitador.

Una cuestión a tener en cuenta: si el protocolo conversacional permite múltiples mensajes consecutivos (sin ningún tipo de respuesta),y se le indica a `recv()` un bloque de tamaño arbitrario, puede acabar leyendo un trozo del siguiente mensaje. Necesitará guardarlo hasta que lo necesite.

Indicar la longitud del mensaje por medio de un prefijo (5 caracteres numéricos) es más complejo, porque (lo crea o no), puede no recibir esos cinco caracteres en un mismo `recv()`. Si todo va bien, funcionará; pero ante una carga alta de red, el programa fallará a menos que use dos bucles para la recepción - el primero determinará la longitud, el segundo leeerá el mensaje. Horrible. Algo similar ocurre cuando descubra que `send()` no siempre puede enviar todo en una sola pasada. Y a pesar de haber leído esto, es posible que sufra este problema de todos modos!

Para no extenderme demasiado, (y preservar mi posición privilegiada), estas mejoras se dejan como ejercicio para el lector.

### Datos binarios 

Es perfectamente posible enviar datos binarios a través de un socket. El mayor problema es que no todas las máquinas usan los mismos formatos para datos binarios. Por ejemplo, un chip Motorola representa un entero de 16 bit con el valor 1 como dos bytes 0x00 0x01 (*big endian*). Intel y DEC, sin embargo, usan ordenamiento invertido - el mismo 1 es 0x01 0x00 (*little endian*). Las librerías de socket tienen funciones para convertir enteros de 16 y 32 bits - `ntohl(),   htonl(), ntohs(), ntohs()` donde \'n\' significa red(*network*), \'h\' significa *host*, \'s\' significa corto(*short*) y *l* significa \'largo\'(*large*}). Cuando el ordenamiento de la red es el mismo que el del host, estas funciones no hacen nada, pero cuando la máquina tiene ordenamiento invertido, intercambian los bytes del modo apropiado.

En estos tiempos de máquinas de 32 bits, la representación ASCII de datos binarios normalmente ocupa menos espacio que la representación binaria. Se debe a que en una sorprendente cantidad de veces, todos esos \'longs\' tienen valor 0, o 1. La cadena \'0\' serían dos bytes, mientras que en binario serían cuatro. Por supuesto, eso no es conveniente con mensajes de longitud fija. Decisiones, decisiones.

## Desconexión 

Estrictamente hablando, se supone que se debe usar `shutdown()` en un socket antes de cerrarlo con `close()`. `shutdown()` es un aviso al socket del otro extremo. Dependiendo del argumento que se pasa, puede significar \"No voy a enviar nada más, pero seguiré escuchando\", o \"No estoy escuchando\". La mayoría de las librerías de sockets, no obstante, son tan usadas por programadores que descuidan el uso de esta muestra de buena educación que normalmente `close()` es lo mismo que `shutdown()`. De modo que en la mayoría de los casos, no es necesario un `shutdown()` explícito.

Una forma para usar `shutdown()` de forma efectiva es en un intercambio tipo HTTP. El cliente envía una petición y entonces ejecuta `shutdown(1)`. Esto le dice al servidor \"Este cliente ha terminado de enviar, pero aún puede recibir\". El servidor puede detectar \"EOF\" al recibir 0 bytes. Puede asumir que ha completado la petición. El servidor envía una respuesta. Si el envío se completa satisfactoriamente entonces, realmente, el cliente estaba aún a la escucha.

Python lleva el `shutdown()` automático un paso más allá, cuando el recolector de basura trata un socket, automáticamente hará el `close()` si es necesario. Pero confiar en eso es un muy mal hábito. Si un socket desaparece sin cerrarse, el socket del otro extremo puede quedar bloqueado indefinidamente, creyendo que este extremo simplemente es lento. Por favor, cierre los sockets cuando ya no los necesite.

### Cuando los sockets mueren 

Probablemente lo peor que puede pasar cuando se usan sockets bloqueantes es lo que sucede cuando el otro extremo cae bruscamente (sin ejecutar un `close()`). Lo más probable es que el socket de este extremo \"se cuelgue\". SOCKSTREAM es un protocolo fiable, y esperará durante mucho, mucho tiempo antes de abandonar la conexión. Si está usando hilos, el hilo completo estará muerto en la práctica. No hay mucho que pueda hacer. En tanto que no haga alguna cosa absurda, como mantener un bloqueo (lock) mientras hace una lectura bloqueante, el hilo no está consumiendo realmente muchos recursos. No intente matar el hilo - parte del motivo por que los hilos son más eficientes que los procesos es que no incluyen la sobrecarga asociada a reciclarlo automático de recursos. En otras palabras, si intenta matar el hilo, es probable que fastidie el proceso completo.

## Sockets no bloqueantes 

Si ha comprendido todo lo anterior, ya sabe más que de lo que necesita saber sobre la mecánica de los sockets. Usará casi siempre las mismas funciones, y del mismo modo. Sólo es eso, si lo hace bien no tendrá problemas.

En Python, se usa `socket.setblocking(0)` para hacer un socket no bloqueante. En C, es más complicado, (necesita elegir entre BSD modo O_NONBLOCK o el casi idéntico Posix modo O_NDELAY, que es completamente diferente de TCP_NODELAY), pero es exactamente la misma idea. Eso se hace después de crear el socket, pero antes de usarlo. Realmente, si está un poco chiflado, puede cambiar entre un modo y otro

La diferencia más importante es que `send()`, `recv()`, `connect()` y `accept()` puede volver sin haber hecho nada. Hay, por supuesto, varias alternativas. Puede comprobar el valor de retorno y el código de error y generalmente volverse loco. Si no lo cree, debería intentarlo alguna vez. Su aplicación pronto será grande, pesada y llena de errores. De modo que pasemos de las soluciones absurdas y hagámoslo bien.

Use `select()`.

En C, escribir código para `select()` puede ser complicado. En Python, está chupado, pero es lo suficientemente parecido a la versión C como para que si entiende `select()` en Python, no tenga muchos problemas en C.

        listo_para_leer, listo_para_escribir, en_error = \\
             select.select(lectores_potenciales,
                           escritores_potenciales,
                           errores_potenciales,
                           timeout)

A `select()` se le pasan tres listas: la primera contiene todos los sockets de los que quiere intentar leer; la segunda todos los sockets en los que quiere intentar escribir, y por último (normalmente vacía) aquellos en los que quiere comprobar se se ha producido un error. La llamada a `select()` es bloqueante, pero se le puede indicar un timeout. Generalmente es es aconsejable indicar un timeout - indique un tiempo largo (digamos un minuto) a menos que tenga una buena razón para hacer otra cosa.

Al retornar, devuelve tres listas. Son las listas de sockets en los que realmente se puede leer, escribir y tienen un error. Cada una de esas listas es un subconjunto (puede que vacío) que la lista correspondiente que se paso como parámetro en la llamada. Y si pone un socket en más de una lista de entrada, sólo estará (como mucho) en una de las listas de retorno.

Si un socket está un la lista de salida de \"legibles\", puede estar seguro que al invocar `recv()` recibirá algo. Lo mismo es aplicable a la lista de \"escribibles\". Puede que esto no es lo que quería, pero algo es mejor que nada. (Realmente, cualquier socket razonablemente sano retornará como \"escribible\" - únicamente significa que hay espacio disponible en el buffer de salida de red.

Si se tiene un socket \"servidor\", se debe poner en la lista de lectores_potenciales. Si retorna en la lista de \"legibles\", una invocación a `accept()` funcionará casi con toda seguridad. Si se crea un socket nuevo para conectar a algún sitio, debe ponerse en la lista de escritores_potenciales. Si aparece en la lista de \"escribibles\", existen ciertas garantías de que haya conectado.

Hay un problema muy feo con `select()`: Si en alguna de las listas de entrada hay un socket que ha muerto de mala manera, `select()` fallará. Entonces necesitará recorrer todos los sockets (uno por uno) de las tres listas y hacer `select([sock],[],[],0)` hasta que encuentre al responsable. El timeout 0 significa que debe retornar inmediatamente.

En realidad, `select()` puede ser útil incluso con sockets bloqueantes. Es un modo para determinar si quedará bloqueado - el socket retorna como \"legible\" cuando hay algo en el buffer. Sin embargo, esto no ayuda con el problema de determinar si el otro extremo ha terminado, está ocupado con otra cosa.

**Advertencia de portabilidad**: En UNIX, `select()` funciona tanto con sockets como con ficheros. No intente esto en Windows. En Windows, `select()` sólo funciona con sockets. También debe notar que en C, muchas de las opciones avanzadas con sockets son diferentes en Windows. De hecho, en Windows normalmente se usan hilos (que funcionan muy bien) con sockets. Si quiere rendimiento, su código será muy diferente en Windows y en UNIX.

### Rendimiento 

No hay duda de que el código más rápido es el que usa sockets no bloqueantes y `select()` para multiplexarlos. Se puede enviar una cantidad inmensa de datos que saturen una conexión LAN sin que suponga una carga excesiva para la CPU. El problema es que una aplicación escrita de este modo no puede hacer mucho más - necesita estar lista para generar bytes en cualquier momento.

Asumiendo que se supone que su aplicación hará algo más que eso, utilizar hilos es la solución óptima, (y usar sockets no bloqueantes es más rápido que usar sockets bloqueantes). Desafortunadamente, el soporte de hilos en los UNIX\'es varia en API y calidad. Así que la solución habitual en UNIX es crear un subproceso para manejar cada conexión. La sobrecarga que eso supone es significativa (y en Windows ni lo haga - la sobrecarga por la creación de procesos es enorme en Windows). También implica que, a menos que cada subproceso sea completamente independiente, necesitarás usar otra forma de IPC, como tuberías, o memoria compartida y semáforos, para comunicar el padre y los procesos hijos.

Finalmente, recuerde que a pesar de que los sockets bloqueantes son algo más lentos que los no bloqueantes, en mucho casos son la solución \"correcta\". Después de todo, si su aplicación reacciona ante los datos que recibe de un socket, no tiene mucho sentido complicar la lógica sólo para que la aplicación pueda esperar en un `select()` en lugar de en un `recv()`.
