import sys

ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

if len(sys.argv) > 1:
    num1 = int(sys.argv[1])
    print(f"El número de prueba es: {num1}")
    print("Los meses con ventas mayores al umbral ingresado son:")

    for mes, monto in ventas.items ():
        if monto > num1:
            print(f"{mes} : {monto}")

else:
    print("Error! Ingrese un número de prueba.")            