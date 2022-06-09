from cmath import sqrt
from itertools import islice

print("=========================================================")
print("   Ingrese las variaciones estequiometricas de cada dia  ")
print("=========================================================")
print("   Si desea detener el ingreso de datos coloque 0 tanto  ")
print("para variacion minima y variacion maxima y presione enter")
print("=========================================================")

def group_elements(lst, chunk_size):
    lst = iter(lst)
    return iter(lambda: tuple(islice(lst, chunk_size)), ())


def calcular_Lista_de_variaciones(valores):
    Lista_de_variaciones = []
    for valor in valores:
        if (0<=valor[1]<=50) and (0<=valor[0]<=50):    
            Lista_de_variaciones.append(valor[1]-valor[0])
    return  Lista_de_variaciones


def variacion_media_maxima(lista):
    max = lista[0]
    for x in lista:
        if x > max:
            max = x
    return max    

def variacion_media_minima(lista):
    min = lista[0]
    for x in lista:
        if x < min:
            min = x
    return min

def calcular_variacion_media_promedio(valores):
    suma = 0
    
    for valor in valores:
        suma += valor   
    return  (suma)/len(valores)
    

if __name__ == "__main__":

    Variaciones_gravimetricas = []
    mensaje_solicitud1 ="Ingrese la variacion minima del dia "
    mensaje_solicitud2 ="Ingrese la variacion maxima del dia "
    contador = 1
    Data_string1 = float(input("{} {}: ".format(mensaje_solicitud1, contador)))
    Data_string2 = float(input("{} {}: ".format(mensaje_solicitud2, contador)))
    print('')

    se_detiene = True

    while se_detiene:
        if (Data_string1 == 0) and (Data_string2 == 0):
            se_detiene = False
        else:
            contador += 1
            Variaciones_gravimetricas.append(Data_string1)
            Variaciones_gravimetricas.append(Data_string2)
            Data_string1 = float(input("{} {}: ".format(mensaje_solicitud1, contador)))
            Data_string2 = float(input("{} {}: ".format(mensaje_solicitud2, contador)))
            print('')

    print(Variaciones_gravimetricas)
    print('')
    numero = 1
    mensaje_solicitud3 = "Variaciones del dia"
    variacion_del_dia = []
    Lista_de_tuples = []
    for new_list in group_elements(Variaciones_gravimetricas , 2):
        print('{} {}: '.format(mensaje_solicitud3, numero))
        variacion_del_dia = print(new_list)
        Lista_de_tuples.append(new_list)
        numero += 1
        print('')

print("Lista con errores de variaciones gravimetricas")
print(Lista_de_tuples)
print('')


numero_de_la_lista = 0
numero_errores_menores = 1
numero_errores_mayores = 1
numero_errores_ambos = 1

while numero_de_la_lista < len(Lista_de_tuples):

    if Lista_de_tuples[numero_de_la_lista][0] < -100:
        print('Variaciones gravimetricas con errores menores a -100, {}:'.format(numero_errores_menores))
        print(Lista_de_tuples[numero_de_la_lista])
        numero_errores_menores += 1
    

    elif Lista_de_tuples[numero_de_la_lista][1] > 100:
        print('Variaciones gravimetricas con errores mayores a 100, {}:'.format(numero_errores_mayores))
        print(Lista_de_tuples[numero_de_la_lista])
        numero_errores_mayores += 1

    elif Lista_de_tuples[numero_de_la_lista][1] > 100 and Lista_de_tuples[numero_de_la_lista][0] < -100:
        print('Variaciones gravimetricas con errores mayores a 100, {}:'.format(numero_errores_mayores))
        print(Lista_de_tuples[numero_de_la_lista])
        numero_errores_ambos += 1

    else:
        numero_de_la_lista += 1
    break

print('')

lista_de_promedios = calcular_Lista_de_variaciones(Lista_de_tuples)

promedio = calcular_variacion_media_promedio(lista_de_promedios)

Variacion_maxima = variacion_media_maxima(lista_de_promedios)

Variacion_minima = variacion_media_minima(lista_de_promedios)

print("===============================================================")
print("Cantidad de dias que tuvieron errores mayores a 100: {}".format(numero_errores_mayores + numero_errores_ambos))
print('')
print("Cantidad de dias que tuvieron errores menores a -100: {}".format(numero_errores_menores + numero_errores_ambos))
print('')
print("Cantidad de dias que tuvieron ambos errores: {}".format(numero_errores_ambos))
print('')
print("lista de promedio: {}".format(lista_de_promedios))
print('')
print("Variacion media maxima: {}".format(Variacion_maxima))
print('')
print("Variacion media minima: {}".format(Variacion_minima))
print('')
print("Variacion media promedio: {}".format(promedio))
print('')
print("La salida de campo duro en dias: {}".format(contador - 1))
print('\n')
