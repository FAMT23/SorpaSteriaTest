NUMERO=int(input("Por favor inserte un número entero: "))

def parImpar(num):
    if(num%2==0 or num==0):
        return True
    else:
        False
        
if(parImpar(NUMERO)):
    print("El número insertado es par\nEl listado de sus pares menores de forma descendientes es")
    for i in range(0,NUMERO+1):
        if(parImpar(NUMERO-i)):print(NUMERO-i)
else:
    print("El número insertado es impar\nEl listado de sus impares menores de forma descendientes es:")
    for i in range(0,NUMERO):
        if not (parImpar(NUMERO-i)):print(NUMERO-i)