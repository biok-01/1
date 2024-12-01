ent = open('contrasenas.txt')
resultados = []

#Procesar cada línea del archivo.
for linea in ent:
    contrasena = linea.rstrip('\n')
    
    #Verificar si la contraseña contiene al menos una vocal.
    tiene_vocal = False
    i = 0
    while i < len(contrasena):
        if contrasena[i] in 'aeiou':
            tiene_vocal = True
        i += 1
    
    #Si no tiene vocal, la contraseña no es aceptable.
    if not tiene_vocal:
        resultados.append(contrasena + " -> No es aceptable.")
        continue
    
    #Verificar que no haya tres vocales o tres consonantes consecutivas.
    i = 0
    es_valida = True
    while i < len(contrasena) - 2:
        v1, v2, v3 = contrasena[i], contrasena[i+1], contrasena[i+2]
        if (v1 in 'aeiou' and v2 in 'aeiou' and v3 in 'aeiou') or (v1 not in 'aeiou' and v2 not in 'aeiou' and v3 not in 'aeiou'):
            es_valida = False
        i += 1
    
    #Verificar que no tenga dos letras consecutivas iguales, excepto 'ee' y 'oo'.
    i = 0
    while i < len(contrasena) - 1:
        if contrasena[i] == contrasena[i + 1] and contrasena[i:i + 2] not in ['ee', 'oo']:
            es_valida = False
        i += 1
    
    #Agregar la contraseña con el mensaje correspondiente.
    if es_valida:
        resultados.append(contrasena + " -> Es aceptable.")
    else:
        resultados.append(contrasena + " -> No es aceptable.")

ent.close()

#Limpiar el archivo de salida (si ya existía).
salida = open('resultados.txt', 'a')
salida.truncate(0)
salida.close()

# Escribir las contraseñas con sus mensajes en el archivo de salida.
salida = open('resultados.txt', 'a')
for resultado in resultados:
    salida.write(resultado + '\n')
salida.close()

print("Se han procesado las contraseñas y los resultados están en \"resultados.txt\".")
