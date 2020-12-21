import math
cEdades = 5
menor = 0
mayor = 0
nPar = 0
nImp = 0
mayorFact = 0

def operador(n):
    edad = int(n)
    global cEdades
    global menor
    global mayor
    global nPar
    global nImp
    global mayorFact
    if cEdades == 5:
        menor = edad
        mayor = edad
    if edad < menor:
        menor = edad
    if edad > mayor:
        mayor = edad
    if edad % 2 == 0:
        nPar += 1
    else:
        nImp += 1
    fact = math.factorial(edad)
    if mayorFact < fact:
        mayorFact = fact
    cEdades -=1
        

            
while cEdades > 0:
    print("Introduce una edad valida. Quedan: ",cEdades)
    i = input()
    try:
        edad = int(i)
        if edad > 18 and edad < 65:
            operador(i)
        else:
            print("Eso no es una edad válida.")
    except ValueError:
        print("Eso no es una edad válida")
else:
    print("El menor tiene: ", menor, " años")
    print("El mayor tiene: ", mayor, " años")
    print("Hay: ", nPar, " pares")
    print("Hay: ", nImp, " impares")
    print("El mayor factorial es: ", mayorFact)
    print("Fin del Programa")
