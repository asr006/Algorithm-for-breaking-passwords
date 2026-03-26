import time

alfabeto = "abcdefghijklmnopqrstuvwxyz"
contraseña = "agpd"
inicio = time.time()
intentos = 0
encontrado = False

for i in alfabeto:
    intento = i
    intentos += 1
    if intento == contraseña:
        encontrado = True
        break
    
if encontrado == False:
    for i in alfabeto:
        for j in alfabeto:
            intento = i + j
            intentos += 1          
            if intento == contraseña:
                encontrado = True
                break
            
if encontrado == False:
    for i in alfabeto:
        for j in alfabeto:
            for k in alfabeto:
                intento = i + j + k
                intentos += 1
                if intento == contraseña:
                    encontrado = True
                    break
            if encontrado == True:
                break
        if encontrado == True:
            break
                
if encontrado == False:
    for i in alfabeto:
        for j in alfabeto:
            for k in alfabeto:
                for l in alfabeto:
                    intento = i + j + k + l
                    intentos += 1
                    if intento == contraseña:
                        encontrado = True
                        break
                if encontrado == True:
                    break
            if encontrado == True:
                break
        if encontrado == True:  
            break
    
print ("Contraseña encontrada:", intento)
print ("Intentos realizados: ", intentos)
final = time.time()
print ("El tiempo fue: ", final)