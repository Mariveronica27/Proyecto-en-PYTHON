print("=====================================================")
print("Ingrese el monto de dinero que desee retirar")
print("=====================================================")


Dinero = int(input("Ingrese monto a retirar: "))

list =[100, 50, 20, 10, 5, 1]

for i in list:
    if Dinero >= i:
        queda = Dinero // i
        print("Tienes "+ str(queda) + (" Billete" if queda == 1 else ' Billetes')+ " de "+ str(i)+ "$" )
        Dinero = Dinero % i
  


print('\n')
print('Gracias por eligir Bank of America')
print('\n\n')
