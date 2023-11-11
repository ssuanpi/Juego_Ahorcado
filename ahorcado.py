import random
from palabras import listaPalabras

def obtener_palabra():
    palabra = random.choice(listaPalabras)
    return palabra.upper()

def juego(palabra):
    palabra_completa = "-" * len(palabra)
    adivinado = False
    letras_adivinadas = []
    palabras_adivinadas = []
    intentos = 6
    print("Vamos a jugar al ahorcado!")
    print(fasesAhorcado(intentos))
    print(palabra_completa)
    print("\n")
    while not adivinado and intentos > 0:
        adivinar = input("Adivina una letra o la palabra: ").upper()
        if len(adivinar) == 1 and adivinar.isalpha():
            if adivinar in letras_adivinadas:
                print(f"La letra {adivinar} ya la haz intentado!")
            elif adivinar not in palabra:
                print(f"La letra {adivinar} no está en la palabra.")
                intentos -= 1
                letras_adivinadas.append(adivinar)
            else:
                print(f"La letra {adivinar} está en la palabra!")
                letras_adivinadas.append(adivinar)
                palabra_lista = list(palabra_completa)
                indices = [i for i, letra in enumerate(palabra) if letra == adivinar]
                for indice in indices:
                    palabra_lista[indice] = adivinar
                palabra_completa = "".join(palabra_lista)
                if "-" not in palabra_completa:
                    adivinado = True
        elif len(adivinar) > 1 and adivinar.isalpha():
            if adivinar in palabras_adivinadas:
                print("Ya intentaste adivinar esa palabra!")
            elif adivinar != palabra:
                print(adivinar, " no es la palabra.")
                intentos -= 1
                palabras_adivinadas.append(adivinar)
            else:
                adivinado = True 
                palabra_completa = palabra
        else:
            print("El valor introducido, no es valido!")
        print(fasesAhorcado(intentos))
        print(palabra_completa)
        print("\n")
    
    
    if adivinado is True:
        print("Felicitaciones, adivinaste la palabra! Ganaste")
    else:
        print(f"Perdiste.. se te acabaron los intentos. La palabra era {palabra}")



def fasesAhorcado(intentos): 
    etapas =    [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return etapas[intentos]


def main():
    palabra = obtener_palabra()
    juego(palabra)
    while input("Jugar de nuevo? (S/N)").upper() == "S":
        palabra = obtener_palabra()
        juego(palabra)

if __name__ == "__main__":
    main()