# Cripto
El link del repositorio es [Criptografia](https://github.com/paulaanb/Cripto).

## Primera Entrega Atbash
# Cifrado Atbash

El cifrado Atbash es un tipo de cifrado por sustitución en el que se invierte el alfabeto para el cifrado de mensajes. Originario del alfabeto hebreo, puede aplicarse a cualquier alfabeto, y es conocido por su simplicidad y la simetría de su cifrado y descifrado.

## Descripción del Algoritmo

El cifrado Atbash reemplaza cada letra del alfabeto por su letra opuesta. Por ejemplo, la primera letra se cifra como la última, la segunda como la penúltima, y así sucesivamente.

### Fórmula Matemática

Para un alfabeto de \(N\) letras, la transformación de la posición \(i\) de una letra a su posición cifrada \(i'\) se calcula con la fórmula:

i' = (N - 1) - i

donde \(i\) es la posición original de la letra (comenzando desde 0), y \(N\) es el número total de letras en el alfabeto.

## Implementación en Python

```python
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
