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

