
from math import sqrt

print("==============================================================")
print("                       Ingrese la data                        ")
print("==============================================================")
print("SI desea deterner el ingreso de dato presione * y dele enter  ")
print("==============================================================")


def desviacion_estandar(valores, media):
    suma=0
    for valor in valores:
        suma += (valor - media) ** 2


    radicando = suma / (len(valores) - 1)

    return sqrt(radicando)


def calcular_media(valores):
    suma=0

    for valor in valores:
        suma += valor

    return suma / len(valores)

def calcular_rango(valores):
    
     min = max = valores[0]
     for valor in valores:
        if valor < min:
            min = valor
        elif valor > max:
            max = valor

     return  max - min 


def median(valores):
    half = len(valores) // 2
    valores.sort()
    if not len(valores) % 2:
        return (valores[half - 1] + valores[half]) / 2.0
    return valores[half]


if __name__ == "__main__":

    numeros = []
    
    contador = 1
    mensaje_solicitud ="Ingrese la Data"

    Data_string = int(input("{} {}:".format(mensaje_solicitud, contador)))

    while Data_string != "*":
        contador += 1
        numeros.append(int(Data_string))
        Data_string = input("{} {}:".format(mensaje_solicitud, contador))
        
        

    print("\n")
    print("Se termino el ingreso de Data")
    print("\n\n")



    media = calcular_media(numeros)

    mediana = median(numeros)

    rango = calcular_rango(numeros)

    resultado = desviacion_estandar(numeros, media)


    print(numeros) 
    print('')
    print('la media es: {}'.format(media))
    print('')
    print ('la mediana es: {}'.format(mediana))
    print('')
    print("el rando es: {}".format(rango))
    print('')
    print('La desviacion estandar es: {}'.format(resultado))
    print("\n\n")
    
