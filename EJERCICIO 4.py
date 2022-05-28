print("=====================================================")
print("Ingrese los valores de ancho y largo de la BANDERA")
print("=====================================================")
print("        Ingrese valores impares entre 3 y 19         ")
print("=====================================================")


Bandera= True

while (Bandera):

    Lhorizontal = int(input("Valor de Lhorizontal:"))

    if (Lhorizontal%2 == 0):
         print("ingrese un numero impar de 3 al 19 para el Lhorizontal")
         bandera= True

    elif (3 > Lhorizontal) :
         print("ingrese un numero impar de 3 al 19 para el Lhorizontal", end= '')
         bandera= True

    elif (20 < Lhorizontal) :
         print("ingrese un numero impar de 3 al 19 para el Lhorizontal", end= '')
         bandera= True

    else:
         print("su Lhorizontal es: "+ str (Lhorizontal))
         bandera= False
         print("\n")
         break




while (Bandera):

    Haltura = int(input("Valor de Haltura:"))
    
    if (Haltura%2 == 0):
         print("ingrese un numero impar de 3 al 19 para el ", end= '')
         bandera=True

    elif (Haltura > 20):
         print("ingrese un numero impar de 3 al 19 para el ", end= '')
         bandera= True
    
    elif (Haltura < 3):
         print("ingrese un numero impar de 3 al 19 para el ", end= '')
         bandera= True

    else:
         print("su Haltura es: "+ str (Haltura))
         bandera=False
         print("\n")
         break
  
operacion1 = (Lhorizontal/2)-0.1
operacion2 = (Haltura/2)-0.1


centrohizontaldebandera = round(operacion1, 0)
centroverticaldebandera = round(operacion2, 0)

for j in range(Haltura):
     for i in range(Lhorizontal):
             if (j == centroverticaldebandera) and (0 <= i <= Lhorizontal):
                 print('+', end='')

             elif (i == centrohizontaldebandera) and (0 <= j <= Haltura):
                 print('+', end='')
            
             else:
                 print("0", end='')
     print()
        
    
    
print('\n\n')
