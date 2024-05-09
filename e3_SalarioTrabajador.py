LEER_HORAS_TRABAJADAS=int(input("Por favor inserte un número de horas trabajadas: "))
LEER_TARIFA=int(input("Por favor inserte la tarifa por hora: "))

UMBRAL_HORAS_TRABAJADAS=40
INCREMENTO_TARIFA=0.5

def calcularSalario(HORASTRABAJADAS ,TARIFA):      

    if(HORASTRABAJADAS<=UMBRAL_HORAS_TRABAJADAS):
        sueldo=(HORASTRABAJADAS)*TARIFA
        return sueldo
    if(HORASTRABAJADAS>UMBRAL_HORAS_TRABAJADAS):
        sueldo=(UMBRAL_HORAS_TRABAJADAS)*TARIFA
        nueva_tarifa=TARIFA*(1+INCREMENTO_TARIFA)
        extra=(HORASTRABAJADAS-UMBRAL_HORAS_TRABAJADAS)*nueva_tarifa
        return sueldo+extra
    
salarioTotal=calcularSalario(LEER_HORAS_TRABAJADAS,LEER_TARIFA)
print("El salario total de este trabajador es de: ",salarioTotal)