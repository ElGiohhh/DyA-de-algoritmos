from num2words import num2words

def numero_a_letra(numero):
    try:
        numero_entero = float(numero)
        if numero_entero < 0:
            return "No se admiten números menores a 0"
        elif numero_entero == 0:
            return "Cero"
        else:
            numero_en_letras = num2words(numero_entero, lang='es')
            return numero_en_letras
    except ValueError:
        return "Por favor, introduce cualquier valor"

numero = input("Introduce un número: ")
resultado = numero_a_letra(numero)
print("El número es:",resultado)