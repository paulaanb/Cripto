
def atbash_cifrar_descifrar(mensaje, alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    # Crear el alfabeto invertido
    alfabeto_invertido = alfabeto[::-1]
    # Crear un diccionario para mapear cada letra a su opuesta
    diccionario_atbash = {alfabeto[i]: alfabeto_invertido[i] for i in range(len(alfabeto))}
    # Cifrar o descifrar el mensaje
    mensaje_transformado = ''.join([diccionario_atbash[letra] if letra in diccionario_atbash else letra for letra in mensaje.upper()])
    return mensaje_transformado

# Ejemplo de uso
mensaje_original = "HELLO"
mensaje_cifrado = atbash_cifrar_descifrar(mensaje_original)
mensaje_descifrado = atbash_cifrar_descifrar(mensaje_cifrado)

print("Mensaje original ejemplo:", mensaje_original)
print("Mensaje cifrado ejemplo:", mensaje_cifrado)
print("Mensaje descifrado ejemplo:", mensaje_descifrado)


# Corregir el error en el código para descifrar correctamente el mensaje

# Crear un diccionario para el cifrado Atbash basado en el alfabeto español (A-Z, omitiendo la ñ)
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabeto_invertido = alfabeto[::-1]
atbash_dict = {alfabeto[i]: alfabeto_invertido[i] for i in range(len(alfabeto))}

# Mensaje cifrado
mensaje_cifrado = "GSVUOZTRHHZBDVZIVXIZA"

# Función para descifrar el mensaje
def descifrar_atbash(mensaje_cifrado, diccionario):
    return ''.join([diccionario[letra] if letra in diccionario else letra for letra in mensaje_cifrado])

# Descifrar el mensaje
mensaje_descifrado = descifrar_atbash(mensaje_cifrado, atbash_dict)
mensaje_descifrado
print("Mensaje descifrado del ejercicio dado:", mensaje_descifrado)