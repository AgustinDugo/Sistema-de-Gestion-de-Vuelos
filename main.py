from funciones.menu import menu
"""
Ejercicio 4
✈️ Sistema de Gestión de Vuelos – Aerolínea “SkyWings"
La aerolínea SkyWings necesita un sistema básico para administrar la información de sus vuelos. Cada vuelo contiene los siguientes datos:
Código del vuelo (número de al menos 5 dígitos)
Ciudad de destino
Precio del boleto
La información se almacenará en una matriz (lista de listas), donde cada fila representa un vuelo y las columnas contienen los datos mencionados.
📋 Requerimientos del sistema
Menú Principal
Mostrar un menú con las siguientes opciones:
Cargar vuelo/s
Buscar vuelo por código
Mostrar vuelo más caro
Mostrar vuelo más barato
Mostrar vuelos con precio mayor a 100000
Salir


Cargar vuelos
Crear una función que permita al usuario ingresar los datos de uno o más vuelos.
El usuario debe indicar cuántos vuelos desea cargar.
Por cada vuelo se solicitará:
Código del vuelo: debe ser un número entero de 5 o más dígitos. Si no cumple, debe pedirse nuevamente.
Ciudad de destino.
Precio del boleto.
La carga se realiza en una matriz predefinida, sin usar métodos de listas.


Buscar vuelo por código
Permitir al usuario ingresar el código de un vuelo.
Si existe, mostrar todos los datos correspondientes.




Mostrar vuelo más caro
Crear una función que recorra la matriz y muestre el vuelo con el precio más alto.


Mostrar vuelo más barato
Crear una función que recorra la matriz y muestre el vuelo con el precio más bajo.


Mostrar vuelos con precio mayor a 100000
Mostrar todos los vuelos cuyo precio supere ese valor.


⚙️ Requisitos técnicos
Se deben utilizar funciones para cada operación.
Está prohibido el uso de:
Métodos de listas (append(), remove(), etc.)
Listas por comprensión
try-except
Clases
Funciones incorporadas de Python (salvo len() e isdigit())
Para almacenar los datos, se debe inicializar una matriz de tamaño fijo con espacio para hasta 100 vuelos:

Los vuelos se deben cargar “a mano” en posiciones libres de esa matriz.
Si el usuario selecciona una opción sin haber cargado vuelos, se debe mostrar un mensaje indicando que no hay datos disponibles para la operación.


"""

TAM_MAX = 100

vuelos = [None] * TAM_MAX

vuelos_cargados = 0





