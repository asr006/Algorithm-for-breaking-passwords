# Algorithm-for-breaking-passwords
Trabajo en clase

Este es mi trabajo en clase que hice en Python para entender cómo funcionan los ataques de fuerza bruta. Básicamente, el código intenta adivinar una contraseña probando todas las combinaciones posibles de letras, una por una.

El script busca una contraseña de hasta 4 letras (en este caso puse "agpd"). Lo que hace es:
Probar todas las letras de la a a la z.
Si no la encuentra, prueba con combinaciones de 2 letras (aa, ab, ac...).
Luego con 3 letras.
Y finalmente con 4 letras hasta que da con la correcta.
Al terminar, me dice cuántos intentos le tomó y cuánto tiempo tardó en encontrarla.

Cómo usarlo:
Se debe colocar una contraseña en la variable contraseña, solo se puede de hasta 4 letras y minisculas

Ejemplos de salida:
Dependiendo de la contraseña que pongas en el código, verás algo como esto en tu pantalla:

Ejemplo con contraseña "agpd":

Contraseña encontrada: agpd
Intentos realizados:  11634
El tiempo fue:  1711382500.123

Reflexión: ¿Qué pasa con contraseñas largas?
Si intentamos usar este mismo método para una contraseña de 8 o más caracteres que incluya mayúsculas, números y símbolos, esto es lo que pasaría:

Al agregar números (0-9) y símbolos (!@#$), el "alfabeto" que la computadora debe recorrer crece muchísimo. Ya no son solo 26 letras, sino más de 90 caracteres posibles.

Con una contraseña de 8 caracteres complejos, una computadora normal podría tardar años o incluso décadas en encontrarla mediante fuerza bruta simple.

El programa se volvería muy lento porque el número de combinaciones sube de forma exponencial.

GRAFICA:
Lamentablemente a la hora de ejecutar el código para la gráfica, no permite visualizar en el codespace, asi que tuve que hacer la grafica de manera local en mi pc para poder tomarle captura y unirla al repositorio. De todas maneras igual ahi está el código para poder ejecutarlo de forma local.

